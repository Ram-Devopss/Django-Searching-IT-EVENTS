
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from requests import request
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
import csv
import pandas as p
import spacy
from django.http import JsonResponse
import lxml
import loginpage
import re
import certifi
import urllib3
import ssl
import urllib.request



# Develop by Ram
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import urllib3
from requests.exceptions import ConnectionError
######################

def home(request):
    
 
    return render(request,"loginpage/home.html") 



def signup(request):
        if request.method=="POST":
            
            username=request.POST.get("username")
            name1=request.POST.get("name")
            email=request.POST.get("email")
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
                   
            print(username,pass1)
            if User.objects.filter(username=username):
                
               messages.error(request,"Username already exist!Please try some other username")
               return redirect('signup')
           
            if   len(username)>10:
                 messages.error(request,"Username must be under 10 Characters")
                 return redirect('signup')
             
            if   len(username)<4:
                 messages.error(request,"Username length should be minimum 4 characters")
                 return redirect('signup')
             
            if not username.isalnum():
                 messages.error(request,"Username must be Alpha-Numeric!")
                 return redirect('signup')
             
            if   len(pass1)<5:
                 messages.error(request,"Password length should be minimum 5 characters..")
                 return redirect('signup')
             
            if   len(pass1)>8:
                 messages.error(request,"Password length should be maximum 8 characters only..")
                 return redirect('signup')
             
            if pass1!=pass2:
                messages.error(request,"Passwords entered do not match! ")
                return redirect('signup')
           
           
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save() 
            messages.success(request,"Your account has been Created Successfully!!!")  
            return redirect('log')   
           
       
        return render(request,"loginpage/signup.html")  
