# Generated by Django 2.1.5 on 2019-01-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addclientsmodel',
            name='client_phone_num',
            field=models.CharField(max_length=22),
        ),
    ]
