from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job, Candidate, Interview
from .serializers import JobSerializer, CandidateSerializer, InterviewSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['company', 'location', 'job_type']
    search_fields = ['title', 'company', 'location', 'description']
    ordering_fields = ['posted_at', 'title', 'location']


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all().order_by('-applied_at')
    serializer_class = CandidateSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['job', 'status']
    search_fields = ['name', 'email', 'resume']
    ordering_fields = ['applied_at', 'status']


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all().order_by('-scheduled_for')
    serializer_class = InterviewSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['candidate', 'interviewer']
    search_fields = ['notes']
    ordering_fields = ['scheduled_for', 'interviewer']
