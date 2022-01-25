# Generated by Django 3.2.11 on 2022-01-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AggregateDataModel',
            fields=[
                ('day', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.FloatField()),
                ('unit', models.CharField(default='kg', max_length=32)),
            ],
            options={
                'ordering': ['day', 'weight'],
            },
        ),
    ]