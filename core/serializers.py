from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile, Campaign, Contribution, Donation, InvestmentProposal



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'location', 'is_entrepreneur', 'is_investor', 'is_donor', 'is_community_member']



class CampaignSerializer(serializers.ModelSerializer):
    entrepreneur = ProfileSerializer()

    class Meta:
        model = Campaign
        fields = ['id', 'title', 'description', 'entrepreneur', 'goal_amount', 'current_amount', 'start_date', 'end_date']



class ContributionSerializer(serializers.ModelSerializer):
    contributor = ProfileSerializer()

    class Meta:
        model = Contribution
        fields = ['id', 'campaign', 'contributor', 'amount', 'date_contributed']



class DonationSerializer(serializers.ModelSerializer):
    donor = ProfileSerializer()

    class Meta:
        model = Donation
        fields = ['id', 'project', 'donor', 'amount', 'date_donated']



class InvestmentProposalSerializer(serializers.ModelSerializer):
    entrepreneur = ProfileSerializer()
    investors = ProfileSerializer(many=True)

    class Meta:
        model = InvestmentProposal
        fields = ['id', 'entrepreneur', 'title', 'description', 'amount_requested', 'amount_invested', 'investors', 'date_submitted', 'is_approved']