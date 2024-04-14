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
    """Deploy static sites to all servers"""
    if os.path.exists(archive_path):
        basename = os.path.basename(archive_path)
        filename = os.path.basename(archive_path).split('.')[0]
        dest_path = f'/data/web_static/releases/{filename}'
        put(f'{archive_path}', '/tmp/')
        sudo(f'rm -rf {dest_path}/')
        run(f'mkdir -p {dest_path}')
        run(f'tar -xzf /tmp/{basename} -C {dest_path}')
        run(f'rm -f /tmp/{basename}')
        run(f'mv {dest_path}/web_static/* {dest_path}')
        run(f'rm -rf {dest_path}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {dest_path}/ /data/web_static/current')
        print('New version deployed!')
        return True
    return False
