# Generated by Django 4.2.3 on 2023-10-02 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='owner',
        ),
    ]
