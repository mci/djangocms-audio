# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import filer.fields.folder
import django.db.models.deletion
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_audio_audiofile', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('text_title', models.CharField(max_length=200, verbose_name='Title', blank=True)),
                ('text_description', models.TextField(verbose_name='Description', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('audio_file', filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='File', to='filer.File', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AudioFolder',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_audio_audiofolder', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, help_text='Is applied to all audio file instances.', verbose_name='Attributes', blank=True)),
                ('audio_folder', filer.fields.folder.FilerFolderField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Folder', to='filer.Folder', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AudioPlayer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_audio_audioplayer', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('template', models.CharField(default=b'default', max_length=50, verbose_name='Template', choices=[(b'default', 'Default')])),
                ('label', models.CharField(max_length=200, verbose_name='Label', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AudioTrack',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_audio_audiotrack', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('kind', models.CharField(max_length=50, verbose_name='Kind', choices=[(b'subtitles', 'Subtitles'), (b'captions', 'Captions'), (b'descriptions', 'Descriptions'), (b'chapters', 'Chapters')])),
                ('srclang', models.CharField(help_text='Examples: "en" or "de" etc.', max_length=10, verbose_name='Source language', blank=True)),
                ('label', models.CharField(max_length=200, verbose_name='Label', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('src', filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Source file', to='filer.File', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
