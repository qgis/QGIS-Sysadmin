# qgis4

The [qgis4](http://qgis4.qgis.org/) server is dedicated to QGIS Server for:
- Daily reports for OGC tests on WMS 1.3.0 and WFS 1.1.0
- Daily reports for performance tests
- Online instances for OGC certification process
- Demonstration of QWC2 applications

## Deployment

Remote deployment with Ansible:

```
$ cd ansible
$ virtualenv -p /usr/bin/python2 venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ ansible-playbook -i hosts playbook.yml
```
