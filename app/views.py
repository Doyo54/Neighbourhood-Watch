from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    all_hoods = Neighbourhood.objects.all()
    return render(request, 'index.html',{'all_hoods': all_hoods,})
