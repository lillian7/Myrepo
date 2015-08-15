from django.conf.urls import url
from git_demo.views import Home

urlpatterns = [
    url(r'^$', Home.as_view(), name="index"),]