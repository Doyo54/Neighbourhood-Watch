from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddBussinessForm, AddPostForm
from .models import Business, Post

# Create your views here.
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render (request, 'bigup/project.html', {'form': form, 'current_user': current_user})

@login_required(login_url='Login')
def AddBusiness(request, username):
    user = User.objects.get(username=username)
    form = AddBussinessForm()
    if request.method == "POST":
        form = AddBussinessForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']

            neighbourhood_obj = NeighbourHood.objects.get(pk=int(neighbourhood))
            member = Membership.objects.filter(user = user.id, neighbourhood_membership = neighbourhood_obj.id)

            if not member:
                messages.error(request, "⚠️ You Need To Be A Member of The Selected Neighbourhood First!")
                return redirect('AddBusiness', username=username)

            else:
                neighbourhood_obj = NeighbourHood.objects.get(pk=int(neighbourhood))
                new_business = Business(name = name, email = email, neighbourhood = neighbourhood_obj, description = description, owner = request.user.profile)
                new_business.save()

                messages.success(request, '✅ A Business Was Created Successfully!')
                return redirect('MyBusinesses', username=username)
        else:
            messages.error(request, "⚠️ A Business Wasn't Created!")
            return redirect('AddBusiness')
    else:
        form = AddBussinessForm()
    return render(request, 'addbusiness.html', {'form':form})

@login_required(login_url='Login')
def MyBusinesses(request, username):
    user = User.objects.get(username=username)
    profile_details = Profile.objects.get(user = profile.id)
    businesses = Business.objects.filter(owner = profile.id).all()
    return render(request, 'My Businesses.html', {'businesses':businesses, 'profile_details':profile_details})

@login_required(login_url='Login')
def MyPosts(request, username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(user = profile.id)
    posts = Post.objects.filter(author = profile.id).all()
    return render(request, 'My Posts.html', {'posts':posts, 'profile_details':profile_details})

def Search(request):
    if request.method == 'POST':
        search = request.POST['BusinessSearch']
        print(search)
        businesses = Business.objects.filter(name__icontains = search).all()
        return render(request, 'search.html', {'search':search, 'businesses':businesses})
    else:
        return render(request, 'search.html')

@login_required(login_url='Login')
def AddPost(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user.id)

    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            neighbourhood = form.cleaned_data['neighbourhood']
            category = form.cleaned_data['category']

            neighbourhood_obj = NeighbourHood.objects.get(pk=int(neighbourhood))
            member = Membership.objects.filter(user = profile.id, neighbourhood_membership = neighbourhood_obj.id)

            if not member:
                messages.error(request, "⚠️ You Need To Be A Member of The Selected Neighbourhood First!")
                return redirect('AddPost', username=username)

            else:
                neighbourhood_obj = NeighbourHood.objects.get(pk=int(neighbourhood))
                new_post = Post(title = title, category = category, neighbourhood = neighbourhood_obj, description = description, author = request.user.profile)
                new_post.save()

                messages.success(request, '✅ Your Post Was Created Successfully!')
                return redirect('MyPosts', username=username)
        else:
            messages.error(request, "⚠️ Your Post Wasn't Created!")
            return redirect('AddPost', username=username)
    else:
        form = AddPostForm()
    return render(request, 'AddPost.html', {'form':form})
