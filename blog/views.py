from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

companyName = "E-Links"

VoterId = "https://voters.eci.gov.in"

PanCard = "https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html?utm_source=Google&utm_medium=cpc&utm_campaign=Pan_Search_Comp_Exact_Oct24&adgroup=UTIITSL&gad_source=1&gclid=Cj0KCQiAvP-6BhDyARIsAJ3uv7aSxdv-Y0YTBUaaU53pk5wcjra7kYU-ylUlKM7_tM26d1A2oYPRcUUaAit1EALw_wcB"

StatusPanApplication = "https://tin.tin.nsdl.com/pantan/StatusTrack.html"

DrivingLicense = "https://sarathi.parivahan.gov.in/sarathiservice/stateSelection.do"

FrontendMentor = "https://www.frontendmentor.io/"

CssTricks = "https://css-tricks.com/"

JavaScript30 = "https://javascript30.com/"

FreeCodeCamp = "https://www.freecodecamp.org/learn"

Firebird = "https://www.firebirdsql.org/"

def index(request):
    return render(request,'index.html',{'companyame':companyName,'VoterId':VoterId,'PanCard':PanCard,'StatusPanApplication':StatusPanApplication,'DrivingLicense':DrivingLicense,'FrontendMentor':FrontendMentor,'CssTricks':CssTricks,'JavaScript30':JavaScript30,'FreeCodeCamp':FreeCodeCamp,'Firebird':Firebird})

def contact(request):
    return render(request,'includes/contact.html',{'companyame':companyName})

def about(request):
    return render(request,'includes/about.html',{'companyame':companyName})

def register(request):
    return render(request,'includes/register.html')