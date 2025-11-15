from .models import Candidates, Profile
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login

from .forms import UserForm

# Create your views here.
def home(request):
    return render(request,'home.html')


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Profile.objects.create(user = user,
                                   role = form.cleaned_data['role'],
                                   )
            return redirect('signin')
    else:
        form = UserForm()
    return render(request,'signup.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            if user.is_superuser:
                return render(request,'admin/admin.html')
            else :
                role = user.profile.role
                if role == 'candidate':
                    try:
                        candidate = user.profile.candidates
                        return redirect('candidate')
                    except Candidates.DoesNotExist:
                        return render(request,'candidate/candidate_details.html')
                elif role == 'company':
                    return render(request,'company/company.html')
        else:
            return render(request,'signin.html',{'error':'invalid username or password'})
    return render(request,'signin.html')


def candidate(request):
    return render(request,'candidate/candidate.html')
def candidate_profile(request):
    return render(request,'candidate/candidate_profile.html')
def candidate_joblist(request):
    return render(request,'candidate/candidate_joblist.html')
def candidate_applications(request):
    return render(request,'candidate/candidate_applications.html')
def candidate_shortlist(request):
    return render(request,'candidate/candidate_shortlist.html')
def candidate_notification(request):
    return render(request,'candidate/candidate_notification.html')
def candidate_settings(request):
    return render(request,'candidate/candidate_settings.html')

def candidate_details(request):
    return render(request,'candidate/candidate_details.html')




def company(request):
    return render(request,'company/company.html')
def company_profile(request):
    return render(request,'company/company_profile.html')
def post_job(request):
    return render(request,'company/post_job.html')


def admin(request):
    return render(request,'admin.html')