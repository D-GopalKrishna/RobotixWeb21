from rest_framework import serializers
from .models import QuestionsForRecruitment, FormResponses, SubmittedUser



class QuestionsForRecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsForRecruitment
        fields = "__all__"


## Form responses Serializers and viewsets
class FormResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormResponses
        fields = "__all__"


class SubmittedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubmittedUser
        fields = "__all__"