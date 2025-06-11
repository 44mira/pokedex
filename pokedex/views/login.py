from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django import forms


class LoginUser(LoginView):
    extra_context = {"message": "Log-in"}
    template_name = "auth_user.html"


class LogoutUser(LoginRequiredMixin, LogoutView):
    http_method_names = ["get", "post", "options"]

    def get(self, request):
        return render(request, "logout.html")
