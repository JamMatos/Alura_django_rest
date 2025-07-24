from django.urls import path
from escola.views import estudantes

urlpatterns = [
    path('estudantes/', estudantes),
]