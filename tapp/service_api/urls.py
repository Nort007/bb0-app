from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('aggregateDataList/', views.AggregateList.as_view()),
    path('addAggregateData/', views.AddAggregateData.as_view()),
    path('aggregateData/<int:pk>/', views.AggregateDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
