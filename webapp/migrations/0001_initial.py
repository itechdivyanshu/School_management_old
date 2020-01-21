# Generated by Django 2.2.7 on 2019-12-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('adm_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_join', models.DateField()),
                ('addhar_no', models.IntegerField()),
                ('fathers_name', models.CharField(max_length=50)),
                ('mothers_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('addrress', models.CharField(max_length=50)),
                ('class_in', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
                ('roll_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_join', models.DateField()),
                ('password', models.CharField(max_length=50)),
                ('last_login', models.DateField()),
                ('addhar_no', models.IntegerField()),
                ('fathers_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('img', models.ImageField(upload_to='pics')),
                ('addrress', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('class_teacher_of', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('emp_status', models.CharField(max_length=50)),
                ('e_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher_timetable',
            fields=[
                ('e_id', models.IntegerField(primary_key=True, serialize=False)),
                ('days', models.CharField(max_length=50)),
                ('period_1', models.CharField(max_length=50)),
                ('period_2', models.CharField(max_length=50)),
                ('period_3', models.CharField(max_length=50)),
                ('period_4', models.CharField(max_length=50)),
                ('period_5', models.CharField(max_length=50)),
                ('period_6', models.CharField(max_length=50)),
                ('period_7', models.CharField(max_length=50)),
                ('period_8', models.CharField(max_length=50)),
                ('period_9', models.CharField(max_length=50)),
            ],
        ),
    ]