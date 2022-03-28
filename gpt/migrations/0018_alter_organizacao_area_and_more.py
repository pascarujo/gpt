# Generated by Django 4.0.2 on 2022-03-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt', '0017_organizacao_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacao',
            name='area',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='área'),
        ),
        migrations.AlterUniqueTogether(
            name='organizacao',
            unique_together={('nome', 'area')},
        ),
    ]