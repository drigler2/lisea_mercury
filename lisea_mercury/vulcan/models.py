"""
Copyright (C) 2021 Damir Rigler

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
from builtins import Exception
import logging

from django.core.exceptions import ValidationError
from django.db import models
from django.forms import Textarea

from lisea_mercury.zookeeper.kazoo import KazooService

logger = logging.getLogger("django")


class InstanceInfos(models.Model):

    url = models.CharField(
        max_length=63,
        null=False,
        blank=False
    )

    instanceId = models.IntegerField(
        unique=True,
        blank=False,
        null=False)

    def clean(self):
        try:
            service = KazooService("/lisea/vulcan/instance_infos")

            service.createOrUpdate(
                "/" + str(self.instanceId) + "/", self.url)

        except Exception as e:
            logger.error(e)
            raise ValidationError(
                "Error while updating zookeeper, underlying cause: " + e.__str__())
