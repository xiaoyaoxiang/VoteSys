# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-25 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0002_auto_20180524_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20, unique=True)),
                ('cAge', models.IntegerField(default=0)),
                ('cDeclaration', models.CharField(max_length=300)),
                ('cVotes', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'candidate',
            },
        ),
        migrations.CreateModel(
            name='ChatRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crName', models.CharField(max_length=20, unique=True)),
                ('crTime', models.DateTimeField(auto_now=True)),
                ('crInfo', models.CharField(max_length=200)),
                ('crTopic', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('crCandidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='VoteApp.Candidate')),
            ],
            options={
                'db_table': 'chatRecord',
            },
        ),
        migrations.CreateModel(
            name='VoteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pType', models.CharField(max_length=20, unique=True)),
                ('pInfo', models.CharField(max_length=200)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'voteType',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatrecord',
            name='crUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='VoteApp.User'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='cPosition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='VoteApp.VoteType'),
        ),
    ]
