# Generated by Django 3.2.11 on 2022-10-26 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dent', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Procedure_Tooth_State',
            new_name='ProcedureToothState',
        ),
        migrations.RenameModel(
            old_name='Service_Category',
            new_name='ServiceCategory',
        ),
        migrations.RenameModel(
            old_name='Tooth_state',
            new_name='ToothState',
        ),
    ]