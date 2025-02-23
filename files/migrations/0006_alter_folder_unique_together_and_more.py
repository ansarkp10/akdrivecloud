# Generated by Django 5.1.6 on 2025-02-18 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_file_uploaded_at'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfolders', to='files.folder'),
        ),
    ]
