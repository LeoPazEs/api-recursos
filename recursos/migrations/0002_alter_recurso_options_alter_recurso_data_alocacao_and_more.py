# Generated by Django 4.0.4 on 2022-04-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recurso',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='recurso',
            name='data_alocacao',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='data_desalocacao',
            field=models.DateField(null=True),
        ),
    ]
