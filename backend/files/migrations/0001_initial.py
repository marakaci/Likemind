# Generated by Django 2.0.2 on 2018-02-16 11:47

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('audio', models.FileField(upload_to='chat_audios/%y/%m/%d')),
                ('content_type', models.ForeignKey(limit_choices_to=django.db.models.query_utils.Q(django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'PrivateChat'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'EncryptedPrivateChat'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'GroupChat'), _connector='AND'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChatFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to='chat_files/%y/%m/%d')),
                ('content_type', models.ForeignKey(limit_choices_to=django.db.models.query_utils.Q(django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'PrivateChat'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'EncryptedPrivateChat'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'GroupChat'), _connector='AND'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChatImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='chat_images/%y/%m/%d')),
                ('content_type', models.ForeignKey(limit_choices_to=django.db.models.query_utils.Q(django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'PrivateChat'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'EncryptedPrivateChat'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'GroupChat'), _connector='AND'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChatVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('video', models.FileField(upload_to='chat_videos/%y/%m/%d')),
                ('content_type', models.ForeignKey(limit_choices_to=django.db.models.query_utils.Q(django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'PrivateChat'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'EncryptedPrivateChat'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'chat'), ('model', 'GroupChat'), _connector='AND'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
