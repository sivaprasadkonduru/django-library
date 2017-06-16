from django.shortcuts import render

# Create your views here.

# views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from forms import *
from models import *

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    all_books = Books.objects.all()

    category = set(all_books.values_list('category', flat=True))

    return render_to_response(
        'home.html',
        {'user': request.user, 'books': all_books, 'category': category}
    )
    # code to deal with the "Add" form

@csrf_exempt
def get_categories(request):

    '''This could be your actual view or a new one'''
    # Your code
    #import pdb;
    #pdb.set_trace()
    if request.method == 'POST': # If the form is submitted
        selected_value = request.POST['dropdown']
        data = Books.objects.filter(category=selected_value)

    return render_to_response('get_categories.html',
        {'user': request.user, 'data': data})

