# Generated by Django 4.1.7 on 2023-04-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
