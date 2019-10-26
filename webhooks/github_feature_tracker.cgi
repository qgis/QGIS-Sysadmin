#!/usr/bin/env python

""" github_feature_tracker.cgi

This scripts is to be run as a cgi on a public server.
By creating a webhook at github for the commits of qgis/QGIS this
script will be called, with the commit data as json (sent by github).

Given this data the script will create an issue in the issue tracker
of qgis/QGIS-Documentation IF the commit message contains 
[FEATURE] OR [NEEDS-DOCS] (both case-insensitive).

There is a special github user created for this (see below).
NOTE: that should have write access to repo because it adds labels too.

"""

import sys
import os
import json
import requests

#ISSUES_REPO = 'rduivenvoorde/temp'
ISSUES_REPO = 'qgis/QGIS-Documentation'
USERNAME = 'qgis-feature-tracker'
# password can be found in qgis.kdb (via PSC members)
PASSWORD = '*******'

# to get the right number for the milestones:
# https://api.github.com/repos/qgis/QGIS-Documentation/milestones
# QGIS 3.0 = 7
# QGIS 3.2 = 9
# QGIS 3.4 = 10
# QGIS 3.6 = 11
# QGIS 3.8 = 12
# QGIS 3.10 = 13
# QGIS 3.16 = 14

def log(msg):
    with open('/tmp/githubhook.log', 'a') as f:
        f.write(unicode(msg) + '\n')

