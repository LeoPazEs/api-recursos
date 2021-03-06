# Generated by Django 4.0.4 on 2022-04-20 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recursos.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recursos', '0003_alter_recurso_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurso',
            name='data_alocacao',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='data_desalocacao',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='user',
        ),
        migrations.AddField(
            model_name='recurso',
            name='status',
            field=models.CharField(choices=[('D', 'Disponível'), ('I', 'Indisponível'), ('A', 'Alocado')], default='D', max_length=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Alocacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_alocacao', models.DateField()),
                ('data_devolucao', models.DateField(validators=[recursos.validators.validatar_data_futuro])),
                ('alocador', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to=settings.AUTH_USER_MODEL)),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='recursos.recurso')),
            ],
        ),
    ]
