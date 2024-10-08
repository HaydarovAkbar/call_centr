# Generated by Django 5.0.7 on 2024-08-01 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_appeal_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Frequently Asked Question',
                'verbose_name_plural': 'Frequently Asked Questions',
                'db_table': 'faq',
            },
        ),
        migrations.RemoveField(
            model_name='appeal',
            name='done',
        ),
        migrations.AddField(
            model_name='appeal',
            name='faq',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.faq'),
        ),
    ]
