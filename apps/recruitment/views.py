from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import QuestionsForRecruitmentSerializer, FormResponsesSerializer, SubmittedUserSerializer
from .models import QuestionsForRecruitment, FormResponses, SubmittedUser
# Create your views here.


class QuestionsForRecruitmentView(APIView):

    def get(self, request, *args, **kwargs):
        queryset_openall = QuestionsForRecruitment.objects.filter(question_for_domain="All")
        queryset_web = QuestionsForRecruitment.objects.filter(question_for_domain="Web")
        queryset_design = QuestionsForRecruitment.objects.filter(question_for_domain="Design")
        queryset_pr = QuestionsForRecruitment.objects.filter(question_for_domain="PR")
        queryset_core = QuestionsForRecruitment.objects.filter(question_for_domain="Core")
        queryset_docs = QuestionsForRecruitment.objects.filter(question_for_domain="Docs")

        serializer_class_openall = QuestionsForRecruitmentSerializer(queryset_openall, many=True)
        serializer_class_web = QuestionsForRecruitmentSerializer(queryset_web, many=True)
        serializer_class_design = QuestionsForRecruitmentSerializer(queryset_design, many=True)
        serializer_class_pr = QuestionsForRecruitmentSerializer(queryset_pr, many=True)
        serializer_class_core = QuestionsForRecruitmentSerializer(queryset_core, many=True)
        serializer_class_docs = QuestionsForRecruitmentSerializer(queryset_docs, many=True)

        hashy = {
            'openall': serializer_class_openall.data,
            'web': serializer_class_web.data,
            'design': serializer_class_design.data,
            'pr': serializer_class_pr.data,
            'core': serializer_class_core.data,
            'docs':serializer_class_docs.data
        }
        return Response(hashy)



class CandidateFormResponsesAPIView(APIView):
    def get(self,request,*args, **kwargs):
        queryset1 = SubmittedUser.objects.all()
        queryset2 = FormResponses.objects.all()

        serializer_class1 = SubmittedUserSerializer(queryset1, many=True)
        serializer_class2 = FormResponsesSerializer(queryset2, many=True)

        candidate_dict = {'CandidateData' : serializer_class1.data ,'CandidateResponses' : serializer_class2.data}

        return Response(candidate_dict)
