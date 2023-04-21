# Generated by Django 3.2.3 on 2021-06-30 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_email', models.EmailField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
