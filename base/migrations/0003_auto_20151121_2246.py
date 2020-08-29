# -*- coding: utf-8 -*-


from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151121_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highscore',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='highscore',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 22, 46, 55, 596645, tzinfo=utc), verbose_name=b'Date published', auto_now_add=True),
            preserve_default=False,
        ),
    ]
