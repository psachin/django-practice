from datetime import datetime

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# import models
from rango.models import Category, Page

# forms
from rango.forms import CategoryForm, PageForm
from rango.forms import UserForm, UserProfileForm

def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

def register(request):
    if request.session.test_cookie_worked():
        print ">>>> TEST COOKIE WORKED"
        request.session.delete_test_cookie()
        
    cat_list = get_category_list()
    context = RequestContext(request)
    # A boolean value for telling the template whether the
    # registration was successful.  Set to False initially. Code
    # changes value to True when registration succeeds.
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.  Since we need to
            # set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid
            # integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?  If so, we need
            # to get it from the input form and put it in the
            # UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration
            # was successful.
            registered = True
            
        
        # Invalid form or forms - mistakes or something else?  Print
        # problems to the terminal.  They'll also be shown to the
        # user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm
    # instances.  These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response( 
        'rango/register.html', 
        {'user_form': user_form, 
         'profile_form': profile_form, 
         'registered': registered,
         'cat_list':cat_list}, 
        context)
    
def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {'cat_list':cat_list}
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            context_dict['bad_details'] = True
            return render_to_response('rango/login.html', context_dict, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('rango/login.html', context_dict, context)



@login_required
def profile(request):
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {'cat_list': cat_list}
    u = User.objects.get(username=request.user)

    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render_to_response('rango/profile.html', context_dict, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Like before, obtain the request's context.
    context = RequestContext(request)

    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rango/')

def index(request):
    request.session.set_test_cookie()
    context = RequestContext(request)
    
    cat_list = get_category_list()

    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    category_list = Category.objects.order_by('-likes')[:5]
    category_most_views = Category.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list,
                    'category_most_views': category_most_views}

    context_dict['cat_list'] = cat_list

    for category in category_list:
        category.url = encode_url(category.name)

    for category in category_most_views:
        category.url = encode_url(category.name)
        
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    #### NEW CODE ####
    if request.session.get('last_visit'):
        # The session has a value for the last visit
        last_visit_time = request.session.get('last_visit')
        visits = request.session.get('visits', 0)

        if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
            request.session['visits'] = visits + 1
    else:
        # The get returns None, and the session does not have a value for the last visit.
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = 1
    #### END NEW CODE ####
    
    return render_to_response('rango/index.html', context_dict, context)
    

def category(request, category_name_url):
    context = RequestContext(request)
    cat_list = get_category_list()
    # Change underscores in the category name to spaces.  URLs don't
    # handle spaces well, so we encode them as underscores.  We can
    # then simply replace the underscores with spaces again to get the
    # name.
    category_name = decode_url(category_name_url)

    # Create a context dictionary which we can pass to the template
    # rendering engine.  We start by containing the name of the
    # category passed by the user.
    context_dict = {'category_name': category_name,
                    'cat_list':cat_list}
    
    try:
        category = Category.objects.get(name=category_name)
        
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)
        
        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['category_name_url'] = category_name_url
    except Category.DoesNotExist:
        pass
        
    return render_to_response('rango/category.html', context_dict, context)

@login_required
def add_category(request):
    # Get the context from the request.
    context = RequestContext(request)
    cat_list = get_category_list()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # No form passed - ignore and keep going.
            pass
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()
        
    context_dict = {'form': form,
                    'cat_list':cat_list}
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('rango/add_category.html', context_dict, context)

@login_required
def add_page(request, category_name_url):
    context = RequestContext(request)
    cat_list = get_category_list()
    category_name = decode_url(category_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            # this time just save the form, but not commit.
            page = form.save(commit=False)

             # Retrieve the associated Category object so we can add it.
            cat = Category.objects.get(name=category_name)
            page.category = cat

            # Also, create a default value for the number of views.
            page.views = 0

            # With this, we can then save our new model instance.
            page.save()

            # Now that the page is saved, display the category instead.
            return category(request, category_name)
        else:
            print form.errors
    else:
        form = PageForm()
        

    context_dict = {'category_name_url':category_name_url,
                    'category_name':category_name,
                    'form':form,
                    'cat_list':cat_list}
    
    return render_to_response('rango/add_page.html', context_dict, context)
            
@login_required
def restricted(request):
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {}
    context_dict['username'] = request.user
    context_dict['message'] = "Since you're logged in, you can see this text!"
    context_dict['cat_list'] = cat_list

    return render_to_response('rango/restricted.html', context_dict, context)

def get_category_list():
    cat_list = Category.objects.all()
    for cat in cat_list:
        cat.url = encode_url(cat.name)
    return cat_list

def about(request):
    context = RequestContext(request)
    cat_list = get_category_list()

    if request.session['visits']:
        count = request.session['visits']
    else:
        count = 0

    context_dict = {'visits': count,
                    'cat_list':cat_list}        
    # remember to include the visit data
    return render_to_response('rango/about.html', context_dict, context)

