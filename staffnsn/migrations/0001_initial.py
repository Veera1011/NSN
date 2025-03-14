# Generated by Django 5.1.6 on 2025-03-08 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendancePercentage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.BigIntegerField()),
                ('Semester', models.IntegerField()),
                ('Course_Code', models.TextField(blank=True, null=True)),
                ('Attendance_Percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentsAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.BigIntegerField()),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2)),
                ('staff_name', models.TextField()),
                ('Course_Code', models.TextField()),
                ('Course_Name', models.CharField(max_length=100)),
                ('Date_Attended', models.DateField()),
                ('From_Time', models.TimeField()),
                ('To_Time', models.TimeField()),
                ('No_of_Hours', models.SmallIntegerField()),
                ('Is_Present', models.BooleanField(default=False)),
            ],
        ),
    ]
