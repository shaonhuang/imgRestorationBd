# Generated by Django 3.2.7 on 2021-09-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesSys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='f_upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
