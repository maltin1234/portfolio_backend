from django.db import models

# -----------------------------------
# Job Post
# -----------------------------------
class Job(models.Model):
    company_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    hires_needed = models.PositiveIntegerField(default=1)
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100, default='English')
    location = models.CharField(max_length=255)
    
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship'),
    ]
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    
    contract_length = models.CharField(max_length=100, blank=True)
    schedule = models.CharField(max_length=255, blank=True)
    pay = models.CharField(max_length=100, blank=True)
    supplemental_pay = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    company = models.CharField(max_length=200, blank=True)
    
    description = models.TextField()
    pre_screening = models.TextField(blank=True)
    
    require_resume = models.BooleanField(default=True)
    contact_email = models.EmailField()
    application_deadline = models.DateField(null=True, blank=True)
    expected_start_date = models.DateField(null=True, blank=True)
    
    approved = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)

    # Analytics
    views = models.PositiveIntegerField(default=0)
    applications = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} at {self.company_name}"
    

# -----------------------------------
# Candidate (Job Application)
# -----------------------------------
class Candidate(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='candidates')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('reviewed', 'Reviewed'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('interviewed', 'Interviewed'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='applied')

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.status}"


# -----------------------------------
# Interview
# -----------------------------------
class Interview(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='interviews')
    scheduled_for = models.DateTimeField()
    interviewer = models.CharField(max_length=255)
    location_or_link = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    feedback = models.TextField(blank=True)

    RESULT_CHOICES = [
        ('pending', 'Pending'),
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('reschedule', 'Reschedule'),
    ]
    result = models.CharField(max_length=50, choices=RESULT_CHOICES, default='pending')

    def __str__(self):
        return f"Interview with {self.candidate.name} on {self.scheduled_for}"
