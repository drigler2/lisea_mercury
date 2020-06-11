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
from builtins import Exception
import logging

from django.core.exceptions import ValidationError
from django.db import models
from django.forms import Textarea

from lisea_mercury.core.models import DbConnection
from lisea_mercury.zookeeper.kazoo import KazooService


logger = logging.getLogger("django")


class User(models.Model):
    selectAllUsers = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    selectUserByUsername = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    insertUser = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    insertUserAndEnable = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    enableUser = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    disableUser = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    updatePassword = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    updatePasswordAndEnabled = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    countUsersWithUsername = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    def clean(self):
        if User.objects.exists() and not self.pk:
            raise ValidationError("Only one instance allowed!")

        try:
            service = KazooService("/lisea/juno/user")

            service.createOrUpdate("/selectAllUsers", self.selectAllUsers)
            service.createOrUpdate(
                "/selectUserByUsername", self.selectUserByUsername)
            service.createOrUpdate("/insertUser", self.insertUser)
            service.createOrUpdate(
                "/insertUserAndEnable", self.insertUserAndEnable)
            service.createOrUpdate("/enableUser", self.enableUser)
            service.createOrUpdate("/disableUser", self.disableUser)
            service.createOrUpdate("/updatePassword", self.updatePassword)
            service.createOrUpdate(
                "/updatePasswordAndEnabled", self.updatePasswordAndEnabled)
            service.createOrUpdate(
                "/countUsersWithUsername", self.countUsersWithUsername)

        except Exception as e:
            logger.error(e)
            raise ValidationError(
                "Error while updating zookeeper, reason: " + e.__str__())

#
# class UserFields(models.Model):
#     table = models.ForeignKey(
#             to=User,
#             on_delete=models.CASCADE,
#             null=False,
#             blank=False
#         )
#     field = models.CharField(
#             max_length=200,
#             null=False,
#             blank=False
#         )
#
#     def clean(self):
#         allFields = ";".join(list(UserFields.objects.all().values_list('field', flat=True)))
#
#         try:
#             service = KazooService("/lisea/juno/user")
#
#             service.createOrUpdate("/fields", allFields)
#
#         except Exception as e:
#             logger.error(e)
#             raise ValidationError("Error while updating zookeeper, underlying cause: " + e.__str__())
#
#     def __str__(self):
#         return self.field


class Authority(models.Model):

    selectAllAuthorities = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    selectAuthorityByName = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    countAuthorityWithName = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    updateUserAuthorityByUserAndName = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    insertUserAuthorityByUserAndName = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    def clean(self):

        if Authority.objects.exists() and not self.pk:
            raise ValidationError("Only one instance allowed!")

        try:
            service = KazooService("/lisea/juno/authority")

            service.createOrUpdate(
                "/selectAllAuthorities", self.selectAllAuthorities)
            service.createOrUpdate(
                "/selectAuthorityByName", self.selectAuthorityByName)
            service.createOrUpdate(
                "/countAuthorityWithName", self.countAuthorityWithName)
            service.createOrUpdate(
                "/updateUserAuthorityByUserAndName", self.updateUserAuthorityByUserAndName)
            service.createOrUpdate(
                "/insertUserAuthorityByUserAndName", self.insertUserAuthorityByUserAndName)

        except Exception as e:
            logger.error(e)
            raise ValidationError(
                "Error while updating zookeeper, underlying cause: " + e.__str__())

# class AuthorityFields(models.Model):
#     table = models.ForeignKey(
#             to=Authority,
#             on_delete=models.CASCADE,
#             null=False,
#             blank=False
#         )
#     field = models.CharField(
#             max_length=200,
#             null=False,
#             blank=False
#         )
#
#     def clean(self):
#         allFields = ";".join(list(AuthorityFields.objects.all().values_list('field', flat=True)))
#
#         try:
#             service = KazooService("/lisea/juno/authority")
#
#             service.createOrUpdate("/fields", allFields)
#
#         except Exception as e:
#             logger.error(e)
#             raise ValidationError("Error while updating zookeeper, underlying cause: " + e.__str__())
#
#     def __str__(self):
#         return self.field


class ConnectionInfo(DbConnection):

    def clean(self):

        if ConnectionInfo.objects.exists() and not self.pk:
            raise ValidationError("Only one instance allowed!")

        try:
            service = KazooService("/lisea/juno/config")

            service.createOrUpdate("/db_url", self.db_url)
            service.createOrUpdate("/db_username", self.db_username)
            service.createOrUpdate("/db_password", self.db_password)
            service.createOrUpdate("/db_poolSize", self.db_poolSize)
            service.createOrUpdate(
                "/db_connectionTimeout", self.db_connectionTimeout)

        except Exception as e:
            logger.error(e)
            raise ValidationError(
                "Error while updating zookeeper, underlying cause: " + e.__str__())
