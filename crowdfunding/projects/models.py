from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
CATEGORIES = (
        ("Builder", "Builder"),
        ("Plumbing", "Plumbing"),
        ("Carpentry", "Carpentry"),
        ("Electrician", "Electrician")
    )

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    image=models.URLField()
    is_open=models.BooleanField()
    date_work_starts=models.DateTimeField() #date_work_starts make this into a calendar for selection
    date_closed=models.DateField() #date_closed make this into a calendar for selection
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
        
    ) 
        
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE, #everything linked to deleted project will also be deleted
        related_name='pledges'
    )

    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )