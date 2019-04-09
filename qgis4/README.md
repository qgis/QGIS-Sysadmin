# qgis4

The [qgis4](http://qgis4.qgis.org/) server is dedicated to QGIS Server for:
- Daily reports for OGC tests on WMS 1.3.0 and WFS 1.1.0
- Daily reports for performance tests
- Online instances for OGC certification process
- Demonstration of QWC2 applications

## Deployment

To deploy this project on a remote server, you have to:
- configure your SSH to have a root connection without password (ssh key)
- create an alias in your `~/.ssh/config` for the host `qgis4` (for
  the `root` user or a sudo user)
- execute the Ansible playbook for the virtualenv (see below)

```
$ cd ansible
$ virtualenv -p /usr/bin/python2 venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ sh qgis4.sh
```

## URLs

Links:
- [QWC2 demos](http://qgis4.qgis.org:8081/demos_qwc2/)
