# admin.py

from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CustomUser
from .models import Rating
from django.contrib import admin

class CustomAdminSite(AdminSite):
    login_form = AuthenticationForm

    def login(self, request, extra_context=None):
        if request.method == "POST":
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            # Use email as username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return HttpResponseRedirect(self.get_redirect_url())
            else:
                return render(request, "admin/login.html", {"error": "Invalid credentials"})
        return super().login(request, extra_context)

# Register your custom admin site
admin_site = CustomAdminSite(name="admin")
admin.site.register(Rating)
admin.site.register(CustomUser)
