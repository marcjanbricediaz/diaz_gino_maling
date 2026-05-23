from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .models import Genders, Users

# --------- Gender CRUD ---------

def gender_list(request):
    try:
        genders = Genders.objects.all()
        data = {
            'genders': genders
        }
        return render(request, 'gender/GenderList.html', data)
    except Exception as e:
        return HttpResponse(f"Error occurred loading genders: {e}")

def add_gender(request):
    if request.method == 'POST':
        gender_name = request.POST.get('gender')
        Genders.objects.create(gender=gender_name)
        messages.success(request, "Gender Added Successfully!")
        return redirect('gender/list/')
    return render(request, 'gender/AddGender.html')

def edit_gender(request, genderId):
    try:
        genderObj = Genders.objects.get(pk=genderId)
        if request.method == 'POST':
            genderObj.gender = request.POST.get('gender')
            genderObj.save()
            messages.success(request, "Gender Updated Successfully!")
            data = {
                'gender': genderObj
            }
            return render(request, 'gender/EditGender.html', data)
        else:
            genderObj = Genders.objects.get(pk=genderId)
            data = {
                'gender': genderObj
            }
            return render(request, 'gender/EditGender.html', data)
    except Exception as e:
        return HttpResponse(f"Error editing gender: {e}")

def delete_gender(request, genderId):
    try:
        genderObj = Genders.objects.get(pk=genderId)
        if request.method == 'POST':
            genderObj.delete()
            messages.success(request, "Gender Deleted Successfully!")

            return redirect('/gender/list/')
        else:
            genderObj = Genders.objects.get(pk=genderId)
            data = {
                'gender': genderObj
            }
            return render(request, 'gender/DeleteGender.html', data)
    except Exception as e:
        return HttpResponse(f"Error deleting gender: {e}")

# --------- User CRUD ---------

def user_list(request):
    try:
        users = Users.objects.select_related('gender')
        data = {
            'users': users
        }
        return render(request, 'user/userList.html', data)
    except Exception as e:
        return HttpResponse(f"Error loading users: {e}")

def add_user(request):
    try:
        if request.method == 'POST':
            profile = request.FILES.get('profile')
            fullname = request.POST.get('full_name')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            address = request.POST.get('address')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')


            if password != confirm_password:
                messages.error(request, 'Passwords do not match!')
                return redirect('add_user')
            
            if len(password) <8:
                messages.error(request, 'Passwords must be at least 8 characters!')
                return redirect('add_user')




            Users.objects.create(
                full_name=fullname,
                gender= Genders.objects.get(pk=gender),
                birth_date=birth_date,
                address=address,
                contact_number=contact_number,
                email=email,
                username=username,
                password=password,
                profile=profile
            )
            messages.success(request, "User Added Successfully!")
            return redirect('user_list')
        else:
            gender_list = Genders.objects.all()
            data = {
                'genders': gender_list
            }
            return render(request, 'user/addUser.html', data)
    except Exception as e:
        return HttpResponse(f'somethin occured during adding new user {e}')
    
def edit_user(request, userId):
    try:
        if request.method == 'POST':
            userObj = Users.objects.get(pk=userId)

            profile = request.FILES.get('profile')
            fullname = request.POST.get('full_name')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            address = request.POST.get('address')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')

            userObj.full_name = fullname
            userObj.gender = Genders.objects.get(pk=gender)
            userObj.birth_date = birth_date
            userObj.address = address
            userObj.contact_number = contact_number
            userObj.email = email
            userObj.username = username
            userObj.profile = profile
            userObj.save()

            messages.success(request, 'User updated Successfully')
            data = {
                'user': userObj
            }
            return render(request, 'user/editUser.html', data)
        else:
            userObj = Users.objects.get(pk=userId)
            gender = Genders.objects.all()
            data = {
                'user': userObj,
                'genders': gender
            }
            return render(request, 'user/editUser.html', data)


    except Exception as e:
        return HttpResponse(f'Something occured during edit user {e}')
        