# Generated by Django 4.0.4 on 2022-04-20 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0004_remove_recurso_data_alocacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alocacao',
            name='recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, related_name='alocacoes', to='recursos.recurso'),
        ),
    ]
