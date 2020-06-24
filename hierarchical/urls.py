from hierarchical import views
from django.urls import path


urlpatterns = [
    path('', views.hierarchical_data_view)
]
