# Generated by Django 3.1.7 on 2021-04-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20210405_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addres',
            name='line2',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
