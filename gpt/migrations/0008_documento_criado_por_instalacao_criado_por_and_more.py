# Generated by Django 4.0.2 on 2022-02-22 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gpt', '0007_alter_documento_options_alter_instalacao_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='criado_por',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instalacao',
            name='criado_por',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='origem',
            name='criado_por',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]