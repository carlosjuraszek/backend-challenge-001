# Generated by Django 3.0.7 on 2020-07-12 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0004_auto_20200712_1540'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_auto_20200712_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic'),
        ),
    ]
