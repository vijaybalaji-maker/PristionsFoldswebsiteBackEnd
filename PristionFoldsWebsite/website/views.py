from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.db import transaction
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Case, When, BooleanField, F, Count, Sum,Q
from datetime import datetime, date
from django.utils.timezone import now
from django.core.cache import cache
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from django.contrib.auth.hashers import make_password,check_password
from datetime import timedelta
# from .authentication import CustomAuthBackend
import random
import csv
from django.http import HttpResponse

from .serializers import *


class PristionFoldsEnquiry(APIView):

    def post(self, request):
        company_name = request.data.get("company_name")
        year_of_establishment = request.data.get("year_of_establishment")
        country = request.data.get("country")
        state = request.data.get("state")
        district = request.data.get("district")
        pincode = request.data.get("pincode")
        number_of_branch = request.data.get("number_of_branch")
        email = request.data.get("email")
        mobile_number = request.data.get("mobile_number")
        alternate_number = request.data.get("alternate_number")if request.data.get('alternate_number') else None

        data = {
            "company_name": company_name,
            "country": country,
            "year_of_establishment": year_of_establishment,
            "district": district,
            "state": state,
            "email": email,
            "pincode": pincode,
            "number_of_branch": number_of_branch,
            "mobile_number": mobile_number,
            "alternate_number": alternate_number,
        }

        serializer = PristionFoldsEnquirySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "True", "message": "Enquiry Details added successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"status": "error", "message": "Failed to add Enquiry Details", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )