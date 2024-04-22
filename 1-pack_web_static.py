#!/usr/bin/python3
"""
Create Archive from web_static folder
"""
from fabric.api import *
from datetime import datetime
from os import stat


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
