"""
Copyright (C) 2020 Damir Rigler

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; version 2 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
from django.conf import settings
from kazoo.client import KazooClient

from .models import Zookeeper


class KazooService():

    zk = None
    rootPath = None

    def __init__(self, rootPath):

        qs = Zookeeper.objects.filter().first()
        if qs is None:
            raise LookupError("Unable to find Zookeeper configuration!")

        self.zk = KazooClient(hosts=qs.url)
        self.rootPath = rootPath

        self.zk.start(timeout=qs.timeout)
        self.zk.ensure_path(rootPath)

    def createOrUpdate(self, pathAffix, nodeValue):

        if isinstance(nodeValue, str):
            bValue = bytes(nodeValue, 'utf-8')
        else:
            bValue = bytes(str(nodeValue), 'utf-8')

        path = self.rootPath + pathAffix

        if self.zk.exists(path) is None:
            self.zk.create(path, bValue)
        else:
            self.zk.set(path, bValue)

    def __del__(self):

        if self.zk is not None:
            self.zk.stop()
