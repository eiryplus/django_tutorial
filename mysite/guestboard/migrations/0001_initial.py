# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(help_text='あなたの名前を入力してください', max_length=64, verbose_name='名前')),
                ('message', models.CharField(help_text='メッセージを入力してください', max_length=255, verbose_name='メッセージ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
