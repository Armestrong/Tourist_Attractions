# Generated by Django 3.1.7 on 2021-04-05 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20210405_1606'),
        ('core', '0002_auto_20210405_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristattraction',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='address.addres'),
            preserve_default=False,
        ),
    ]
