# Generated by Django 3.2.3 on 2021-08-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subuserplace',
            name='owner_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='tempuser',
            name='owner_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]