def test():
    data_without_FEATURE = ''' {
    "ref": "refs/heads/master",
    "before": "055ef76a68f1075d989f3a126e155d050842a204",
    "after": "497191bf40cb9fdbbeef986dc4e19da50fe8059b",
    "created": false,
    "deleted": false,
    "forced": false,
    "base_ref": null,
    "compare": "https://github.com/qgis/QGIS/compare/055ef76a68f1...497191bf40cb",
    "commits": [
        {
        "id": "497191bf40cb9fdbbeef986dc4e19da50fe8059b",
        "distinct": true,
        "message": "Transactions: addFeature propagates new feature id",
        "timestamp": "2015-11-27T16:01:40+01:00",
        "url": "https://github.com/qgis/QGIS/commit/497191bf40cb9fdbbeef986dc4e19da50fe8059b",
        "author": {
            "name": "Matthias Kuhn",
            "email": "matthias@opengis.ch",
            "username": "m-kuhn"
        },
        "committer": {
            "name": "Matthias Kuhn",
            "email": "matthias@opengis.ch",
            "username": "m-kuhn"
        },
        "added": [

        ],
        "removed": [

        ],
        "modified": [
            "src/core/qgsvectorlayereditpassthrough.cpp"
        ]
        }
    ],
    "head_commit": {
        "id": "497191bf40cb9fdbbeef986dc4e19da50fe8059b",
        "distinct": true,
        "message": "Transactions: addFeature propagates new feature id",
        "timestamp": "2015-11-27T16:01:40+01:00",
        "url": "https://github.com/qgis/QGIS/commit/497191bf40cb9fdbbeef986dc4e19da50fe8059b",
        "author": {
        "name": "Matthias Kuhn",
        "email": "matthias@opengis.ch",
        "username": "m-kuhn"
        },
        "committer": {
        "name": "Matthias Kuhn",
        "email": "matthias@opengis.ch",
        "username": "m-kuhn"
        },
        "added": [

        ],
        "removed": [

        ],
        "modified": [
        "src/core/qgsvectorlayereditpassthrough.cpp"
        ]
    },
    "repository": {
        "id": 1690480,
        "name": "QGIS",
        "full_name": "qgis/QGIS",
        "owner": {
        "name": "qgis",
        "email": null
        },
        "private": false,
        "html_url": "https://github.com/qgis/QGIS",
        "description": "QGIS is a free, open source, cross platform (lin/win/mac) geographical information system (GIS)",
        "fork": false,
        "url": "https://github.com/qgis/QGIS",
        "forks_url": "https://api.github.com/repos/qgis/QGIS/forks",
        "keys_url": "https://api.github.com/repos/qgis/QGIS/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/qgis/QGIS/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/qgis/QGIS/teams",
        "hooks_url": "https://api.github.com/repos/qgis/QGIS/hooks",
        "issue_events_url": "https://api.github.com/repos/qgis/QGIS/issues/events{/number}",
        "events_url": "https://api.github.com/repos/qgis/QGIS/events",
        "assignees_url": "https://api.github.com/repos/qgis/QGIS/assignees{/user}",
        "branches_url": "https://api.github.com/repos/qgis/QGIS/branches{/branch}",
        "tags_url": "https://api.github.com/repos/qgis/QGIS/tags",
        "blobs_url": "https://api.github.com/repos/qgis/QGIS/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/qgis/QGIS/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/qgis/QGIS/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/qgis/QGIS/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/qgis/QGIS/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/qgis/QGIS/languages",
        "stargazers_url": "https://api.github.com/repos/qgis/QGIS/stargazers",
        "contributors_url": "https://api.github.com/repos/qgis/QGIS/contributors",
        "subscribers_url": "https://api.github.com/repos/qgis/QGIS/subscribers",
        "subscription_url": "https://api.github.com/repos/qgis/QGIS/subscription",
        "commits_url": "https://api.github.com/repos/qgis/QGIS/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/qgis/QGIS/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/qgis/QGIS/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/qgis/QGIS/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/qgis/QGIS/contents/{+path}",
        "compare_url": "https://api.github.com/repos/qgis/QGIS/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/qgis/QGIS/merges",
        "archive_url": "https://api.github.com/repos/qgis/QGIS/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/qgis/QGIS/downloads",
        "issues_url": "https://api.github.com/repos/qgis/QGIS/issues{/number}",
        "pulls_url": "https://api.github.com/repos/qgis/QGIS/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/qgis/QGIS/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/qgis/QGIS/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/qgis/QGIS/labels{/name}",
        "releases_url": "https://api.github.com/repos/qgis/QGIS/releases{/id}",
        "created_at": 1304323586,
        "updated_at": "2015-11-27T10:11:41Z",
        "pushed_at": 1448636512,
        "git_url": "git://github.com/qgis/QGIS.git",
        "ssh_url": "git@github.com:qgis/QGIS.git",
        "clone_url": "https://github.com/qgis/QGIS.git",
        "svn_url": "https://github.com/qgis/QGIS",
        "homepage": "http://qgis.org",
        "size": 1205570,
        "stargazers_count": 805,
        "watchers_count": 805,
        "language": "C++",
        "has_issues": false,
        "has_downloads": true,
        "has_wiki": false,
        "has_pages": false,
        "forks_count": 743,
        "mirror_url": null,
        "open_issues_count": 48,
        "forks": 743,
        "open_issues": 48,
        "watchers": 805,
        "default_branch": "master",
        "stargazers": 805,
        "master_branch": "master",
        "organization": "qgis"
    },
    "pusher": {
        "name": "m-kuhn",
        "email": "matthias@opengis.ch"
    },
    "organization": {
        "login": "qgis",
        "id": 483444,
        "url": "https://api.github.com/orgs/qgis",
        "repos_url": "https://api.github.com/orgs/qgis/repos",
        "events_url": "https://api.github.com/orgs/qgis/events",
        "members_url": "https://api.github.com/orgs/qgis/members{/member}",
        "public_members_url": "https://api.github.com/orgs/qgis/public_members{/member}",
        "avatar_url": "https://avatars.githubusercontent.com/u/483444?v=3",
        "description": null
    },
    "sender": {
        "login": "m-kuhn",
        "id": 588407,
        "avatar_url": "https://avatars.githubusercontent.com/u/588407?v=3",
        "gravatar_id": "",
        "url": "https://api.github.com/users/m-kuhn",
        "html_url": "https://github.com/m-kuhn",
        "followers_url": "https://api.github.com/users/m-kuhn/followers",
        "following_url": "https://api.github.com/users/m-kuhn/following{/other_user}",
        "gists_url": "https://api.github.com/users/m-kuhn/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/m-kuhn/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/m-kuhn/subscriptions",
        "organizations_url": "https://api.github.com/users/m-kuhn/orgs",
        "repos_url": "https://api.github.com/users/m-kuhn/repos",
        "events_url": "https://api.github.com/users/m-kuhn/events{/privacy}",
        "received_events_url": "https://api.github.com/users/m-kuhn/received_events",
        "type": "User",
        "site_admin": false
    },
    "distinct_commits": [
        {
        "id": "497191bf40cb9fdbbeef986dc4e19da50fe8059b",
        "distinct": true,
        "message": "Transactions: addFeature propagates new feature id",
        "timestamp": "2015-11-27T16:01:40+01:00",
        "url": "https://github.com/qgis/QGIS/commit/497191bf40cb9fdbbeef986dc4e19da50fe8059b",
        "author": {
            "name": "Matthias Kuhn",
            "email": "matthias@opengis.ch",
            "username": "m-kuhn"
        },
        "committer": {
            "name": "Matthias Kuhn",
            "email": "matthias@opengis.ch",
            "username": "m-kuhn"
        },
        "added": [

        ],
        "removed": [

        ],
        "modified": [
            "src/core/qgsvectorlayereditpassthrough.cpp"
        ]
        }
    ],
    "ref_name": "master"
    } '''

    data_with_FEATURE = '''{
    "ref": "refs/heads/master",
    "before": "f100e9ae43a26e991a8c01b381a21a8e08b74384",
    "after": "454afaf5d7e3a7c091b8de9341b70bbcde11a703",
    "created": false,
    "deleted": false,
    "forced": false,
    "base_ref": null,
    "compare": "https://github.com/rduivenvoorde/temp/compare/f100e9ae43a2...454afaf5d7e3",
    "commits": [
        {
        "id": "454afaf5d7e3a7c091b8de9341b70bbcde11a703",
        "distinct": true,
        "message": "[FEATURE] Cool new feature",
        "timestamp": "2015-11-28T11:34:40+01:00",
        "url": "https://github.com/rduivenvoorde/temp/commit/454afaf5d7e3a7c091b8de9341b70bbcde11a703",
        "author": {
            "name": "Richard Duivenvoorde",
            "email": "richard@duif.net",
            "username": "rduivenvoorde"
        },
        "committer": {
            "name": "Richard Duivenvoorde",
            "email": "richard@duif.net",
            "username": "rduivenvoorde"
        },
        "added": [

        ],
        "removed": [

        ],
        "modified": [
            "README.md"
        ]
        }
    ],
    "head_commit": {
        "id": "454afaf5d7e3a7c091b8de9341b70bbcde11a703",
        "distinct": true,
        "message": "[FEATURE] Cool new feature",
        "timestamp": "2015-11-28T11:34:40+01:00",
        "url": "https://github.com/rduivenvoorde/temp/commit/454afaf5d7e3a7c091b8de9341b70bbcde11a703",
        "author": {
        "name": "Richard Duivenvoorde",
        "email": "richard@duif.net",
        "username": "rduivenvoorde"
        },
        "committer": {
        "name": "Richard Duivenvoorde",
        "email": "richard@duif.net",
        "username": "rduivenvoorde"
        },
        "added": [

        ],
        "removed": [

        ],
        "modified": [
        "README.md"
        ]
    },
    "repository": {
        "id": 45624871,
        "name": "temp",
        "full_name": "rduivenvoorde/temp",
        "owner": {
        "name": "rduivenvoorde",
        "email": "richard@duif.net"
        },
        "private": false,
        "html_url": "https://github.com/rduivenvoorde/temp",
        "description": "",
        "fork": false,
        "url": "https://github.com/rduivenvoorde/temp",
        "forks_url": "https://api.github.com/repos/rduivenvoorde/temp/forks",
        "keys_url": "https://api.github.com/repos/rduivenvoorde/temp/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/rduivenvoorde/temp/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/rduivenvoorde/temp/teams",
        "hooks_url": "https://api.github.com/repos/rduivenvoorde/temp/hooks",
        "issue_events_url": "https://api.github.com/repos/rduivenvoorde/temp/issues/events{/number}",
        "events_url": "https://api.github.com/repos/rduivenvoorde/temp/events",
        "assignees_url": "https://api.github.com/repos/rduivenvoorde/temp/assignees{/user}",
        "branches_url": "https://api.github.com/repos/rduivenvoorde/temp/branches{/branch}",
        "tags_url": "https://api.github.com/repos/rduivenvoorde/temp/tags",
        "blobs_url": "https://api.github.com/repos/rduivenvoorde/temp/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/rduivenvoorde/temp/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/rduivenvoorde/temp/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/rduivenvoorde/temp/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/rduivenvoorde/temp/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/rduivenvoorde/temp/languages",
        "stargazers_url": "https://api.github.com/repos/rduivenvoorde/temp/stargazers",
        "contributors_url": "https://api.github.com/repos/rduivenvoorde/temp/contributors",
        "subscribers_url": "https://api.github.com/repos/rduivenvoorde/temp/subscribers",
        "subscription_url": "https://api.github.com/repos/rduivenvoorde/temp/subscription",
        "commits_url": "https://api.github.com/repos/rduivenvoorde/temp/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/rduivenvoorde/temp/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/rduivenvoorde/temp/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/rduivenvoorde/temp/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/rduivenvoorde/temp/contents/{+path}",
        "compare_url": "https://api.github.com/repos/rduivenvoorde/temp/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/rduivenvoorde/temp/merges",
        "archive_url": "https://api.github.com/repos/rduivenvoorde/temp/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/rduivenvoorde/temp/downloads",
        "issues_url": "https://api.github.com/repos/rduivenvoorde/temp/issues{/number}",
        "pulls_url": "https://api.github.com/repos/rduivenvoorde/temp/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/rduivenvoorde/temp/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/rduivenvoorde/temp/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/rduivenvoorde/temp/labels{/name}",
        "releases_url": "https://api.github.com/repos/rduivenvoorde/temp/releases{/id}",
        "created_at": 1446741780,
        "updated_at": "2015-11-05T16:43:00Z",
        "pushed_at": 1448706880,
        "git_url": "git://github.com/rduivenvoorde/temp.git",
        "ssh_url": "git@github.com:rduivenvoorde/temp.git",
        "clone_url": "https://github.com/rduivenvoorde/temp.git",
        "svn_url": "https://github.com/rduivenvoorde/temp",
        "homepage": null,
        "size": 0,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": null,
        "has_issues": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": false,
        "forks_count": 0,
        "mirror_url": null,
        "open_issues_count": 12,
        "forks": 0,
        "open_issues": 12,
        "watchers": 0,
        "default_branch": "master",
        "stargazers": 0,
        "master_branch": "master"
    },
    "pusher": {
        "name": "rduivenvoorde",
        "email": "richard@duif.net"
    },
    "sender": {
        "login": "rduivenvoorde",
        "id": 731673,
        "avatar_url": "https://avatars.githubusercontent.com/u/731673?v=3",
        "gravatar_id": "",
        "url": "https://api.github.com/users/rduivenvoorde",
        "html_url": "https://github.com/rduivenvoorde",
        "followers_url": "https://api.github.com/users/rduivenvoorde/followers",
        "following_url": "https://api.github.com/users/rduivenvoorde/following{/other_user}",
        "gists_url": "https://api.github.com/users/rduivenvoorde/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/rduivenvoorde/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/rduivenvoorde/subscriptions",
        "organizations_url": "https://api.github.com/users/rduivenvoorde/orgs",
        "repos_url": "https://api.github.com/users/rduivenvoorde/repos",
        "events_url": "https://api.github.com/users/rduivenvoorde/events{/privacy}",
        "received_events_url": "https://api.github.com/users/rduivenvoorde/received_events",
        "type": "User",
        "site_admin": false
    }
    }'''
    # choose one of this jsons:
    #return data_with_FEATURE
    return data_without_FEATURE

