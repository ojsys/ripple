from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, CampaignViewSet, ContributionViewSet, DonationViewSet, InvestmentProposalViewSet, RegisterView

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'campaigns', CampaignViewSet)
router.register(r'contributions', ContributionViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'investment_proposals', InvestmentProposalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register')
]
