# Generated by Django 5.0.2 on 2024-02-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_resultado_examen_paciente_resultados_examenes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_examen',
            name='pendiente',
            field=models.BooleanField(default=True),
        ),
    ]
