# Generated by Django 3.2.7 on 2021-10-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=10)),
                ('phone_number', models.TextField(max_length=10)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
    ]
