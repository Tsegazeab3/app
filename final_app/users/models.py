from django.db import models
# Create your models here.
class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=36)
    email = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    timezone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class UserPreferences(models.Model):
    preference_id = models.CharField(primary_key=True, max_length=36)
    user = models.OneToOneField(Users, models.DO_NOTHING)
    preferred_study_times = models.JSONField(blank=True, null=True)
    preferred_study_duration_minutes = models.IntegerField(blank=True, null=True)
    preferred_break_duration_minutes = models.IntegerField(blank=True, null=True)
    weekly_study_hours_target = models.IntegerField(blank=True, null=True)
    learning_style = models.JSONField(blank=True, null=True)
    focus_issues = models.TextField(blank=True, null=True)
    procrastination_tendency = models.TextField(blank=True, null=True)
    sleep_bed_time = models.TimeField(blank=True, null=True)
    sleep_wake_time = models.TimeField(blank=True, null=True)
    preferred_reward_system = models.TextField(blank=True, null=True)
    notification_email = models.IntegerField(blank=True, null=True)
    notification_web_push = models.IntegerField(blank=True, null=True)
    notification_in_app = models.IntegerField(blank=True, null=True)
    notification_timing_before_study_minutes = models.IntegerField(blank=True, null=True)
    notification_daily_summary_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_preferences'


class UserGoals(models.Model):
    goal_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    goal_type = models.CharField(max_length=50)
    description = models.TextField()
    target_date = models.DateField(blank=True, null=True)
    is_achieved = models.IntegerField(blank=True, null=True)
    achieved_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_goals'



class UserInstitutionConnections(models.Model):
    connection_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    #institution = models.ForeignKey('AcademicInstitutions', models.DO_NOTHING)
    blackboard_access_token = models.TextField(blank=True, null=True)
    blackboard_refresh_token = models.TextField(blank=True, null=True)
    blackboard_token_expires_at = models.DateTimeField(blank=True, null=True)
    last_synced_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_institution_connections'


