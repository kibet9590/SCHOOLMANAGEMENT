from django.shortcuts import render, redirect, get_object_or_404

from school.models import Course,Trainer,Announcement
# Create your views here.

def course(request):
    courses = Course.objects.all()
    return render(request, 'courses.html' , {'courses':courses})

def add_course(request):
       if request.method == 'POST':
           title = request.POST['title']
           description = request.POST['description']
           duration = request.POST['duration']
           # quantity = request.POST['quantity']
           # price = request.POST['price']
           # description = request.POST['description']



           Course.objects.create(title=title,description=description,duration=duration)
           return redirect('courses')
       return render(request, 'add_course.html')

def delete_course(request,id):
    course = get_object_or_404(Course,id=id)
    course.delete()
    return redirect('courses')

def announcement(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements.html', {'announcements':announcements})


def add_announcement(request):
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        date_posted= request.POST['date_posted']
        Announcement.objects.create(title=title,message=message,date_posted=date_posted)
        return redirect('announcements')
    return render(request, 'add_announcement.html')


def delete_announcement(request,id):
    announcement = get_object_or_404(Announcement,id=id)
    announcement.delete()
    return redirect('announcements')

def trainer(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers':trainers})
def add_trainer(request):
    if request.method == 'POST':
        name = request.POST['name']
        bio = request.POST['bio']
        experience = request.POST['experience']
        Trainer.objects.create(name=name,bio=bio,experience=experience)
        return redirect('trainers')
    return render(request, 'add_trainer.html')


def delete_trainer(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    trainer.delete()
    return redirect('trainers')
