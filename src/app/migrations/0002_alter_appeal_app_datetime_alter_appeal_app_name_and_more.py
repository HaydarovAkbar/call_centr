# Generated by Django 5.0.7 on 2024-07-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='app_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='app_name',
            field=models.CharField(blank=True, help_text='Murojaatchi FISH', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
