# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highscore',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Date published'),
        ),
    ]
