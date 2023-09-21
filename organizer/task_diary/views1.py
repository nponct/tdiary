from django.shortcuts import render
from datetime import datetime,timedelta
from rest_framework import viewsets

from .serializers import ClaimSerializer, CategorySerializer, DoctorSerializer

from . import models
from .models import Category




class AllDoctorsView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return models.Doctor.objects.all()

class OnlySpecDoctorsView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return models.Doctor.objects.filter(spec__name=self.request.kwargs.get('name'))

class OnlySpecClaimView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__spec__name=self.request.kwargs.get('name'))


class OnlyDoctorClaimView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__lastname=self.request.kwargs.get('name'))


class AllClaimsOnlySpecNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__spec__name=self.request.kwargs.get('name')).count()


class  TodayAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(visittime=datetime.today())


class  TomorrowAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(visittime=datetime.today()+timedelta(hours=24))


class  WeekLaterAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(visittime=datetime.today()+timedelta(hours=168))



class  OneDoctorWeekLaterAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__lastname=self.request.kwargs.get('name'),
                                           visittime=datetime.today()+timedelta(hours=168))




class  OneDoctorTodayAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__lastname=self.request.kwargs.get('name'),
                                           visittime=datetime.today())

class  OneDoctorTomorrowLaterAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__lastname=self.request.kwargs.get('name'),
                                           visittime=datetime.today()+timedelta(hours=24))

