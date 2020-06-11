# Generated by Django 3.0.6 on 2020-06-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectAllAuthorities', models.TextField(max_length=1000)),
                ('selectAuthorityByName', models.TextField(max_length=1000)),
                ('countAuthorityWithName', models.TextField(max_length=1000)),
                ('updateUserAuthorityByUserAndName', models.TextField(max_length=1000)),
                ('insertUserAuthorityByUserAndName', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_url', models.CharField(max_length=200)),
                ('db_username', models.CharField(max_length=100)),
                ('db_password', models.CharField(max_length=100)),
                ('db_poolSize', models.PositiveIntegerField()),
                ('db_connectionTimeout', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectAllUsers', models.TextField(max_length=1000)),
                ('selectUserByUsername', models.TextField(max_length=1000)),
                ('insertUser', models.TextField(max_length=1000)),
                ('insertUserAndEnable', models.TextField(max_length=1000)),
                ('enableUser', models.TextField(max_length=1000)),
                ('disableUser', models.TextField(max_length=1000)),
                ('updatePassword', models.TextField(max_length=1000)),
                ('updatePasswordAndEnabled', models.TextField(max_length=1000)),
                ('countUsersWithUsername', models.TextField(max_length=1000)),
            ],
        ),
    ]
