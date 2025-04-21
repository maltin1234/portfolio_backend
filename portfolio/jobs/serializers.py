from rest_framework import serializers
from .models import Job, Candidate, Interview

# -----------------------------------
# Job Serializer
# -----------------------------------
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


# -----------------------------------
# Candidate Serializer
# -----------------------------------
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


# -----------------------------------
# Interview Serializer
# -----------------------------------
class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'
class InterviewNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['id', 'scheduled_for', 'interviewer', 'result']

class CandidateNestedSerializer(serializers.ModelSerializer):
    interviews = InterviewNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'email', 'status', 'applied_at', 'interviews']

class JobDetailSerializer(serializers.ModelSerializer):
    candidates = CandidateNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
