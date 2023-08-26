from . import views
from django.urls import path,include
urlpatterns = [
   path('', views.index, name="spacehome"),
   path('crop/', views.crop, name="CheckOut"),

]