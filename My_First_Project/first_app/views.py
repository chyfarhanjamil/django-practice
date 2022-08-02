from django.shortcuts import render, redirect
from first_app.forms import StudentsForm
from first_app.models import Students

# Create your views here.


def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = StudentsForm()
    return render(request, 'index.html', {'form': form})


def view(request):
    students = Students.objects.order_by("f_name")
    return render(request, 'view.html', {'students': students})


def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect("/")


def edit(request, id):
    students = Students.objects.get(id=id)
    return render(request, 'edit.html', {'students': students})


def update(request, id):
    students = Students.objects.get(id=id)

    form = StudentsForm(request.POST or None, instance=students)

    if form.is_valid():
        form.save()
        return redirect('/')

    else:
        form = StudentsForm()
    return render(request, 'index.html', {'form': form})
