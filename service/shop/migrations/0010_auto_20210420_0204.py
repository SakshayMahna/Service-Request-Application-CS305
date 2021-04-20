# Generated by Django 3.1.7 on 2021-04-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_appointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='purpose',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='remark_from_staff',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='remark_from_user',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]