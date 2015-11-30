# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20151122_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='date_modifed',
            new_name='date_modified',
        ),
        migrations.AlterField(
            model_name='highscore',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date created'),
        ),
    ]
