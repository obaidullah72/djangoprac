from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .forms import AddStudentForm

class Home(View):
    def get(self, request):
        stud_data = Student.objects.all()
        context = {
            'stud_data': stud_data
        }
        return render(request, 'cruduser/home.html', context)


class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        context = {
            'form': fm
        }
        return render(request, 'cruduser/add_student.html', context)
    
    def post(self, request):
        fm = AddStudentForm(request.POST)
        context = {
            'form': fm
        }
        if fm.is_valid():
            fm.save()
            return redirect('cruduser-home')  # This redirects to the home page of the `cruduser` app.
        else:
            return render(request, 'cruduser/add_student.html', context)


class Delete_Student(View):
    def post(self, request):
        data= request.POST
        id = data.get('id')
        studata = Student.objects.get(id = id)
        studata.delete()
        return redirect('cruduser-home')
    
    
    
class Edit_Student(View):
    def get(self, request, id):
        stu = Student.objects.get(id = id)
        fm = AddStudentForm(instance = stu)
        context = {
            'form': fm
        }
        return render(request, 'cruduser/edit_student.html', context)
    
    def post(self, request, id):
        stu = Student.objects.get(id = id)
        fm = AddStudentForm(request.POST, instance=stu)
        if(fm.is_valid):
            fm.save()
            return redirect('cruduser-home')