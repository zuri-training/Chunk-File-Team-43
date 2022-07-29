# Generated by Django 4.0.5 on 2022-07-29 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_authentication_chunkedfile_remove_accounts_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='username',
        ),
    ]
