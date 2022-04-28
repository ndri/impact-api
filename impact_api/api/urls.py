from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluations/<str:charity_name>/<int:year>', views.evaluation, name='evaluation'),
    path('distributions/<int:year>/<int:month>', views.max_impact_distribution, name='max_impact_distribution')
]