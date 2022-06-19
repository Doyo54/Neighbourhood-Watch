from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood
from .forms import NeighbourHoodForm

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    all_hoods = Neighbourhood.objects.all()
    return render(request, 'index.html',{'all_hoods': all_hoods,})


def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('ndex')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})
