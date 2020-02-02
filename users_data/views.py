from django.shortcuts import render, redirect
from .models import UserDetails
from .forms import CreateUserForm

# Create your views here.
def create_user_view(request):
    user_obj = UserDetails.objects.all()
    form = CreateUserForm()
    template = "create.html"
    context = {
        "form"  : form,
        'users' : user_obj,
    }

    if request.method == "POST":
        form = CreateUserForm(request.POST or None)
        if form.is_valid:
            username = form.data['username']
            password = form.data['password']
            email    = form.data['email']

            print(username)
            print(password)
            print(email)

            exists = False
            
            for user in user_obj:
                if user.username == username and user.password == password and user.email == email:
                    #User object already exists
                    exists = True
            
            form = CreateUserForm()
            if exists:
                context['exits'] = True
                return redirect("create")

            new_user = UserDetails.objects.create(
                username = username,
                password = password,
                email    = email,
            )
            new_user.save()
            return redirect("create")

    return render(request, template, context)


