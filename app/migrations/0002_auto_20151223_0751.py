# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Leaf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Trunk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Twig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tree',
            name='sorted_twigs',
            field=models.ForeignKey(to='app.Twig'),
        ),
        migrations.AddField(
            model_name='tree',
            name='trunk',
            field=models.OneToOneField(to='app.Trunk'),
        ),
        migrations.AddField(
            model_name='leaf',
            name='twigs',
            field=models.ManyToManyField(to='app.Twig'),
        ),
        migrations.AddField(
            model_name='branch',
            name='trunk',
            field=models.ForeignKey(to='app.Trunk'),
        ),
    ]
