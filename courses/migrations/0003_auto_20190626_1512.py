# Generated by Django 2.2.2 on 2019-06-26 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_studetns'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='studetns',
            new_name='students',
        ),
    ]
