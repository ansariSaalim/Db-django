from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# def home(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('all_students')
#     else:
#         form = StudentForm()

#     return render(request, 'home.html', {'form': form})


def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # print("Form saved successfully")  # Add debugging statement
            return redirect('all_students')
        else:
            print("Form is not valid:", form.errors)  # Add debugging statement
    else:
        form = StudentForm()

    return render(request, 'home.html', {'form': form})


def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html', {'students': students})