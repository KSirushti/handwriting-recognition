from django.urls import path
from . import views

urlpatterns = [
    path('predict-character/', views.predict_character, name='predict_character'),
    path('submit-correction/', views.submit_correction, name='submit_correction'),
]