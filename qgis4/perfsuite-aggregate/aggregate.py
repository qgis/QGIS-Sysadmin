from tqdm import trange

from graffiti.graffiti.request import Request
from graffiti.graffiti.graph import Graph
from graffiti.graffiti.report import Report
from graffiti.graffiti.config import Config
from graffiti.graffiti.database import Database

cfg = Config('scenarios.yml')

database = Database(cfg.database)

report = Report(cfg.title, cfg.date, cfg.logo)

for i in trange(len(cfg.requests), desc='Requests'):
    req = Request.build(cfg.requests[i])

    means = database.means(req, limit=30, min=0.05)
    durations = {}

    days = None
    dates = None
    for host in means:
        host_means = []
        for value in means[host]:
            host_means.append(value[1])
        durations[host] = host_means

        if not dates:
            dates = []
            for value in means[host]:
                dates.append(value[0].split(' ')[0])

        if not days:
            days = len(host_means)

    req.durations = durations

    x_labels = dates

    x_title = '{} days'.format(days)
    graph = Graph(req)
    graph.draw_temporal(cfg.imdir, x_title=x_title, x_labels=x_labels, x_label_rotation=45)
    graph.draw_box(cfg.imdir, x_title=x_title)
    report.add(graph)

report.write(cfg.html, cfg.desc)
