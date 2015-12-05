# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_notepad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notepad',
            name='tab_data',
            field=models.TextField(blank=True),
        ),
    ]
