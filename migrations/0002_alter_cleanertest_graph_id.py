# Generated by Django 4.2.20 on 2025-04-10 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanertest',
            name='graph_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
