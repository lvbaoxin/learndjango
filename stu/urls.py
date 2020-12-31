from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_view, name="index"),
    url(r'^register/', views.register_view, name='register'),
    url(r'^movie/', views.movie_view, name='movie'),
    url(r'^show/', views.show_view, name='show'),
    url(r'^login/', views.login_view, name='login')
]
