# Generated by Django 3.2.11 on 2022-01-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SortedDataModel',
            fields=[
                ('day', models.DateTimeField()),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.FloatField()),
            ],
            options={
                'ordering': ['day', 'weight'],
            },
        ),
    ]
