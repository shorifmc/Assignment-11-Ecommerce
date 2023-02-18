from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog, name= 'home'),
    path('form/',views.show_form, name= 'sform'),

]

