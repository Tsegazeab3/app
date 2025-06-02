from django.db import models
from institutions.models import AcademicInstitutions 
from users.models import Users
# Create your models here.

class Courses(models.Model):
    course_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    institution = models.ForeignKey(AcademicInstitutions, models.DO_NOTHING, blank=True, null=True)
    blackboard_course_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=255)
    instructor_name = models.CharField(max_length=255, blank=True, null=True)
    syllabus_url = models.TextField(blank=True, null=True)
    course_difficulty = models.IntegerField(blank=True, null=True)
    current_grade_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'
        unique_together = (('user', 'course_code'),)

class Assignments(models.Model):
    assignment_id = models.CharField(primary_key=True, max_length=36)
    course = models.ForeignKey(Courses, models.DO_NOTHING)
    blackboard_assignment_id = models.CharField(max_length=255, blank=True, null=True)
    assignment_type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    weight_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    estimated_effort_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_completed = models.IntegerField(blank=True, null=True)
    completion_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignments'

