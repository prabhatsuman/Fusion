# Generated by Django 3.1.5 on 2024-04-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='medical_relief',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='medical_files/')),
                ('file_id', models.IntegerField(default=0)),
                ('compounder_forward_flag', models.BooleanField(default=False)),
                ('acc_admin_forward_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='file_id',
            field=models.IntegerField(default=0),
        ),
    ]
