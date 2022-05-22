# Generated by Django 4.0.4 on 2022-05-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_likeanswer_mark_d_alter_likeanswer_mark_l_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likequestion',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='likequestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='answer',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='LikeAnswer',
        ),
        migrations.DeleteModel(
            name='LikeQuestion',
        ),
    ]