# Generated by Django 5.0.7 on 2024-07-19 12:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('app_name', models.CharField(help_text='Murojaatchi FISH', max_length=255)),
                ('phone_number', models.CharField(blank=True, help_text='Phone number', max_length=255, null=True)),
                ('app_datetime', models.DateTimeField()),
                ('result', models.CharField(blank=True, max_length=255, null=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('text', models.TextField()),
                ('voice', models.FileField(blank=True, null=True, upload_to='appeals/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Appeal',
                'verbose_name_plural': 'Appeals',
                'db_table': 'appeals',
                'indexes': [models.Index(fields=['user'], name='appeals_user_id_1bd8ef_idx'), models.Index(fields=['is_resolved'], name='appeals_is_reso_80f56b_idx')],
            },
        ),
    ]
