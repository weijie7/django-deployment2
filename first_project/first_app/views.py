from django.shortcuts import render, redirect
from first_app.models import Topic, Webpage, AccessRecord
from first_app.forms import FormName, UserProfileForm, UserForm

#for login handler
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect


def user_login(request): #make sure this is not named as login/logout, as it will overwrite fn above
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account is not active")
        else:
            print("login failed")
            print(f'{username} and {password} failed')
            return HttpResponse("Invalid login")
    else:
        return render(request, 'first_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) 

@login_required
def special(request):
    return HttpResponse("you are logged in, nice")


# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_rec' : webpage_list}
    return render(request, r'first_app\index.html', context = date_dict)
# each view needs its function - this view is called index
# each view takes at least one argument
# usually called request by convention
# each view MUST return in HTTPresponse object



def registration(request):
    registered = False
    user_form = UserForm()
    profile_form = UserProfileForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    
    return render(request, 'first_app/form_page.html', 
    {'user_form' : user_form , 'profile_form': profile_form, 'registered' : registered })


def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            # do something code will work
            print("VALIDATION SUCCESS")
            print("Name :" + form.cleaned_data['name'])
            print("EMAIL :" + form.cleaned_data['email'])
            print("TEXT :" + form.cleaned_data['text'])

    return render(request, r'first_app\form_page.html', {'form' : form})