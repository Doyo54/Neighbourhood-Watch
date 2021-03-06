from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddBussinessForm
from app.models import Business
from app.models import Neighbourhood, Profile

# Create your views here.
@login_required(login_url='Login')
def AddBusiness(request, username):
    profile = User.objects.get(username=username)
    hood = Neighbourhood.objects.all()
    form = AddBussinessForm()
    if request.method == "POST":
        form = AddBussinessForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            neighbourhood = form.cleaned_data['neighbourhood']
            description = form.cleaned_data['description']

            neighbourhood_obj = Neighbourhood.objects.get(pk=int(neighbourhood))
            # member = Membership.objects.filter(user = profile.id, neighbourhood_membership = neighbourhood_obj.id)

            # if not member:
            #     messages.error(request, "⚠️ You Need To Be A Member of The Selected Neighbourhood First!")
            #     return redirect('business:addbusiness', username=username)

        # else:
            new_business = Business(name = name, email = email, neighbourhood = neighbourhood_obj, description = description, owner = request.user.profile)
            new_business.save()

            messages.success(request, '✅ A Business Was Created Successfully!')
            return redirect('single-hood', profile.profile.neighbourhood.id)
        else:
            messages.error(request, "⚠️ A Business Wasn't Created!")
            return redirect('business:addbusiness')
    else:
        form = AddBussinessForm()
    return render(request, 'addbusiness.html', {'form':form})


def Search(request):
    if request.method == 'POST':
        search = request.POST['search']
        print(search)
        businesses = Business.objects.filter(name__icontains = search).all()
        return render(request, 'search.html', {'search':search, 'businesses':businesses})
    else:
        return render(request, 'search.html')

