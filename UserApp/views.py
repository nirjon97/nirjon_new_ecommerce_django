from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib import messages
from Product.models import Product,Category
from base_app.models import Setting
from OrderApp.views import ShopCart,Order,OderProduct
from UserApp.forms import SignUpForm,UserUpdateForm,ProfileUpdateForm
from UserApp.models import UserProfile,wishlist_cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.warning(request, 'Your username or password is invalid.')
    setting = Setting.objects.get(id=1)

    context={
        'setting': setting ,

    }
    return render(request,'user_login.html',context)


def user_logout(request):
    logout(request)
    return redirect('Home')



def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "user_img/avatar.jpg"
            data.save()

            return redirect('Home')
        else:
            messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()
    setting = Setting.objects.get(id=1)
    context = {
               'setting': setting,
               'form': form}
    return render(request, 'user_register.html', context)


#user profile showing function

def userprofile(request):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    user_order= Order.objects.filter(user_id=current_user.id)
    order_product = OderProduct.objects.filter(user_id=current_user.id)

    context = {
               'setting': setting,
               'profile': profile,
               'user_order': user_order,
               'order_product':order_product,
               }
    return render(request, 'user_profile.html', context)



#update profile
@login_required(login_url='/user/login')  # Check login
def user_update(request):
    if request.method == 'POST':
        # request.user is user  data
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('userprofile')
    else:
       # category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        # "userprofile" model -> OneToOneField relatinon with user
        profile_form = ProfileUpdateForm(instance=request.user)
        setting = Setting.objects.get(id=1)
        context = {

            'user_form': user_form,
            'profile_form': profile_form,
            'setting': setting,
        }
        return render(request, 'userupdate.html', context)


#password change showing

@login_required(login_url='/user/login')  # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('userprofile')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('user_password')
    else:
        
        setting = Setting.objects.get(id=1)
        form = PasswordChangeForm(request.user)


    context ={
           'setting':setting,
           'form': form,
    }
    return render(request, 'userpasswordupdate.html', context)


# wishlist details showing
@login_required(login_url='/user/login')
def wishlist_detials(request):
    current_user = request.user
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    wishlist_product = wishlist_cart.objects.filter(user_id=current_user.id)
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        if p.product and p.quantity:
           total_amount += p.product.new_price*p.quantity
    

    context = {
        'category': category,
        'setting': setting,
        'wishlist_product': wishlist_product,
        'cart_product': cart_product,
        'total_amount': total_amount,

    }
    return render(request, 'user_wishlist.html', context)


#wishlist delete
@login_required(login_url='/user/login')
def wishlist_delete(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    wishlist_product = wishlist_cart.objects.filter(id=id, user_id=current_user.id)
    wishlist_product.delete()
    messages.warning(request, 'Your product has been deleted.')
    return HttpResponseRedirect(url)



#user wishlist showing
@login_required(login_url='/user/login')
def add_to_user_wishlist(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = wishlist_cart.objects.filter(
        product_id=id, user_id=current_user.id)
    if checking:
        control = 1
    else:
        control = 0

    # control ==1 means its checking the requesting product.if the requesting product is into our wishlist , we  will return the same url and messageing that you have already add this product in your wishlist.
    if control == 1:

        messages.success(request, 'Your Product  has been already added to your wishlist')
        return HttpResponseRedirect(url)

    else:

        data = wishlist_cart()
        data.user_id = current_user.id
        data.product_id = id
        data.save()

        messages.success(request, 'Your  product has been added to your wishlist')
        return HttpResponseRedirect(url)


    

