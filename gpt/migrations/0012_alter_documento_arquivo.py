# Generated by Django 4.0.2 on 2022-02-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt', '0011_documento_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='gpt/arq'),
        ),
    ]
