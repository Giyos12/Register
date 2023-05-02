from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from auth2.models import Student, Token
from auth2.forms import StudentForm, LoginForm, StudentEditForm, ResetPasswordForm, NewPasswordForm
from auth2.service import toke_gen_uniqe


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
                    return redirect('profile')
            return render(request, 'login.html', {'form': form})
        return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', context={'form': form})


def home(request):
    return HttpResponse('home page')


def _logout(request):
    logout(request)
    return HttpResponse('successfully logout')


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StudentEditForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                Student.objects.filter(username=cd['username']).update(
                    username=cd['username'],
                    email=cd['email'],
                    subject=cd['subject'],
                    phone_number=cd['phone_number'],
                )
                return redirect('login')
            return render(request, 'profile.html', {'form': form})
        form = StudentEditForm(
            initial={
                "username": request.user.username,
                "email": request.user.email,
                "subject": request.user.subject,
                "phone_number": request.user.phone_number,
            }
        )
        return render(request, 'profile.html', {'form': form})
    return redirect('login')


def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = Student.objects.filter(username=cd['username']).first()
            if user:
                if user.email == cd['email']:
                    token = toke_gen_uniqe()
                    send_mail(
                        subject='Activation link',
                        message=f'Activation link: http://localhost:8000/verify/?token={token}',
                        from_email='giyosoripov4@gmail.com',
                        recipient_list=['giyosoripov4@gmail.com'],
                        fail_silently=False
                    )
                    token = Token(token=token, user=user)
                    token.save()
                    print(token.token)
                    return render(request, "reset_dane.html", {'have': True, 'user': user})
                return render(request, "reset_dane.html", {'have': False})
            form.add_error('username', "databaseda bunaqangi usernamelik user mavjud emas")
            return render(request, 'reset_password.html', {'form': form})
        return render(request, 'reset_password.html', {'form': form})
    else:
        form = ResetPasswordForm()
        return render(request, 'reset_password.html', {'form': form})


def new_password(username, password):
    user = Student.objects.filter(username=username)
    user.update(password=make_password(password))


def new_password_page(request, user):
    if request.method == "POST":
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['re_password']:
                new_password(username=user.username, password=cd['password'])
                return redirect('login')
            form.add_error('password', "ikkta password bir emas")
            return render(request, "new_password.html", {"form": form})
        return render(request, "new_password.html", {"form": form})
    else:
        form = NewPasswordForm()
        return render(request, "new_password.html", {"form": form})


def verify(request):
    _token = request.GET.get("token")
    token = Token.objects.get(token=_token)
    if token:
        user = token.user
        return new_password_page(request, user)
    return HttpResponse('this token is invalid')
