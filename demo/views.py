import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

from .forms import InputImageForm


logger = logging.getLogger(__name__)


class UploadView(LoginRequiredMixin, View):
    def get(self, request, *arts, **kwargs):

        context = {"form": InputImageForm()}
        return render(request, "demo/upload.html", context)

    def post(self, request, *args, **kwargs):

        form = InputImageForm(request.POST, request.FILES)
        input_image = form.save(commit=False)
        input_image.submitter = self.request.user  # モデルオブジェクトの save() 時にファイルがアップロードされる
        input_image.save()
        return redirect(reverse("demo:upload"))


upload = UploadView.as_view()
