# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('git', '0004_auto_20170428_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='avatar_url',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='login',
        ),
    ]
