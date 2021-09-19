from django.urls import path

from users.views import login, registration, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),
]
