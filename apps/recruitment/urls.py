from django.urls import path, include
from rest_framework import routers
# from .views import FormResponsesViewset, QuestionsForRecruitmentViewset, FormResponsesAPIView
from .views import CandidateFormResponsesAPIView, QuestionsForRecruitmentView


app_name = 'recruitment'

urlpatterns = [
    path('questions/', QuestionsForRecruitmentView.as_view()), 
    path('', CandidateFormResponsesAPIView.as_view())
]   