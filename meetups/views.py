import email
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import DetailView

from meetups.forms import RegistrationForm
from .models import Meetup, Participant
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })

# def meetup_details(request,slug):
#     try:
#         selected_meetup = Meetup.objects.get(slug=slug)

#         if request.method =='GET':
            
#             registration_form = RegistrationForm
      
#         else:
#             registration_form = RegistrationForm(request.POST)
#             if registration_form.is_valid():
#                participant = registration_form.save()
#                selected_meetup.participants.add(participant)
#                redirect()
#         return render(request,'meetups/meetup-details.html',{
#                             'meetup_found':True,
#             'meetup':selected_meetup,
#             'form':registration_form
#             })   
#     except Exception as ex:
#         return render(request, 'meetups/meetup-details.html',{
#             'meetup_found':False
#         })
class meetup_details(View):
    def get(self,request,slug):
        try:
            selected_meetup = Meetup.objects.get(slug=slug)

                
            registration_form = RegistrationForm()
        

            return render(request,'meetups/meetup-details.html',{
                                    'meetup_found':True,
                    'meetup':selected_meetup,
                    'form':registration_form
                    })   
        except Exception as ex:
             return render(request, 'meetups/meetup-details.html',{
                'meetup_found':False
            })
    def post(self, request, slug):
        selected_meetup = Meetup.objects.get(slug=slug)
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
           
               user_email = registration_form.cleaned_data['email']
               participant, was_created =  Participant.objects.get_or_create(email=user_email) # or use _ to ignore by placeholder
               
               selected_meetup.participants.add(participant)
               return redirect('confirm-registration',slug=slug)

class ConfirmRegistrationView(DetailView):
    template_name= 'meetups/registration-success.html'
    model= Meetup
    context_object_name= 'meetup'


# def confirm_registration(request):
#     return render(request,'meetups/registration-success.html')