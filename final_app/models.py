# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#academic
class AcademicInstitutions(models.Model):
    institution_id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    blackboard_api_base_url = models.CharField(max_length=255, blank=True, null=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    api_secret = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_institutions'



#Authentication
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

#Authentication
class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

#Authentication for the database editing
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


#Authentication for the database editing
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


#Authentication for the database editing
class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


#Authentication for the database editing
class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

#courses
class Courses(models.Model):
    course_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey('Users', models.DO_NOTHING)
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


#Authentication for the database editing
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


#Authentication for the database editing
class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


#Authentication for the database editing
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


#Authentication for the database editing
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

#Notifications
class Notifications(models.Model):
    notification_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    related_entity_type = models.CharField(max_length=50, blank=True, null=True)
    related_entity_id = models.CharField(max_length=36, blank=True, null=True)
    message = models.TextField()
    send_time = models.DateTimeField()
    notification_type = models.CharField(max_length=50)
    is_sent = models.IntegerField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


#streaks
class Streaks(models.Model):
    streak_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    streak_type = models.CharField(max_length=50)
    current_streak_count = models.IntegerField()
    longest_streak_count = models.IntegerField()
    last_updated_at = models.DateTimeField(blank=True, null=True)
    last_successful_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'streaks'
        unique_together = (('user', 'streak_type'),)

#academics
class StudyBlocks(models.Model):
    block_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey('Users', models.DO_NOTHING)
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

#academics
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

#users
class UserGoals(models.Model):
    goal_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    goal_type = models.CharField(max_length=50)
    description = models.TextField()
    target_date = models.DateField(blank=True, null=True)
    is_achieved = models.IntegerField(blank=True, null=True)
    achieved_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_goals'

#users
class UserInstitutionConnections(models.Model):
    connection_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    institution = models.ForeignKey(AcademicInstitutions, models.DO_NOTHING)
    blackboard_access_token = models.TextField(blank=True, null=True)
    blackboard_refresh_token = models.TextField(blank=True, null=True)
    blackboard_token_expires_at = models.DateTimeField(blank=True, null=True)
    last_synced_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_institution_connections'
        unique_together = (('user', 'institution'),)

#users
class UserPreferences(models.Model):
    preference_id = models.CharField(primary_key=True, max_length=36)
    user = models.OneToOneField('Users', models.DO_NOTHING)
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

#users
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


#users
class WellBeingEntries(models.Model):
    entry_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    entry_date = models.DateField(blank=True, null=True)
    stress_level = models.IntegerField(blank=True, null=True)
    motivation_level = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'well_being_entries'
        unique_together = (('user', 'entry_date'),)
