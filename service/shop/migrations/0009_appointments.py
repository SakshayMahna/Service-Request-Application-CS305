# Generated by Django 3.1.7 on 2021-04-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210417_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestid', models.CharField(max_length=50)),
                ('doa', models.DateField()),
                ('purpose', models.CharField(default='', max_length=100)),
                ('remark_from_staff', models.CharField(default='', max_length=200)),
                ('remark_from_user', models.CharField(default='', max_length=200)),
            ],
            options={
                'unique_together': {('requestid', 'doa')},
            },
        ),
    ]
