from django.db import models
from users.models import Users

class Streaks(models.Model):
    streak_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    streak_type = models.CharField(max_length=50)
    current_streak_count = models.IntegerField()
    longest_streak_count = models.IntegerField()
    last_updated_at = models.DateTimeField(blank=True, null=True)
    last_successful_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'streaks'
        unique_together = (('user', 'streak_type'),)
# Create your models here.
