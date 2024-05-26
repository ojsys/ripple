from django.contrib.auth.models import User
from django.db import models


# All models

# User Profile Model
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
    

# Campaign Model
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
    
# Contribution model
class Contribution(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_contributed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.contributor.user.username} contributed {self.amount} to {self.campaign}'
    

# Donation Model
class Donation(models.Model):
    project = models.ForeignKey(Campaign, on_delete=models.CASCADE)  # Assuming donations are linked to campaigns
    donor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_donated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.user.username} donated {self.amount}"


# Investment Proposal Model
class InvestmentProposal(models.Model):
    entrepreneur = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    investors = models.ManyToManyField(Profile, related_name='investments', blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


