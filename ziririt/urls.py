from django.contrib import admin
from django.urls import path, include
from .views import main, home, credit, gumi

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('', main, name='mainpage'),
    path('home/', home, name='homepage'),
    path('credit/', credit, name='credit'),
    path('gumi', gumi, name='gumi'),
]
