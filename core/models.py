from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    is_entrepreneur = models.BooleanField(default=False)
    is_investor = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    is_community_member = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
    


class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    entrepreneur = models.ForeignKey(Profile, on_delete=models.CASCADE)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

class Contribution(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_contributed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.contributor.user.username} contributed {self.amount} to {self.campaign}'