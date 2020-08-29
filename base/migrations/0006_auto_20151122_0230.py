# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20151122_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='latitude',
            field=models.DecimalField(default=None, null=True, max_digits=20, decimal_places=18, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='longitude',
            field=models.DecimalField(default=None, null=True, max_digits=21, decimal_places=18, blank=True),
        ),
    ]
