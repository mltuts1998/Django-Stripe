from django.urls import path
from strip import views

app_name="strip"

urlpatterns = [
	path('', views.index,name='index' ),
	path('charge', views.charge, name='charge'),
	path('success/<str:args>/', views.success, name='success'),
]