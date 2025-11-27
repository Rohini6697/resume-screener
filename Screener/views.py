from .models import Candidates, Company, Job, Profile
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
                    try:
                        company = user.profile.company
                        return redirect('company')
                    except Company.DoesNotExist:
                        return render(request,'company/company_details.html')
        else:
            return render(request,'signin.html',{'error':'invalid username or password'})
    return render(request,'signin.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def candidate(request):
    return render(request,'candidate/candidate.html')
def candidate_profile(request):
    return render(request,'candidate/candidate_profile.html')
def candidate_joblist(request):
    jobs = Job.objects.all()
    return render(request,'candidate/candidate_joblist.html',{'jobs':jobs})
def candidate_applications(request):
    return render(request,'candidate/candidate_applications.html')
def candidate_shortlist(request):
    return render(request,'candidate/candidate_shortlist.html')
def candidate_notification(request):
    return render(request,'candidate/candidate_notification.html')
def candidate_settings(request):
    return render(request,'candidate/candidate_settings.html')
def view_job(request):
    return render(request,'candidate/view_job.html')

@login_required
def candidate_details(request, candidate_id):

    # Get the profile of the logged-in user
    user_profile = get_object_or_404(Profile, id=candidate_id)

    # Create or get candidate details
    candidate, created = Candidates.objects.get_or_create(user=user_profile)

    if request.method == "POST":
        # Basic fields
        candidate.full_name = request.POST.get("fullname")
        candidate.phone = request.POST.get("phone")
        candidate.gender = request.POST.get("gender")
        candidate.work_type = request.POST.get("work_type")
        candidate.preferred_location = request.POST.get("preferred_location")
        candidate.skills = request.POST.get("skills")
        candidate.experience = request.POST.get("experience")

        # File upload (resume)
        if "resume" in request.FILES:
            candidate.resume = request.FILES["resume"]

        candidate.save()
        return redirect("candidate")  # Go to candidate dashboard after saving

    return render(request, "candidate/candidate_details.html", {
        "candidate": candidate
    })



def company(request):
    return render(request,'company/company.html')
def company_profile(request):
    return render(request,'company/company_profile.html')
@login_required
def post_job(request):
    # Get company profile of the logged-in user
    try:
        company = Company.objects.get(user=request.user.profile)
    except Company.DoesNotExist:
        messages.error(request, "You must create a company profile before posting jobs.")
        return redirect("company_profile")

    if request.method == "POST":
        title = request.POST.get("title")
        location = request.POST.get("location")
        job_type = request.POST.get("job_type")
        experience_type = request.POST.get("experience_type")

        # Experience fields (only if experienced)
        min_experience = request.POST.get("min_experience")
        max_experience = request.POST.get("max_experience")

        # Salary fields
        min_salary = request.POST.get("min_salary")
        max_salary = request.POST.get("max_salary")

        skills = request.POST.get("skills")
        description = request.POST.get("description")

        # Create job object
        job = Job(
            company=company,
            title=title,
            location=location,
            job_type=job_type,
            experience_type=experience_type,
            skills=skills,
            description=description,
            min_salary=min_salary or None,
            max_salary=max_salary or None
        )

        # Only save experience range if experienced
        if experience_type == "Experienced":
            job.min_experience = min_experience or None
            job.max_experience = max_experience or None

        job.save()

        messages.success(request, "Job posted successfully!")
        return redirect("company")  
    return render(request,'company/post_job.html')



def company_details(request, company_id):
    # Get profile of logged-in company
    user_profile = get_object_or_404(Profile, id=company_id)

    # Create or return existing company record
    company, created = Company.objects.get_or_create(user=user_profile)

    if request.method == "POST":

        company.name = request.POST.get("name")
        company.website = request.POST.get("website")
        company.industry = request.POST.get("industry")
        company.size = request.POST.get("size")
        company.location = request.POST.get("location")
        company.about = request.POST.get("about")
        company.linkedin = request.POST.get("linkedin")
        company.twitter = request.POST.get("twitter")
        if "logo" in request.FILES:
            company.logo = request.FILES["logo"]

        company.save()

        return redirect("company") 

    return render(request, "company/company_details.html", {
        "company": company
    })


def admin(request):
    return render(request,'admin.html')

def job_list(request):
    company = Company.objects.get(user=request.user.profile)
    jobs = Job.objects.filter(company=company).order_by('-id')
    return render(request,'company/job_list.html',{'jobs':jobs})




