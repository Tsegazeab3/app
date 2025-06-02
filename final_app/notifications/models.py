from django.db import models
from users.models import Users

# Create your models here.
class Notifications(models.Model):
    notification_id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(Users, models.DO_NOTHING)
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



