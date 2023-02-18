from django.shortcuts import render
from django.http import HttpResponse
from .forms import ElectronicsRegistration



def blog(request):
    return render(request, 'electronics/forms1.html')


def show_form(request):
    frm = ElectronicsRegistration(auto_id='emp_%s', label_suffix='', initial={'email': 'shorif@gmail.com'})
    frm.order_fields(field_order=['email',  'rollno', 'last_name' , 'first_name' ,   'batch' ])
    return render (request, 'electronics/forms.html', {'form': frm})
