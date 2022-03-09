# Generated by Django 4.0.2 on 2022-02-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt', '0005_alter_documento_criado_em_alter_instalacao_criado_em_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='referencias',
            field=models.ManyToManyField(blank=True, to='gpt.Documento', verbose_name='referências'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='instalacoes',
            field=models.ManyToManyField(blank=True, to='gpt.Instalacao', verbose_name='instalações'),
        ),
    ]