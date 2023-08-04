# Generated by Django 4.2.4 on 2023-08-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NamusaviGarage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(default=1)),
                ('make', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=9)),
                ('chasis', models.IntegerField()),
                ('damage', models.CharField(max_length=30)),
                ('insuarance', models.CharField(max_length=30)),
            ],
        ),
    ]