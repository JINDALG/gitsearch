# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('username', models.CharField(unique=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('followers_url', models.URLField()),
                ('organizations_url', models.URLField()),
                ('repos_url', models.URLField()),
                ('company', models.CharField(max_length=50, null=True, blank=True)),
                ('blog', models.CharField(max_length=50, null=True, blank=True)),
                ('location', models.CharField(max_length=50, null=True, blank=True)),
                ('public_repos', models.IntegerField(default=0)),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('account_created', models.DateField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
    ]
