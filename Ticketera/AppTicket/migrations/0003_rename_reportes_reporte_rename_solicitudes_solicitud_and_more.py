# Generated by Django 4.1.3 on 2022-12-27 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTicket', '0002_reportes_soluciones_usuarios_solicitudes_asunto_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reportes',
            new_name='Reporte',
        ),
        migrations.RenameModel(
            old_name='Solicitudes',
            new_name='Solicitud',
        ),
        migrations.RenameModel(
            old_name='Soluciones',
            new_name='Solucion',
        ),
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]