#!/usr/bin/python3
"""

FAbric script that generates a tgz archive from contents of webstatic
folder of the Airbnb clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """ generates the archive """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("An error occured: {}".format(e))
        return None
