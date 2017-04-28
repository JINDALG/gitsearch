# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('git', '0003_auto_20170428_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account_created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='public_repos',
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
