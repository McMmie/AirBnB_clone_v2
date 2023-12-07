#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo"""

from fabric.api import local
from datetime import datetime
import tarfile
import os

def do_pack():
    """
    generates an archive file and return the archive path
    if it has been generated correctly"""

    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = ("versions/web_static_{}.tgz".format(time))
    local("mkdir -p versions")
    local(f"tar -cvzf {file_name} web_static")
    if os.path.exists(file_name):
        return file_name
    else:
        return None
