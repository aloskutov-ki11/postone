# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0', blank=True)),
                ('description', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0', blank=True)),
                ('document', models.FileField(upload_to=b'', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryPhotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GuardGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd1\x8b')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GuardGroupScheduleItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb1\xd1\x8b\xd1\x82\xd0\xb8\xd0\xb5')),
                ('time', models.TimeField(verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0')),
                ('group', models.ForeignKey(verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb0', to='post_app.GuardGroup')),
            ],
            options={
                'verbose_name': '\u0421\u043e\u0431\u044b\u0442\u0438\u0435',
                'verbose_name_plural': '\u0421\u043e\u0431\u044b\u0442\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8')),
                ('pub_date', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('content', models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8')),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsPhotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f')),
                ('news', models.ForeignKey(to='post_app.News')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0434\u043b\u044f \u043d\u043e\u0432\u043e\u0441\u0442\u0438',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0434\u043b\u044f \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=256, verbose_name=b'\xd0\xa4\xd0\x98\xd0\x9e')),
                ('school', models.CharField(max_length=256, verbose_name=b'\xd0\xa8\xd0\xba\xd0\xbe\xd0\xbb\xd0\xb0')),
                ('photo', models.ImageField(upload_to=b'', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f', blank=True)),
                ('group', models.ForeignKey(verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb0', blank=True, to='post_app.GuardGroup', null=True)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0441\u0442\u043e\u0432\u0435\u0446',
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u043e\u0432\u0446\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=256, verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0 \xd1\x80\xd0\xb5\xd1\x81\xd1\x83\xd1\x80\xd1\x81')),
                ('description', models.CharField(max_length=256, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb5\xd1\x81\xd1\x83\xd1\x80\xd1\x81\xd0\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0441\u0443\u0440\u0441',
                'verbose_name_plural': '\u0420\u0435\u0441\u0443\u0440\u0441\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_name', models.CharField(max_length=256, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80')),
                ('pub_date', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('content', models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb3\xd1\x80\xd0\xb0\xd0\xb4\xd1\x8b')),
            ],
            options={
                'verbose_name': '\u041d\u0430\u0433\u0440\u0430\u0434\u0430',
                'verbose_name_plural': '\u041d\u0430\u0433\u0440\u0430\u0434\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('title', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb8\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video_url', models.CharField(max_length=255, verbose_name=b'YouTube-\xd1\x81\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0')),
            ],
            options={
                'verbose_name': 'YouTube-\u0441\u0441\u044b\u043b\u043a\u0430',
                'verbose_name_plural': 'YouTube-\u0441\u0441\u044b\u043b\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='rewards',
            field=models.ManyToManyField(to='post_app.Reward', null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb3\xd1\x80\xd0\xb0\xd0\xb4\xd1\x8b', blank=True),
            preserve_default=True,
        ),
    ]
