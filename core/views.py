from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from rest_framework import viewsets
from .models import Profile, Campaign, Contribution, Donation, InvestmentProposal
from .serializers import ProfileSerializer, CampaignSerializer, ContributionSerializer, DonationSerializer, InvestmentProposalSerializer



class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Username, password and email are required'})
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, password=password, email=email)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh), 
            'access': str(refresh.access_token)
            })


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class InvestmentProposalViewSet(viewsets.ModelViewSet):
    queryset = InvestmentProposal.objects.all()
    serializer_class = InvestmentProposalSerializer
