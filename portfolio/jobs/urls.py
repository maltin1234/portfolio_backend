# portfolioapp/urls.py

from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CandidateViewSet, InterviewViewSet

router = DefaultRouter()
router.register('jobs', JobViewSet)
router.register('candidates', CandidateViewSet)
router.register('interviews', InterviewViewSet)

# Export the router itself
app_name = "jobs"
router_jobs = router  # 👈 rename so you can import it in main urls.py
