# Generated by Django 3.2.11 on 2022-03-15 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dent', '0003_auto_20220115_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=512)),
                ('mobile_phone', models.CharField(max_length=512)),
                ('phone', models.CharField(blank=True, max_length=512, null=True)),
                ('sex', models.CharField(max_length=1)),
                ('date_birth', models.DateField()),
                ('address', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('state', models.CharField(max_length=1)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('up_on', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_clinic', to='dent.clinic')),
                ('cr_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='patient_crby', to='dent.stuff')),
                ('up_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='patient_upby', to='dent.stuff')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
    ]
