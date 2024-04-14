# Generated by Django 3.1.5 on 2024-04-14 19:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leave', '0001_initial'),
        ('globals', '0001_initial'),
        ('academic_information', '0001_initial'),
        ('filetracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('budget_type', models.CharField(max_length=20)),
                ('club_type', models.CharField(choices=[('TECHNICAL', 'technical'), ('CULTURAL', 'cultural'), ('SPORTS', 'sports')], default='', max_length=20)),
                ('budget_allocated', models.PositiveIntegerField(default=0)),
                ('budget_expenditure', models.PositiveIntegerField(default=0)),
                ('budget_available', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='hostel_allotment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('program', models.CharField(choices=[('BTECH', 'btech'), ('BDES', 'bdes'), ('MTECH', 'mtech'), ('MDES', 'mdes'), ('PHD', 'phd')], default='', max_length=30)),
                ('year', models.IntegerField(default=2016)),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], default='', max_length=10)),
                ('hall_no', models.CharField(choices=[('HALL-1-BOYS', 'hall-1-boys'), ('HALL-1-GIRLS', 'hall-1-girls'), ('HALL-3', 'hall-3'), ('HALL-4', 'hall-4')], default='', max_length=15)),
                ('number_students', models.PositiveIntegerField(default=0)),
                ('remark', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'hostel_allotment',
            },
        ),
        migrations.CreateModel(
            name='hostel_capacity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('HALL-1-BOYS', 'hall-1-boys'), ('HALL-1-GIRLS', 'hall-1-girls'), ('HALL-3', 'hall-3'), ('HALL-4', 'hall-4')], default='', max_length=15)),
                ('current_capacity', models.PositiveIntegerField(default=0)),
                ('total_capacity', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'hostel_capacity',
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.CharField(max_length=10)),
                ('lab_instructor', models.CharField(max_length=30)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], default='Monday', max_length=10)),
                ('s_time', models.CharField(default='0:00', max_length=6)),
                ('e_time', models.CharField(default='0:00', max_length=6)),
            ],
            options={
                'db_table': 'Lab',
            },
        ),
        migrations.CreateModel(
            name='quotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation1', models.FileField(upload_to='')),
                ('quotation2', models.FileField(upload_to='')),
                ('quotation3', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'quotations',
            },
        ),
        migrations.CreateModel(
            name='Registrar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('purpose', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('0', 'unseen'), ('1', 'seen')], default=0, max_length=1)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='registrar_create_doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='registrar_director_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('purpose', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('0', 'unseen'), ('1', 'seen')], default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='registrar_establishment_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=50)),
                ('person_mail_id', models.CharField(default='xyz', max_length=50)),
                ('date', models.DateField()),
                ('duration', models.IntegerField()),
                ('post', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='registrar_finance_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('purpose', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[('0', 'unseen'), ('1', 'seen')])),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='registrar_purchase_sales_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('member1', models.CharField(max_length=50)),
                ('member2', models.CharField(max_length=50)),
                ('member3', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('purpose', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[('0', 'unseen'), ('1', 'seen')], default=0)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default='0')),
                ('item_type', models.IntegerField(choices=[('0', 'Non-consumable'), ('1', 'Consumable')], default='0')),
            ],
            options={
                'db_table': 'stock',
            },
        ),
        migrations.CreateModel(
            name='Teaching_credits1',
            fields=[
                ('roll_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('course1', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='NO', max_length=100)),
                ('course2', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='NO', max_length=100)),
                ('course3', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='NO', max_length=100)),
                ('tag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Teaching_credits1',
            },
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=100)),
                ('vendor_address', models.CharField(max_length=200)),
                ('vendor_item', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
        migrations.CreateModel(
            name='TA_assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=2)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_module.lab')),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TA_id', to='globals.extrainfo')),
            ],
            options={
                'db_table': 'TA_assign',
            },
        ),
        migrations.CreateModel(
            name='Requisitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('civil', 'civil'), ('electrical', 'electrical')], max_length=50)),
                ('building', models.CharField(choices=[('corelab', 'corelab'), ('computer center', 'computer center'), ('hostel', 'hostel'), ('mess', 'mess'), ('library', 'library'), ('cc', 'cc')], max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('tag', models.IntegerField(default=0)),
                ('assign_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filetracking.file')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Registrar_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=20)),
                ('track_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_id', to='filetracking.tracking')),
            ],
            options={
                'db_table': 'Registrar_response',
            },
        ),
        migrations.CreateModel(
            name='registrar_general_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('status', models.IntegerField(choices=[('0', 'unseen'), ('1', 'seen')], default=0)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_module.registrar_create_doc')),
            ],
        ),
        migrations.CreateModel(
            name='Registrar_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[('0', 'unseen'), ('1', 'seen')], default=0)),
                ('approval', models.IntegerField(choices=[('0', 'reject'), ('1', 'accept')], default=0)),
                ('section_name', models.CharField(max_length=50)),
                ('section_type', models.CharField(max_length=20)),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filetracking.tracking')),
            ],
        ),
        migrations.CreateModel(
            name='purchase_commitee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve_mem1', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('-1', 'Rejected')], default='0')),
                ('approve_mem2', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('-1', 'Rejected')], default='0')),
                ('approve_mem3', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('-1', 'Rejected')], default='0')),
                ('local_comm_mem1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_comm_mem1', to='globals.extrainfo')),
                ('local_comm_mem2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_comm_mem2', to='globals.extrainfo')),
                ('local_comm_mem3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_comm_mem3', to='globals.extrainfo')),
            ],
            options={
                'db_table': 'purchase_commitee',
            },
        ),
        migrations.CreateModel(
            name='Project_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('sponsored_agency', models.CharField(max_length=100)),
                ('CO_PI', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('duration', models.IntegerField(default=0)),
                ('agreement', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='NO', max_length=20)),
                ('amount_sanctioned', models.IntegerField(default=0)),
                ('project_type', models.CharField(choices=[('SRes', 'Sponsored Research'), ('Consultancy', 'Consultancy'), ('fig', 'Faculty Initiation Grant'), ('Testing', 'Testing')], max_length=25)),
                ('project_operated', models.CharField(choices=[('PI', 'Only by PI'), ('any', 'Either PI or CO-PI')], default='me', max_length=50)),
                ('remarks', models.CharField(max_length=200)),
                ('fund_recieved_date', models.DateField(blank=True, null=True)),
                ('HOD_response', models.CharField(choices=[('Forwarded', 'Forwarded'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('DRSPC_response', models.CharField(choices=[('Approve', 'Approve'), ('Disapprove', 'Disapprove'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('applied_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('PI_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Reallocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('previous_budget_head', models.CharField(max_length=300)),
                ('previous_amount', models.IntegerField(default=0)),
                ('pf_no', models.CharField(max_length=100, null=True)),
                ('new_budget_head', models.CharField(max_length=300)),
                ('new_amount', models.IntegerField(default=0)),
                ('transfer_reason', models.CharField(max_length=300)),
                ('HOD_response', models.CharField(choices=[('Forwarded', 'Forwarded'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('DRSPC_response', models.CharField(choices=[('Approve', 'Approve'), ('Disapprove', 'Disapprove'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_module.project_registration')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Extension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('extended_duration', models.IntegerField(default=0)),
                ('extension_details', models.CharField(max_length=300)),
                ('HOD_response', models.CharField(choices=[('Forwarded', 'Forwarded'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('DRSPC_response', models.CharField(choices=[('Approve', 'Approve'), ('Disapprove', 'Disapprove'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('file', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_module.project_registration')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Closure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('expenses_dues', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='Pending', max_length=20)),
                ('expenses_dues_description', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_dues', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='Pending', max_length=20)),
                ('payment_dues_description', models.CharField(blank=True, max_length=200, null=True)),
                ('salary_dues', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='Pending', max_length=20)),
                ('salary_dues_description', models.CharField(blank=True, max_length=200, null=True)),
                ('advances_dues', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='Pending', max_length=20)),
                ('advances_description', models.CharField(blank=True, max_length=200, null=True)),
                ('others_dues', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='Pending', max_length=20)),
                ('other_dues_description', models.CharField(blank=True, max_length=200, null=True)),
                ('overhead_deducted', models.CharField(choices=[('Computer Graphics', 'Computer Graphics'), ('Machine Learning', 'Machine Learning'), ('Image Processing', 'Image Processing'), ('Data Structure', 'Data Structure')], default='Pending', max_length=20)),
                ('overhead_description', models.CharField(blank=True, max_length=200, null=True)),
                ('HOD_response', models.CharField(choices=[('Forwarded', 'Forwarded'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('DRSPC_response', models.CharField(choices=[('Approve', 'Approve'), ('Disapprove', 'Disapprove'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('remarks', models.CharField(max_length=300, null=True)),
                ('extended_duration', models.CharField(default='0', max_length=100, null=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_module.project_registration')),
            ],
        ),
        migrations.CreateModel(
            name='LTC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateField()),
                ('travel_mode', models.CharField(choices=[('road', 'ROAD'), ('rail', 'RAIL')], default='ROAD', max_length=10)),
                ('advance', models.IntegerField(default=0)),
                ('family_details', models.TextField(max_length=500)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.departmentinfo')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.designation')),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.leave')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'LTC',
            },
        ),
        migrations.CreateModel(
            name='hostel_guestroom_approval',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hall_no', models.CharField(choices=[('HALL-1-BOYS', 'hall-1-boys'), ('HALL-1-GIRLS', 'hall-1-girls'), ('HALL-3', 'hall-3'), ('HALL-4', 'hall-4')], default='', max_length=16)),
                ('arrival_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('APPROVED', 'Approved'), ('PENDING', 'Pending')], default='Pending', max_length=20)),
                ('intender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Filemovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(max_length=200, null=True)),
                ('actionby_receiver', models.CharField(choices=[('forward', 'forwarded'), ('revert', 'revert'), ('accept', 'accept'), ('reject', 'reject')], max_length=50)),
                ('receivedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_by', to='globals.holdsdesignation')),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_module.requisitions')),
                ('sentby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_by', to='globals.holdsdesignation')),
            ],
        ),
        migrations.CreateModel(
            name='DeanS_approve_committes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('description', models.CharField(max_length=200)),
                ('convener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convener', to='globals.extrainfo')),
                ('faculty_incharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultyincharge', to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='CPDA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PF_no', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('amoutn', models.IntegerField(default=0)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.designation')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'CPDA',
            },
        ),
        migrations.CreateModel(
            name='Auto_fair_claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=100)),
                ('amount', models.IntegerField(default=0)),
                ('auto_reg_no', models.CharField(max_length=50)),
                ('auto_contact', models.IntegerField(default=0)),
                ('bill', models.FileField(upload_to='hod/')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'auto_fair_claim',
            },
        ),
        migrations.CreateModel(
            name='Assigned_Teaching_credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_course', models.CharField(default='NO', max_length=100)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_module.teaching_credits1')),
            ],
            options={
                'db_table': 'Assigned_Teaching_credits',
            },
        ),
        migrations.CreateModel(
            name='apply_for_purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspecting_authority', models.CharField(default='0', max_length=200)),
                ('expected_purchase_date', models.DateField()),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('purchase_status', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('2', 'Items Ordered'), ('3', 'Items Puchased'), ('4', 'Items Delivered')], default=0)),
                ('amount', models.IntegerField(default='0')),
                ('purchase_date', models.DateField(default='2018-06-01')),
                ('registrar_approve_tag', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('-1', 'Rejected')], default=0)),
                ('director_approve_tag', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('-1', 'Rejected')], default=0)),
                ('HOD_approve_tag', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('-1', 'Rejected')], default=0)),
                ('accounts_approve_tag', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('-1', 'Rejected')], default=0)),
                ('gem_tag', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Approve'), ('-1', 'Rejected')], default=0)),
                ('purchase_type', models.IntegerField(choices=[('0', 'Amount < 25000'), ('1', '25000<Amount<250000'), ('2', '250000<Amount < 2500000'), ('3', 'Amount>2500000')], default=0)),
                ('purpose', models.CharField(default=0, max_length=200)),
                ('budgetary_head', models.CharField(default=0, max_length=200)),
                ('invoice', models.FileField(default=0, upload_to='')),
                ('nature_of_item1', models.IntegerField(choices=[('0', 'Non-consumable'), ('1', 'Consumable')], default=0)),
                ('nature_of_item2', models.IntegerField(choices=[('0', 'Equipment'), ('1', 'Machinery'), ('2', 'Furniture'), ('3', 'Fixture')], default=0)),
                ('item_name', models.CharField(default=0, max_length=100)),
                ('expected_cost', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('indentor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indentor_name', to='globals.extrainfo')),
            ],
            options={
                'db_table': 'apply_for_purchase',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.meeting')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.faculty')),
            ],
            options={
                'db_table': 'Member',
                'unique_together': {('member_id', 'meeting_id')},
            },
        ),
        migrations.CreateModel(
            name='Assistantship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('action', models.IntegerField(default=0)),
                ('comments', models.CharField(blank=True, max_length=150, null=True)),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.curriculum_instructor')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'db_table': 'Assistantship',
                'unique_together': {('student_id', 'instructor_id')},
            },
        ),
    ]
