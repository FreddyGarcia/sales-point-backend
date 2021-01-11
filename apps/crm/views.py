from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect

def redirect_to_api(request):
    return redirect('/api/v1/crm')
