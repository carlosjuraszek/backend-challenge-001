# Generated by Django 3.0.7 on 2020-07-12 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20200710_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner',
            new_name='author',
        ),
    ]