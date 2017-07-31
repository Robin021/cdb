#!/bin/sh
# Robin021
# Used to pull code from github

#改目录权限以方便jenkins可以运行git 命令
chown -R jenkins: /opt/cdb/
cd /opt/cdb/
git pull