@csrf_protect   
def log(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass1')
        
        user=authenticate(username=username,password=password)
        print(username,password)
        if user is not None:
           login(request,user)
           messages.success(request,"Welcome,You are Successfully Logged in!!!")
           return redirect('signin')
        else:
            messages.error(request,"Username or Password is incorrect.Please try again..")
            return redirect('log')
    
    return render(request,"loginpage/log.html")

@csrf_protect
def passchange(request):
        if request.method=="POST":
            
            username=request.POST.get("username")
            pass_new=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
            
            if   len(pass_new)<5:
                 messages.error(request,"Password length should be minimum 5 characters..")
                 return redirect('passchange')
             
            if   len(pass_new)>8:
                 messages.error(request,"Password length should be maximum 8 characters only..")
                 return redirect('passchange')
             
            if pass_new!=pass2:
                messages.error(request,"Passwords entered do not match! ")
                return redirect('passchange')
                               
            print(username,pass_new)
            try:
                user = User.objects.get(username=username)
                user.set_password(pass_new)
                user.save()
                print(f"Password changed successfully for user '{username}'.")
                messages.success(request,"Password changed successfully!!!")
                return redirect('log')
            except User.DoesNotExist:
                print(f"User '{username}' does not exist.")
                messages.error(request,"User does not exist,Please enter the correct Username.")
        return render(request,"loginpage/passchange.html") 
      
@csrf_protect
def signin(request):  
    
 
     
    return render(request,"loginpage/signin.html")
@csrf_protect   



## getting datas on the 10th number of requests
########### Develop By Ram
def iit(request):
    text_list = []

    modified_elements = []
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    max_pages = 10
    current_page = 0

    try:
        while current_page <= max_pages:
            url = "https://www.timesnownews.com/latest-news"
            current_url = f'{url}?page={current_page}'

            print(current_url)
            response = requests.get(current_url, verify=False)
            
            # Raise an exception if the response status code is not 200 (OK)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            events_div = soup.find_all('div', {'class': '_1W5s'})
 #           elements_with_class = events_div.find_all(class_='_1W5s')

            for element in events_div:
                anchor_text = element.text
                anchor_text = anchor_text.replace('\n', '')
                text_list.append(anchor_text)

            current_page += 1

    except ConnectionError as e:
        print("ConnectionError:", e)
        # You can handle the connection error here, such as retrying the connection or logging the error.

    except Exception as e:
        print("An error occurred:", e)
        # Handle other types of exceptions if necessary.

    return render(request, "loginpage/aigov.html", {'links': text_list})


############################



########### Develop By Ram

def AICTE(request):
    text_list = []

    modified_elements = []
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    max_pages = 10
    current_page = 0

    try:
        while current_page <= max_pages:
            url = "https://internship.aicte-india.org/fetch_city.php?city=Q2hlbm5haQ=="
            current_url = f'{url}'

            print(current_url)
            response = requests.get(current_url, verify=False)
            
            # Raise an exception if the response status code is not 200 (OK)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            events_div = soup.find('div', {'class': 'col'})
            elements_with_class = events_div.find_all(class_='internship-info')

            for element in elements_with_class:
                anchor_text = element.text
                anchor_text = anchor_text.replace('\n', '')
                text_list.append(anchor_text)

            current_page += 1

    except ConnectionError as e:
        print("ConnectionError:", e)
        # You can handle the connection error here, such as retrying the connection or logging the error.

    except Exception as e:
        print("An error occurred:", e)
        # Handle other types of exceptions if necessary.

    return render(request, "loginpage/aigov.html", {'links': text_list})


############################


########### Develop By Ram

def NCS(request):
    text_list = []

    modified_elements = []
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    max_pages = 10
    current_page = 0

    try:
        while current_page <= max_pages:
            url = "https://www.ncs.gov.in//Pages/Search.aspx"
            current_url = f'{url}'

            print(current_url)
            response = requests.get(current_url, verify=False)
            
            # Raise an exception if the response status code is not 200 (OK)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            events_div = soup.find('div', {'class': 'panel-body padding0'})
            elements_with_class = events_div.find_all(class_='row padding0-15')

            for element in elements_with_class:
                anchor_text = element.text
                anchor_text = anchor_text.replace('\n', '')
                text_list.append(anchor_text)

            current_page += 1

    except ConnectionError as e:
        print("ConnectionError:", e)
        # You can handle the connection error here, such as retrying the connection or logging the error.

    except Exception as e:
        print("An error occurred:", e)
        # Handle other types of exceptions if necessary.

    return render(request, "loginpage/aigov.html", {'links': text_list})

############################





########### Develop By Ram
def TCS(request):
    text_list = []

    modified_elements = []
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    max_pages = 10
    current_page = 0

    try:
        while current_page <= max_pages:
            url = "https://ibegin.tcs.com/iBegin/jobs/search"
            current_url = f'{url}'

            print(current_url)
            response = requests.get(current_url, verify=False)
            
            # Raise an exception if the response status code is not 200 (OK)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            events_div = soup.find('div', {'data-ng-if': 'isGrs() && noexp() && noexpus()'})
            elements_with_class = events_div.find_all(class_='job-data-bar')

            for element in elements_with_class:
                anchor_text = element.text
                anchor_text = anchor_text.replace('\n', '')
                text_list.append(anchor_text)

            current_page += 1

    except ConnectionError as e:
        print("ConnectionError:", e)
        # You can handle the connection error here, such as retrying the connection or logging the error.

    except Exception as e:
        print("An error occurred:", e)
        # Handle other types of exceptions if necessary.

    return render(request, "loginpage/aigov.html", {'links': text_list})

############################





########### Develop By Ram

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import urllib3

def INFO(request):
    text_list = []

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    max_pages = 10
    current_page = 0

    try:
        while current_page <= max_pages:
            url = "https://career.infosys.com/joblist?countrycode=IN&companyhiringtype=IL"
            current_url = f'{url}&page={current_page + 1}'

            print(current_url)
            response = requests.get(current_url, verify=False)
            
            # Raise an exception if the response status code is not 200 (OK)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            
            # Adjust the selector based on the HTML structure of the page
            job_listings = soup.find_all('div', class_='col-md-8')

            for job_listing in job_listings:
                job_title = job_listing.find('row marT10 nomarLR').text.strip()
                job_location = job_listing.find('div', class_='location').text.strip()
                # You can extract other details like job description, company name, etc.

                # Create a dictionary to store job details
                job_details = {
                    'title': job_title,
                    'location': job_location
                    # Add other details here
                }

                text_list.append(job_details)

            current_page += 1

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        # Handle other types of exceptions if necessary.

    return render(request, "loginpage/aigov.html", {'job_listings': text_list})


############################

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')