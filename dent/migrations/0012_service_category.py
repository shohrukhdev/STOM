# Generated by Django 3.2.11 on 2022-04-17 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dent', '0011_service_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='service_category', to='dent.service_category'),
            preserve_default=False,
        ),
    ]
