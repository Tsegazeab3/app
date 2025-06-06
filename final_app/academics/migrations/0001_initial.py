# Generated by Django 5.2.1 on 2025-06-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('assignment_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('blackboard_assignment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('assignment_type', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField()),
                ('weight_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('estimated_effort_hours', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('is_completed', models.IntegerField(blank=True, null=True)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'assignments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('blackboard_course_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('course_code', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=255)),
                ('instructor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('syllabus_url', models.TextField(blank=True, null=True)),
                ('course_difficulty', models.IntegerField(blank=True, null=True)),
                ('current_grade_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'courses',
                'managed': False,
            },
        ),
    ]
