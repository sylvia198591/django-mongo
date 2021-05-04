from UserLog.views import ExampleView, CustomAuthToken
from django.urls import path
urlpatterns = [
    path('api/users/',ExampleView.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view()),
]