# Generated by Django 4.1.4 on 2023-01-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_delete_upload_file_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_file_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=' ', null=True)),
                ('file_name', models.CharField(default=' ', max_length=50, null=True)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]
