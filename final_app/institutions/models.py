from django.db import models
from users.models import Users
# Create your models here.
class AcademicInstitutions(models.Model):
    institution_id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    blackboard_api_base_url = models.CharField(max_length=255, blank=True, null=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    api_secret = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_institutions'

