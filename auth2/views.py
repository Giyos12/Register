from django.shortcuts import render

from auth2.models import Student
from auth2.forms import StudentForm


# Create your views here.
def register(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            s1 = Student(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                subject=form.cleaned_data.get('subject'),
                password=form.cleaned_data.get('password1'),
            )
            s1.save()
            return render(request, "register.html")
        return render(request, "register.html", {"form": form})

        #     username = request.POST.get('username')
        #     email = request.POST.get('email')
        #     subject = request.POST.get('subject')
        #     password1 = request.POST.get('password1')
        #     password2 = request.POST.get('password2')
        #     if password2 == password1:
        #         s1 = Student(username=username, email=email, subject=subject, password=password1)
        #         s1.save()
    return render(request, 'register.html', {'form': form})
