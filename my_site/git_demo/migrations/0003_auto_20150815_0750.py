# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('git_demo', '0002_auto_20150815_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
