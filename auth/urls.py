from django.urls import path

urlpatterns = [
    path('login/', login_view.as_view(), name='login'),
    path('register/', register_view.as_view(), name='register')
]