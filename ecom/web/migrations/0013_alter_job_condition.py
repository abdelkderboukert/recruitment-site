# Generated by Django 5.0.3 on 2024-03-18 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_condition_job_info_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='condition',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.condition'),
        ),
    ]
