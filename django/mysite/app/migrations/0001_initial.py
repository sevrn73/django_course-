# Generated by Django 3.1.1 on 2021-10-19 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StableRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=30)),
                ('y', models.CharField(max_length=30)),
            ],
        ),
    ]