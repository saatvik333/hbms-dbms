# Generated by Django 4.0.2 on 2022-02-05 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_hospital_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='name',
            new_name='hospitalname',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='username',
        ),
    ]
