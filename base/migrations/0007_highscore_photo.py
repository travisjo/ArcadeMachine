# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20151122_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='highscore',
            name='photo',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
