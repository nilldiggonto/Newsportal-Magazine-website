from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required


###
from django.core.mail import send_mail
from django.conf import settings
from .tokens import account_activation_token

from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def registrationView(request):
    user =User.objects.get(username="nill")
    template_name = 'accounts/register.html'

    if request.method == 'POST':
        username = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():

            return render(request,template_name,{'valid':False})
        else:
            user = User.objects.create(first_name=fname,last_name=lname,username=username,email=username,is_active=False)
            user.set_password(password)
            user.active=False
            user.save()
            ### SENDING EMAIL FOR VERIFICATION
            current_site = str(get_current_site(request).domain)
            print(current_site)
            mail_subject = 'Activate your newsCarrier account.'
            message = render_to_string('acc_active_email.html', {
                'first_name': user.first_name,
                
                'last_name':user.last_name,
                'domain': current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            # print(message)
            plain_message = strip_tags(message)

            to_email = username
            email = EmailMessage(
                        mail_subject, plain_message, to=[to_email]
            )
            # email.attach_alternative(message, 'text/html')
            email.send()
            request.session['vmsg'] = True

            return redirect('auth-login')
    
    return render(request,template_name,{'valid':True})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        if 'vmsg' in request.session:
            del request.session['bar']
        return redirect('dashboard-home')
    else:
        return HttpResponse('Activation link is invalid!')



def loginView(request):
    template_name = 'accounts/login.html'
    a = ''
    if request.user.is_authenticated:
        return redirect('dashboard-home')
        
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username,is_active=False):
            a = 'ask antu to verify. will automate later'

        # print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('dashboard-home')
        else:
            a = 'please register sir'

    return render(request,template_name,context={'a':a})

@login_required
def logoutView(request):
    user = logout(request)
    return redirect('home-page')
   
    

