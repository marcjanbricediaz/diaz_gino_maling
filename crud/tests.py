from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders, Users

# -------------------------------
# Gender Views
# -------------------------------
def gender_list(request):
    try:
        genders = Genders.objects.all()
        return render(request, 'gender/GenderList.html', {'genders': genders})
    except Exception as e:
        return HttpResponse(f'Error loading genders: {e}')

def add_gender(request):
    try:
        if request.method == 'POST':
            gender = request.POST.get('gender')
            Genders.objects.create(gender=gender)
            messages.success(request, 'Gender Added Successfully!')
            return redirect('/gender/list')
        return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f'Error adding gender: {e}')

# -------------------------------
# User Views
# -------------------------------
def user_list(request):
    try:
        users = Users.objects.select_related('gender').all()
        return render(request, 'user/userList.html', {'users': users})
    except Exception as e:
        return HttpResponse(f'Error loading users: {e}')

def add_user(request):
    try:
        if request.method == 'POST':
            profile = request.FILES.get('profile')
            full_name = request.POST.get('full_name')
            gender_id = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            address = request.POST.get('address')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = make_password(request.POST.get('password'))

            Users.objects.create(
                profile=profile,
                full_name=full_name,
                gender=Genders.objects.get(pk=gender_id),
                birth_date=birth_date,
                address=address,
                contact_number=contact_number,
                email=email,
                username=username,
                password=password
            )
            messages.success(request, 'User Added Successfully!')
            return redirect('/user/list')

        else:
            genders = Genders.objects.all()
            return render(request, 'user/addUser.html', {'genders': genders})

    except Exception as e:
        return HttpResponse(f'Error adding user: {e}')