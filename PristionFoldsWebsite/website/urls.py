from django.urls import path
from .views import *

urlpatterns = [
    path('pristionfoldsenquiry/', PristionFoldsEnquiry.as_view(), name='PristionFolds-Enquiry'), 
]