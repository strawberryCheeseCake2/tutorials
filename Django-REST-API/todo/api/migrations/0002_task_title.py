# Generated by Django 3.0.12 on 2021-02-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Fuck You', max_length=200),
        ),
    ]
