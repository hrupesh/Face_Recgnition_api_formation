# Generated by Django 2.2.3 on 2019-07-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_auto_20190726_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]