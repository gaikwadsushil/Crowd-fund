from django.db import models
class MotiveType(models.TextChoices):
    SOCIAL_CAUSE = 'Social Cause', 'Social Cause'
    ENVIRONMENTAL = 'Environmental', 'Environmental'
    EDUCATIONAL = 'Educational', 'Educational'
    MEDICAL = 'Medical','Medical'
    CHARITY = 'Charity','Charity'
    OTHER = 'Other','Other'
    
class Motive(models.Model):
    name = models.CharField(max_length=50,unique=True)
    logo = models.ImageField()
    motive_type = models.CharField(max_length=50,choices=MotiveType.choices,default=MotiveType.SOCIAL_CAUSE,)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Group(models.Model):
    group_name = models.CharField(max_length=50,default=" ",null= False)
    group_desc = models.TextField

