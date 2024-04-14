# Generated by Django 3.1.5 on 2024-04-14 19:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(default=datetime.date.today)),
                ('brief', models.CharField(default='--', max_length=20)),
                ('request_details', models.CharField(max_length=200)),
                ('upload_request', models.FileField(blank=True, upload_to='')),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('remarks', models.CharField(default='--', max_length=300)),
                ('request_receiver', models.CharField(default='--', max_length=30)),
                ('request_maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ann_date', models.DateTimeField(default='04-04-2021')),
                ('message', models.CharField(max_length=200)),
                ('batch', models.CharField(default='Year-1', max_length=40)),
                ('department', models.CharField(default='ALL', max_length=40)),
                ('programme', models.CharField(max_length=10)),
                ('upload_announcement', models.FileField(default=' ', null=True, upload_to='department/upload_announcement')),
                ('maker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
    ]
