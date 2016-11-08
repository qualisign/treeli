
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from models import User, Leaf, Twig, Branch, Trunk, Tree, Drawing
from trytreeli.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/app/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account has been disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details provided.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})
    
def search(reqeust):
    form = forms.SearchForm()
    return render(request, 'search.html', {'form' : form})
    
def index(request):
    if request.method != 'POST':
        return render(request, 'index.html')
    else:
        if request.is_ajax():
            if request.POST.get('userName'):
                user_name=request.POST.get('userName')
                user=User.objects.get(user_name=user_name)
            else:
                user=None

            if request.POST.get("mode") == "grow":
                    
                parent = request.POST.get('parent')
                child = request.POST.get('child')
                
                # case 1: parent already trunk -- create branch from child
                try:
                    trunk = Trunk.objects.get(text=parent)
                    drawing = trunk.drawing                    
                    if trunk:
                        try:
                            branch = Branch.objects.get(text=child)
                            data = {"already" : True,
                                    "parent" : parent,
                                    "child" : child
                            }
                            return JsonResponse(data)
                        except Branch.DoesNotExist:                            
                            branch = Branch(text=child, trunk=trunk)
                            branch.save()
                            branch.get_tips()
                            data = drawing.get_data()
                            if trunk.branch_set.count() > 1:
                                data["tree?"] = trunk.text
                                branch.stage = "filled"
                                branch.save()
                            return JsonResponse(data)
                        # display message saying that this combo already exists.
                                
                except Trunk.DoesNotExist:
                    # case 2: parent already branch -- create twig from child
                    print("trying case 2")
                    try:
                        branch = Branch.objects.get(text=parent)
                        drawing = branch.trunk.drawing
                        if branch:
                            try:
                                twig = Twig.objects.get(text=child)
                                data = {"already" : True,
                                        "parent" : parent,
                                        "child" : child
                                }
                                return JsonResponse(data)
                            except Twig.DoesNotExist:
                                twig = Twig(text=child, branch=branch)                        
                                twig.save()
                                twig.get_tips()
                                data = drawing.get_data()
                                if branch.trunk.branch_set.count() > 1:
                                    data["tree?"] = branch.trunk.text
                                    twig.stage = "filled"
                                    twig.save()
                                return JsonResponse(data)
                                
                    except Branch.DoesNotExist:
                        # case 3: parent already twig -- create leaf from child
                        print("trying case 3")
                        try:
                            twig = Twig.objects.get(text=parent)
                            drawing = twig.branch.trunk.drawing
                            if twig:
                                try:
                                    leaf = Leaf.objects.get(text=child)
                                    leaf.twigs.add(twig)
                                    leaf.save()
                                    leaf.get_tips(parent)
                                    data = drawing.get_data()
                                    return JsonResponse(data)
                                except Leaf.DoesNotExist:                                    
                                    leaf = Leaf(text=child)
                                    leaf.save()
                                    leaf.twigs.add(twig)
                                    leaf.save()
                                    leaf.get_tips(parent)
                                    data = drawing.get_data()
                                    if twig.branch.trunk.branch_set.count() > 1:
                                        data["tree?"] = twig.branch.trunk.text
                                        leaf.stage = "filled"
                                        leaf.save()
                                    return JsonResponse(data)
                                
                        except Twig.DoesNotExist:
                            # case 4: neither child nor parent saved to tree -- 
                            # create branch from child and trunk from parent
                            print("trying case 4")
                            trunk = Trunk.objects.create(text=parent)
                            branch = Branch.objects.create(text=child)
                            branch.get_tips()
                            branch.trunk = trunk
                            branch.save()
                            drawing = Drawing.objects.create(text=parent, trunk=trunk)
                            data = drawing.get_data()
                            trunk.stage = "filled"
                            trunk.save()
                            branch.stage = "filled"
                            branch.save()
                            return JsonResponse(data)

            elif request.POST.get("mode") == "prompt":
                trunk_name = request.POST.get("trunkName")
                trunk = Trunk.objects.get(text=trunk_name)  
                try:
                    tree = Tree.objects.get(name=trunk_name)
                    tree.rank_twigs()
                    tree.save()
                    sorted_twigs = Twig.objects.order_by('-rank').filter(tree=tree)
                    current_twig = sorted_twigs[tree.twigs_learned]
                    print("current twig is " + current_twig.text)
                    data = { "twig" : current_twig.text }
                    return JsonResponse(data)                    
                except Tree.DoesNotExist:
                    tree = Tree(name=trunk_name, trunk=trunk)
                    tree.rank_twigs()
                    tree.save()
                    sorted_twigs = Twig.objects.order_by('-rank').filter(tree=tree)
                    current_twig = sorted_twigs[tree.twigs_learned]
                    data = { "twig" : current_twig.text }
                    return JsonResponse(data)
                    
            elif request.POST.get("mode") == "remind":
                trunk_name = request.POST.get("trunkName")
                tree = Tree.objects.get(name=trunk_name)
                sorted_twigs = Twig.objects.order_by('-rank').filter(tree=tree)
                current_twig = sorted_twigs[tree.twigs_learned]
                tries = request.POST.get("tries").strip(',')
                for leaf in current_twig.leaf_set.all():
                    if leaf.text in tries:
                        leaf.learned = True
                        leaf.save()
                total_count = current_twig.leaf_set.count()
                learned_count = current_twig.leaf_set.all().filter(learned=True).count()
                if total_count == learned_count:
                    tree.twigs_learned += 1
                    tree.save()
                    current_twig = sorted_twigs[tree.twigs_learned]
                    data = {"twig" : current_twig.text}
                    return JsonResponse(data)
                else:
                    missed_leaf = current_twig.leaf_set.all().filter(learned=False)[0]
                    print("missed leaf is: " + missed_leaf.text)
                    next_twigs_list = [i.text for i in missed_leaf.twigs.all()[1:missed_leaf.reminders+1]]
                    print(next_twigs_list)
                    
                    next_twigs = map(lambda x: " AND " + x, next_twigs_list) 
                    data = {"miss" : current_twig.text, "next_twigs" : next_twigs}
                    missed_leaf.reminders += 1
                    missed_leaf.save()
                    return JsonResponse(data)
                    
            elif request.POST.get("mode") == "check":
                to_check = request.POST.get("toCheck")
                try:
                    matching_leaf = current_twig.leaf_set.get(text=to_check)
                    next_leaf = current_twig.misses[indexofmissedleaf+1]
                    other_twigs = request.POST.get(nextTwigs)
                    next_leaf_next_twigs = [i.text for i in next_leaf.twigs[0:missed_leaf.reminders]]
                    if other_twigs in [twig.text for i in matching_leaf.twigs]:
                        # user successfully remembered missed leaf she was reminded of. go on
                        # to next leaf...
                        matching_leaf.learned = True
                        matching_leaf.save()
                        current_twig.misses.remove(matching_leaf)
                        data = { "miss" : next_leaf.text, "next_twigs" : next_leaf_next_twigs }
                        return JsonResponse(data)
                except matching_leaf.DoesNotExist:
                    # user failed to remember missed leaf she was reminded of.
                    # give another reminder, unless she has exhausted them all...
                    missed_leaf = current_twig.misses[0]
                    next_twigs = [i.text for i in missed_leaf.twigs[0:missed_leaf.reminders]]
                    data = { "miss" : current_twig, "next_twigs" : [i.text] }
                    return JsonResponse(data)    
                        
        else:        
            print("request wasn't ajax")
            return render(request, 'index.html')
   
def profile(request, username):
    return HttpResponse(username)

                    






        