# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151121_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='latitude',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='longitude',
            field=models.DecimalField(default=0, max_digits=21, decimal_places=18),
            preserve_default=False,
        ),
    ]
