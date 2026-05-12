from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders, Users
# Create your views here.


def gender_list(request):
    try:
        genders = Genders.objects.all()
        data = {
            'genders': genders
        }
        return render(request, 'gender/GenderList.html', data)
    except Exception as e:
        return HttpResponse(f'Error occured during load genders {e}')


def add_gender(request):
    try:
        if request.method == 'POST':
            gender = request.POST.get('gender')
            Genders.objects.create(gender=gender).save()
            messages.success(request, 'Gender Added Successfully!')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f'Error occured during the add Gender: {e}')
    
def edit_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj =  Genders.objects.get(pk=genderId)

            gender = request.POST.get('gender')

            genderObj.gender = gender
            genderObj.save()

            data = {
                'gender': genderObj
            }
 
            messages.success(request, 'Gender updated Succesfully!')
            return render (request, 'gender/EditGender.html', data) 
        else:    
            genderObj =  Genders.objects.get(pk=genderId)

            data = {
                'gender': genderObj
            } 

            return render(request,'gender/EditGender.html', data)
      
    except  Exception as e:
        return HttpResponse(f'Error occurred during edit gender: {e}')    
    
def delete_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj = Genders.objects.get(pk=genderId)
            genderObj.delete()

            messages.success(request, 'Gender Deleted Successfully!')
            return redirect('/gender/list')
        else:
            genderObj = Genders.objects.get(pk=genderId)
            data = {
                'gender': genderObj
            }
            return render(request, 'gender/DeleteGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error occured during delete gender {e}')
    
# crud for users

def user_list(request):
    try:
        userObj = Users.objects.select_related('gender')
        data = {
            'users': userObj
        }
        return render(request, 'user/userList.html', data)
    except Exception as e:
        return HttpResponse(f'Something Occured during load Users: {e}')


def add_user(request):
    try:
        if request.method == 'POST':
            fullname = request.POST.get('full_name')
            gender = request.POST.get('gender')
            birthDate = request.POST.get('birthDate')
            address = request.POST.get('address')
            contactNumber = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            hashedPassword = make_password(password)
            confirmPassword = request.POST.get('confirm_password')
            print("Gender ID received:", gender)
            print("Available genders:", Genders.objects.all().values())
            Users.objects.create(
                full_name = fullname,
                gender = Genders.objects.get(pk=gender),
                birth_date = birthDate,
                address = address,
                contact_number = contactNumber,
                email = email,
                username = username,
                password = hashedPassword
            ).save()

            messages.success(request, 'User Added Successfully!')
            return redirect('/user/add')

        else:

            genderObj = Genders.objects.all()
            data = {
                'genders': genderObj
            }
            return render(request, 'user/addUser.html', data)
    except Exception as e:
        return HttpResponse(f'Something occurred during add gender: {e}')