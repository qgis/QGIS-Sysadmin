#!/usr/bin/env python

""" github_feature_tracker.cgi

This scripts is to be run as a cgi on a public server.
By creating a webhook at github for the commits of qgis/QGIS this
script will be called, with the commit data as json (sent by github).

Given this data the script will create an issue in the issue tracker
of qgis/QGIS-Documentation IF the commit message contains [FEATURE].

There is a special github user created for this (see below).
NOTE: that should have write access to repo because it adds labels too.

"""

import sys
import os
import json
import requests

method = os.environ["REQUEST_METHOD"]

#ISSUES_REPO = 'rduivenvoorde/temp'
ISSUES_REPO = 'qgis/QGIS-Documentation'
USERNAME = 'qgis-feature-tracker'
# password can be found in qgis.kdb (via PSC members)
PASSWORD = '*******'

def log(msg):
    with open('/tmp/githubhook.log', 'a') as f:
        f.write(unicode(msg) + '\n')

try:
    if method == "POST":
        rawdata = sys.stdin.read()
        data = json.loads(rawdata)
        issues_url = 'https://api.github.com/repos/%s/issues' % ISSUES_REPO
        for commit in data['commits']:
            msg = commit['message']
            if '[FEATURE]' in msg:
                # message is both title and description from the commit, separated by \n\n
                msg = msg.split('\n\n')
                title = msg[0]
                committer = commit['committer']['username']
                desc = 'Unfortunately this lazy coder did not write a description... :-('
                if len(msg)>1:
                    desc = '\n\n'.join(msg[1:])
                body = 'Original commit: %s by %s\n\n%s' % (commit['url'], committer, desc)
                issue_payload = {
                    'title': title,
                    'body': body,
                    'labels': ['Automatic new feature']
                }
                issue_payload = json.dumps(issue_payload)
                r = requests.post(issues_url, data=issue_payload, auth=(USERNAME, PASSWORD))
    else:
        print "Content-Type: text/plain"
        print
        print "Illegal request."

except Exception, E:
    log("ERROR in script")
    log(E)
    print "Status: 500 Unexpected Error"
    print "Content-Type: text/plain"
    print 
    print "Some unexpected error occurred. Error text was:", E
