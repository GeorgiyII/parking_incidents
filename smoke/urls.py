from django.urls import path
from smoke import views


urlpatterns = [
    path('smoke/', views.Smoke.as_view(), name='smoke'),
]
