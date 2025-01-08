from rest_framework import serializers
from .models import *



class PristionFoldsEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrsitionFoldsEnquiry
        fields = '__all__' 