def sent_content(status, msg):
    # http://www.restpatterns.org/HTTP_Status_Codes
    print "Status: %s Success" % status
    print "Content-Type: text/plain"
    print
    print unicode(msg)


# THE ACTUAL CGI

method = os.environ["REQUEST_METHOD"]

try:
    # TO TEST: make method GET and take one of the jsons from test()
    #if method == "GET":
    #    rawdata = test()
    if method == "POST":
        rawdata = sys.stdin.read()
        data = json.loads(rawdata)
        issues_url = 'https://api.github.com/repos/%s/issues' % ISSUES_REPO
        for commit in data['commits']:
            msg = commit['message']
            if '[FEATURE]' in msg.upper() or '[NEEDS-DOCS]' in msg.upper():
                # message is both title and description from the commit, separated by \n\n
                msg = msg.split('\n\n')
                title = msg[0]
                committer = commit['committer']['username']
                desc = 'Unfortunately this naughty coder did not write a description... :-('
                if len(msg)>1:
                    desc = '\n\n'.join(msg[1:])
                body = 'Original commit: %s by %s\n\n%s' % (commit['url'], committer, desc)
                issue_payload = {
                    'title': title,
                    'body': body,
                    'milestone': 14,
                    'labels': ['Automatic new feature', '3.12']
                }
                issue_payload = json.dumps(issue_payload)
                r = requests.post(issues_url, data=issue_payload, auth=(USERNAME, PASSWORD))

        # ok, either handled FEATURE or a commmit without that: return a decent 200
        sent_content(200, 'Ok')
    else:
        sent_content(400, 'Illegal request')

except Exception, error:
    log("ERROR in script")
    log(error)
    sent_content(500, "Some unexpected error occurred. Error text was: %s" % error)
