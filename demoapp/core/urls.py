from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.submit_contact, name="submit_contact"),
    path("dashboard/", views.metabase_view, name="metabase"),
]
