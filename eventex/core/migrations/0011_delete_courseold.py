# Generated by Django 4.1.2 on 2022-11-03 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course_abc_to_mti'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]