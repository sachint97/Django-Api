# Generated by Django 4.1.1 on 2022-09-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_college_alter_student_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='slug',
            field=models.SlugField(editable=False, max_length=250, null=True),
        ),
    ]
