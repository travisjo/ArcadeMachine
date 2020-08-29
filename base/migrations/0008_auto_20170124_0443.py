# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_highscore_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='year',
        ),
        migrations.AddField(
            model_name='game',
            name='aliases',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='game',
            name='giantbomb_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.DateField(null=True, verbose_name=b'Year released'),
        ),
    ]
