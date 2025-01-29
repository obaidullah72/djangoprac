from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # Class-based views
    path("", views.IndexView.as_view(), name="index"),  # Homepage showing the latest polls
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # Poll detail view
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  # Poll results view

    # Function-based views
    path("<int:question_id>/vote/", views.vote, name="vote"),  # Voting endpoint
]
