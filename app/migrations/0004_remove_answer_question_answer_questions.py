# Generated by Django 4.0.4 on 2022-05-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_likequestion_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ManyToManyField(to='app.question'),
        ),
    ]