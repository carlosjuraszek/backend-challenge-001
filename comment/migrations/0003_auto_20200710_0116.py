# Generated by Django 3.0.7 on 2020-07-10 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200708_1637'),
        ('comment', '0002_auto_20200708_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='post.Post'),
        ),
    ]