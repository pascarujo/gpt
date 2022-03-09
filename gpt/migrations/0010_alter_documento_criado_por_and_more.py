# Generated by Django 4.0.2 on 2022-02-22 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gpt', '0009_alter_documento_criado_por_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='documentos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documento',
            name='instalacoes',
            field=models.ManyToManyField(blank=True, related_name='documentos', to='gpt.Instalacao', verbose_name='instalações'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='origem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='documentos', to='gpt.origem'),
        ),
    ]
