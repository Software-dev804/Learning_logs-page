from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name= 'topics'),
    path('topics/<str:topic_id>', views.topic, name='topic'),
]