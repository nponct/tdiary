from django.urls import path
from .views import TaskChangeView,TaskActionView
from .import views



urlpatterns=[

    path('tasks/',views.TaskChangeView.as_view({'get':'list','post':'create'})),
    path('tasks/<int:pk>/',views.TaskChangeView.as_view({'put':'update','delete':'destroy'})),
    path('taskact/',views.TaskActionView.as_view({'get':'list','post':'create'})),
    path('taskact/<int:pk>/',views.TaskActionView.as_view({'put':'update','delete':'destroy'})),
]