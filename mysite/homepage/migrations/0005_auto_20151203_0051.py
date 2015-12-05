# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_preferences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widget',
            name='show_widget',
        ),
        migrations.AddField(
            model_name='widget',
            name='widget_code',
            field=models.CharField(default=datetime.datetime(2015, 12, 3, 6, 51, 19, 903349, tzinfo=utc), max_length=40000),
            preserve_default=False,
        ),
    ]
