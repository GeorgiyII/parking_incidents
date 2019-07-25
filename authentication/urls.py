from django.urls import path
from authentication import views


urlpatterns = [
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
    path('facebook/', views.FacebookLogin.as_view(), name='facebook_login')
]
