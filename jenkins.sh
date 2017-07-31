#!/bin/sh
# Robin021
# Used to pull code from github

#
chown -R jenkins: /opt/cdb/
cd /opt/cdb/
git pull
