# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20151203_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='banner_text',
            field=models.CharField(default=datetime.datetime(2015, 12, 3, 13, 25, 13, 29575, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
