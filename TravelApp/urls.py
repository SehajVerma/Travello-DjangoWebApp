from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^index/', views.index, name='index'),
    url(r'^destinations/',views.destinations,name="destinations"),
    url(r'^contact/',views.contact,name="contact"),
    url(r'^elements/',views.elements,name="elements")
]