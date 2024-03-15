from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Member
# Create your views here.
def dashboard(request):

    members = Member.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        mymember = Member.objects.create(name=name, email=email)
        mymember.save()
        messages.success(request, 'Member Added successfully !!')
        return redirect('/')
    else:
        context = {
            'members':members
        }
    return render(request, 'dashboard.html', context)

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    messages.success(request, 'Member Deleted !!')
    return redirect('/')

def edit(request, id):
    member = Member.objects.get(id = id)
    print(member)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        member.name = name
        member.email = email
        member.save()
        return redirect('/')
        
    context = {
        'member':member
    }
    return render(request, 'edit.html', context)


@login_required
def view(request, id):
    member = Member.objects.get(id = id)
    context = {
        'member':member
    }
    if request.user.is_superuser:
        return render(request, 'view.html', context)
    else:
        return HttpResponse('<h1>You dont have access to view this Page!!</h1>')
    
