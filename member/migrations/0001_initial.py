# Generated by Django 3.1.6 on 2021-02-08 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('born', models.CharField(max_length=100)),
                ('hp', models.CharField(max_length=100)),
                ('wdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
