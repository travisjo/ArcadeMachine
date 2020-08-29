# -*- coding: utf-8 -*-


from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('year', models.DateField(verbose_name=b'Year released')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date created')),
                ('date_modifed', models.DateTimeField(auto_now=True, verbose_name=b'Date modified')),
            ],
        ),
        migrations.CreateModel(
            name='HighScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('game', models.ForeignKey(to='base.Game')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
