from django.conf.urls import url

from app import views

app_name='app'


urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^home/',views.home_page,name='home'),
    url(r'^home/lists/the-only-list-in-the-world/$',views.home_page,name='home'),
]