from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def home(request):
    # if request.user.is_authenticated:
    #     return render(request, 'decasite/dashboard.html')
    return render(request, 'decasite/home.html')

@login_required
def dashboard(request):
    return render(request, 'decasite/dashboard.html')

@login_required
def resources(request):
    return render(request, 'decasite/resources.html')

def loginscreen(request):
    return render(request, 'decasite/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'decasite/login.html')


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))

def join(request):
    return render(request, 'decasite/join.html')

def new_event_page(request):
    return render(request, 'decasite/new_event_page.html')

def update_event(request):
    if request.method == 'POST':
        new_event = request.POST.get('event')
        user = request.user  # Fetch the current logged-in user

        # Update the email
        user.event = new_event
        user.save()  # Save the changes

        return redirect('dashboard')  # Redirect to a success page

    return render(request, 'update_event.html')  # Render the email update form

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def attendance_page(request):
    return render(request, 'decasite/attendance.html')

@login_required
@user_passes_test(is_superuser)
def mark_attendance(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    username = request.POST.get('user')  # Fetch the current logged-in user
    print(username)
    # Update the email
    user = User.objects.get(username=username)
    user.meetings_attended += 1
    user.save()  # Save the changes

    return redirect('dashboard')  # Redirect to a success page


from django.shortcuts import render

def makeUserPage(request):
    return render(request, 'decasite/newUser.html')

def createUser(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    firstName = request.POST.get('firstname', None)
    lastName = request.POST.get('lastname', None)
    username = firstName + lastName
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    # meetings_attended = request.POST.get('meetings_attended', None)
    cohort = request.POST.get('cohort', None)
    event = request.POST.get('event', None)
    tshirt = request.POST.get('tshirt', None)
    grade = request.POST.get('grade', None)
    # decaid = request.REQUEST.get('username', None)

    #undisplayed info
    cell_phone = request.POST.get('cell_phone', None)
    parent_first_name = request.POST.get('parent_first_name', None)
    parent_last_name = request.POST.get('parent_last_name', None)
    parent_cell = request.POST.get('parent_cell', None)
    parent_email = request.POST.get('parent_email', None)
    address = request.POST.get('address', None)
    city = request.POST.get('city', None)
    zipcode =  request.POST.get('zipcode', None)
    partners = request.POST.get('partners', None)
    bloodtype = request.POST.get('bloodtype', None)
    physician = request.POST.get('physician', None)
    physicianPhone = request.POST.get('physicianPhone', None)
    physicianAddress = request.POST.get('physicianAddress', None)
    insurance_number = request.POST.get('insurance_number', None)
   
    user = User.objects.create_user(username=username,
                                    email=email,
                                    password=password, 
                                    meetings_attended = 0,
                                    cohort = cohort,
                                    event = event,
                                    tshirt = tshirt,
                                    grade = grade,
                                    decaid = '',
                                    #undisplayed info
                                    cell_phone = cell_phone,
                                    parent_first_name = parent_first_name,
                                    parent_last_name = parent_last_name,
                                    parent_cell = parent_cell,
                                    parent_email =parent_email,
                                    address = address,
                                    city = city,
                                    zipcode =  zipcode,
                                    partners = partners,
                                    bloodtype = bloodtype,
                                    physician = physician,
                                    physicianPhone = physicianPhone,
                                    physicianAddress = physicianAddress,
                                    insurance_number = insurance_number

                                                                
                                 
                                 )
    print(f"{user} created")
    user.is_active = 'False'
    user.save()


    return render(request,'decasite/processing.html')