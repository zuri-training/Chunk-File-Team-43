# Generated by Django 4.0.5 on 2022-07-30 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_firstname_accounts_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='accounts',
            new_name='chunkit_users',
        ),
    ]