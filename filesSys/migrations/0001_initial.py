# Generated by Django 3.2.7 on 2021-09-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_filename', models.CharField(max_length=200)),
                ('f_upload_date', models.DateTimeField()),
            ],
        ),
    ]
