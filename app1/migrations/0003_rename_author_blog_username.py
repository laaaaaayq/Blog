# Generated by Django 4.2.6 on 2023-11-14 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_register_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='username',
        ),
    ]
