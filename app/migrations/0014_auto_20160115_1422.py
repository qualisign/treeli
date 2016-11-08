# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20160115_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twig',
            old_name='twig_cirlce',
            new_name='twig_circle',
        ),
    ]
