# Generated by Django 3.2.5 on 2022-07-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220701_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferedServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=200)),
                ('service_description', models.TextField()),
                ('sesrvice_icon', models.TextField()),
            ],
        ),
    ]
