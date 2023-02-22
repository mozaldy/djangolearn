from django.shortcuts import render, redirect, resolve_url
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')
    priority = forms.IntegerField(label='Priority', max_value=10)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session['tasks'] = []
    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasks']
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return redirect(resolve_url('index'))
        else:
            return render(request, 'tasks/add.html', {
                'form': form
            })
    return render(request, 'tasks/add.html', {
        'form': NewTaskForm()
    })