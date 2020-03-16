# Generated by Django 2.2.11 on 2020-03-16 10:54

import django.db.models.deletion
import filer.fields.file
from django.db import migrations, models

import djangocms_mediaplayer.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('filer', '0011_auto_20190418_0137'),
        ('djangocms_mediaplayer', '0002_auto_20200316_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPlayer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_mediaplayer_videoplayer', serialize=False, to='cms.CMSPlugin')),
                ('not_supported_text', models.TextField(default='Your browser does not support video playback.', help_text='Is shown when browser is not supporting audio files', verbose_name='Not Supported Text')),
                ('file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, to='filer.File', validators=[djangocms_mediaplayer.models.validate_video_file], verbose_name='Video File')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
