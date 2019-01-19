from django.shortcuts import render
from kjp_app.forms import AddClientsForm
from kjp_app.models import AddClientsModel
from kjp_app import templatetags

# Create your views here.

def home(request):
    return render(request,'kjp_app/home.html')

def add_clients(request):
    form = AddClientsForm()

    if request.method == 'POST':
        form = AddClientsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('Form is invalid')

    return render(request,'kjp_app/add_clients.html',{'form':form})

def view_clients(request):
    client_list = AddClientsModel.objects.order_by('client_name')
    client_dict = {'client_rec': client_list}
    return render(request,'kjp_app/view_clients.html',context=client_dict)
