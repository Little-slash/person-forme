# Generated by Django 4.2.7 on 2023-11-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_edu_index', models.CharField(max_length=20)),
                ('my_edu_name', models.CharField(max_length=100)),
                ('my_edu_major', models.CharField(max_length=100)),
                ('my_edu_degree', models.CharField(max_length=100)),
            ],
        ),
    ]