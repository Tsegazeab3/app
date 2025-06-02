from django.db import models
from academics.models import Courses, Assignments
from users.models import Users

# Create your models here.
class StudyBlocks(models.Model):
    block_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    assignment = models.ForeignKey(Assignments, models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey('StudyTopics', models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    actual_duration_minutes = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_blocks'

class StudyTopics(models.Model):
    topic_id = models.CharField(primary_key=True, max_length=36)
    course = models.ForeignKey(Courses, models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_completed = models.IntegerField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    parent_topic = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_topics'


