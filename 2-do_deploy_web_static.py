#!/usr/bin/python3
"""
Create Archive from web_static folder
"""
from fabric.api import *
from datetime import datetime
from os import stat
import os

env.hosts = [
    '54.237.104.154',
    '18.206.206.79'
]

env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Creates a new archive for all web_static files"""
    new_date = datetime.now()
    year = new_date.year
    month = new_date.month
    day = new_date.day
    hour = new_date.hour
    minute = new_date.minute
    second = new_date.second
    dt_string = f'{year}{month}{day}{hour}{minute}{second}'
    local('mkdir -p versions')
    archive_path = (f'versions/web_static_{dt_string}.tgz')
    try:
        print(f'Packing web_static to {archive_path}')
        local(f'tar -cvzf {archive_path} web_static')
        file_size = stat(archive_path)
        print(f'web_static packed: {archive_path} -> {file_size.st_size}')
    except Exception:
        return None


def do_deploy(archive_path):
    """ method doc
        fab -f 2-do_deploy_web_static.py do_deploy:
        archive_path=versions/web_static_20231004201306.tgz
        -i ~/.ssh/id_rsa -u ubuntu
    """
    try:
        if not os.path.exists(archive_path):
            return False
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, fn_no_ext))
        run("mkdir -p {}{}/".format(dpath, fn_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
        run("rm /tmp/{}".format(fn_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
        run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
