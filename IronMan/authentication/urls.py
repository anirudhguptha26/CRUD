from django.urls import path
from authentication import views

urlpatterns = [
    path('',views.login_view, name="login"),
    path('sign_up', views.sign_up, name='sign_up')
]