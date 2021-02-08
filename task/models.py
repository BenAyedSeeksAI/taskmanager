from django.db import models

# Create your models here.
class work(models.Model):
    work_content = models.CharField(max_length=250)
    work_hours_per_day = models.IntegerField(default=0)
    work_money = models.IntegerField(default=0)
    work_company = models.CharField(max_length=250)
    work_country = models.CharField(max_length=250)
    def __str__(self):
        return self.work_content + '-' + self.work_company + '-' + self.work_country


