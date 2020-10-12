from tqdm import trange
from collections import OrderedDict

from graffiti.graffiti.request import Request
from graffiti.graffiti.graph import Graph
from graffiti.graffiti.report import Report
from graffiti.graffiti.config import Config
from graffiti.graffiti.database import Database
from graffiti.graffiti.style import Style

cfg = Config('scenarios.yml', 'style.yml')

database = Database(cfg.database)
style = Style(cfg.styles)
report = Report(cfg.title, cfg.date, cfg.logo, cfg.css)

for i in trange(len(cfg.requests), desc='Requests'):
    req = Request.build(cfg.requests[i])

    means = database.means(req, limit=30, min=0.05)
    durations = OrderedDict()

    days = None
    dates = None

    for host in req.hosts:
        for mean_host in means:
            if mean_host != host.name:
                continue

            host_means = []
            for value in means[mean_host]:
                host_means.append(value[1])
            durations[mean_host] = host_means

            if not dates:
                dates = []
                for value in means[mean_host]:
                    dates.append(value[0].split(' ')[0])

            if not days:
                days = len(host_means)

    req.durations = durations

    x_labels = dates

    x_title = '{} days'.format(days)
    graph = Graph(req, style)
    graph.draw_temporal(cfg.imdir, x_title=x_title, x_labels=x_labels, x_label_rotation=45)
    graph.draw_box(cfg.imdir, x_title=x_title)
    report.add(graph)

report.write(cfg.html, cfg.desc)
