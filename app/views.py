from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Profile,Post,Business
from .forms import NeighbourHoodForm,UpdateUserProfileForm,UploadPostForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    all_hoods = Neighbourhood.objects.all()
    return render(request, 'index.html',{'all_hoods': all_hoods,})


def create_hood(request):
    if request.method == 'POST':
        profile= Profile.objects.get_or_create(user=request.user)
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})

def join_hood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('index')


def leave_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('index')

def single_hood(request,id):
    hood = Neighbourhood.objects.get(id=id)
    posts = Post.objects.filter(hood=hood)
    businesses = Business.objects.filter(neighbourhood = hood.id).all()
    params = {
        'hood': hood,
        'posts':posts,
        'businesses':businesses
    }
    return render(request, 'single_hood.html', params)

def profile(request, id):
    profile= Profile.objects.get_or_create(user=request.user)
    user_prof = Profile.objects.get(id=id)
    return render(request, 'user_profile.html')

def update_profile(request, id):
    user = User.objects.get(id=id)
    profile= Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile= Profile.objects.get_or_create(user=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            prof_form.save()
            return redirect('profile',user.id)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'prof_form': prof_form,})

def hood_post(request, id):
    hood = Neighbourhood.objects.get(id=id)
    if request.method == 'POST':
        profile= Profile.objects.get_or_create(user=request.user)
        form =UploadPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = UploadPostForm()
    return render(request, 'hood_post.html', {'form': form})
