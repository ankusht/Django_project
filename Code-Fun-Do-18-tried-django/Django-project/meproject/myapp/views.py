
from django.shortcuts import render, redirect
from django.http import HttpResponse
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from django.core.mail import send_mail
import myapp.lib.output_fb as fb
import myapp.lib.yt_output as youtube
# Create your views here.
def hello(request) :
	alph = 110
	return render(request, "hello.html", {"alpha" : alph})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return redirect("https://www.facebook.com")	

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "sainiabhi7734@gmail.com", [emailto])
   return HttpResponse('%s'%res)

def alphaFn(request, var) :
	return redirect(sendSimpleEmail,"abhisni@iitk.ac.in")
	
def fb_video(request) :
    alph = 4
    video_url = "https://www.facebook.com/election.commission.iitk/videos/597396273797338/"
    output = fb.main(video_url)
    print(output)
    return render(request, "aa.html", {"array1" : output["time_break_list"]})

def youtube_video(request) :
    video_url = "https://www.youtube.com/watch?v=3KenEVty7gg"
    output = youtube.main(video_url)
    print(output)
    return render(request, "aa.html", {"array1" : 1})




# # # # # # # # # # # # # # # # # # # # # # # # 

from myapp.models import Dreamreal
from django.http import HttpResponse

def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)	
   
def datamanipulation(request):
   res = ''
   
   #Filtering data:
   qs = Dreamreal.objects.filter(name = "paul")
   res += "Found : %s results<br>"%len(qs)
   
   #Ordering results
   qs = Dreamreal.objects.order_by("name")
   
   for elt in qs:
      res += elt.name + '<br>'
   
   return HttpResponse(res)
'''
from django.http import HttpResponse

def hello(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)
   '''
