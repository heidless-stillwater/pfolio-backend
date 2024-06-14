from django.urls import path
from .views import AppListView

urlpatterns = [
    path('', AppListView.as_view()),
]
