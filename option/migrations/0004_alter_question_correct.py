# Generated by Django 3.2.6 on 2021-09-14 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0003_question_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.CharField(default='No Answer Chosen', max_length=100, null='Not found'),
        ),
    ]