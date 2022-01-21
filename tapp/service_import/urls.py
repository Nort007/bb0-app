from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views


urlpatterns = [
    path('origRunImportTask/', views.OrigSortedTask.as_view()),
    path('runImportTask/', views.SortedTask.as_view()),
    path('sortedDataList/', views.SortedDataList.as_view()),
    path('runImportTaskThroughApi/', views.SortedDataThroughApi.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
