from django.urls import path

from .import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("apply/", views.ApplyView.as_view(), name="apply")
]
