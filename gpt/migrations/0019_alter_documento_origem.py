# Generated by Django 4.0.2 on 2022-03-22 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpt', '0018_alter_organizacao_area_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='origem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentos', to='gpt.organizacao'),
        ),
    ]