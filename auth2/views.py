from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from auth2.models import Student
from auth2.forms import StudentForm, LoginForm


# Create your views here.
def register(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['re_password']:
                s1 = Student(
                    username=form.cleaned_data.get('username'),
                    email=form.cleaned_data.get('email'),
                    subject=form.cleaned_data.get('subject'),
                    password=(form.cleaned_data.get('password')))
                s1.save()
                return redirect('login')
            form.add_error("password", "bir xil emas")
        return render(request, "register.html", {"form": form})
    return render(request, 'register.html', {'form': form})


def _login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # print(cd)
            # try:
            #     user = Student.objects.get(username=cd['username'])
            #     if check_password(cd['password'], user.password):
            #         user = user
            #     else:
            #         user = None
            #         form.add_error('password', "bu userning password siz kirtgandan boshqacharoq")
            # except Student.DoesNotExist:
            #     user = None
            #     form.add_error('bunaqa usernamelik user mavjud emas db da')

            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'], )

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
            return render(request, 'login.html', {'form': form})
        return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', context={'form': form})


def home(request):
    return HttpResponse('home page')


def _logout(request):
    logout(request)
    return HttpResponse('successfully logout')
