#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo"""

from fabric.api import *
from datetime import datetime
import tarfile
import os

env.hosts = ['54.237.38.25', '100.25.152.122']


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


def do_deploy(archive_path):
    """
    distributes an archive to your web servers, using the function
    """

    file_name = archive_path.split('/')
    file_name = file_name[-1].split(".")
    new_file = file_name[0]

    if os.path.exists(archive_path):
        put("{}".format(archive_path), '/tmp/')
        run("mkdir -p /data/web_static/releases/{}".format(new_file))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format
            (new_file, new_file))
        run("rm /tmp/{}.tgz".format(new_file))
        run("rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}\
                /data/web_static/current".format(new_file))

        return True
    else:

        return False
