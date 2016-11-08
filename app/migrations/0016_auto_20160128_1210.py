# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20160124_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='drawing',
            new_name='stage',
        ),
        migrations.RenameField(
            model_name='leaf',
            old_name='drawing',
            new_name='stage',
        ),
        migrations.RenameField(
            model_name='trunk',
            old_name='drawing',
            new_name='stage',
        ),
        migrations.RenameField(
            model_name='twig',
            old_name='drawing',
            new_name='stage',
        ),
        migrations.AlterField(
            model_name='branch',
            name='base_x',
            field=models.IntegerField(default=320),
        ),
        migrations.AlterField(
            model_name='branch',
            name='base_y',
            field=models.IntegerField(default=440),
        ),
        migrations.AddField(
            model_name='drawing',
            name='trunk',
            field=models.OneToOneField(to='app.Trunk'),
        ),
    ]
