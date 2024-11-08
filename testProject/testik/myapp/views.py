from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.all()
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'myapp/index.html', {'entries': entries, 'form': form})

def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    return redirect('index')
