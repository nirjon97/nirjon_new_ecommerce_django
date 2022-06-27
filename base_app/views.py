from email.policy import HTTP
from unicodedata import category
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Setting,ContactForm,ContactMessage,Newsletter,Newsletter_Form
from Product.models import Product,Category,Comment
from .forms import SearchForm
from OrderApp.views import ShopCart



#function based views
def Home(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        if p.product and p.quantity:
           total_amount += p.product.new_price*p.quantity
           

    


    setting = Setting.objects.get(id=1)
    feature_product = Product.objects.all()
    Contact_message =ContactMessage.objects.filter(status="Read")
    new_product = Product.objects.all().order_by('-id')

    
    context={'setting': setting ,
             'feature_product': feature_product,
             'new_product': new_product,
             'cart_product': cart_product,
             'total_amount': total_amount,
             'Contact_message':Contact_message,
              }

    
    return render(request,"home.html",context)

# gender based category
def gender_category(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity


    setting = Setting.objects.get(id=1)

    context = {
        'setting' : setting,
        'cart_product': cart_product,
        'total_amount': total_amount,
    }

    return render(request,"gender_based_category.html",context)

#men category product
def men_category(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity


    setting = Setting.objects.get(id=1)
    filter_category_men = Category.objects.filter(gender='Male')


    context = {
        'setting' : setting,
        'filter_category_men' : filter_category_men,
        'cart_product': cart_product,
        'total_amount': total_amount,

    }
    
    return render(request,"men_category_product.html",context)


#women category product
def women_category(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity


    setting = Setting.objects.get(id=1)
    filter_category_women = Category.objects.filter(gender='Female')


    context = {
        'setting' : setting,
        'filter_category_women' : filter_category_women,
        'cart_product': cart_product,
        'total_amount': total_amount,

    }

    return render(request,"women_category_product.html",context)

#category product details
def category_product(request,slug):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity


    setting = Setting.objects.get(id=1)
    product=Product.objects.filter(category__slug=slug)
   # category=Category.objects.filter(slug=slug)


    context = {
        'setting' : setting,
        #'category' : category,
        'product' : product,
        'cart_product': cart_product,
        'total_amount': total_amount,


    }

    return render(request,"category_based_product.html",context)

#single product details
def product_details(request,cate_slug,id):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity


    setting = Setting.objects.get(id=1)
    #product=Product.objects.filter(slug =prod_slug).first
    product=Product.objects.get(id=id)
    category=Category.objects.filter(slug=cate_slug)
    comment_show = Comment.objects.filter(product_id=id, status='True')


    context = {
        'setting' : setting,
        'category' : category,
        'product' : product,
        'cart_product': cart_product,
        'total_amount': total_amount,
        'comment_show': comment_show,

    }

    return render(request,"single_product.html",context)


#contact view function


def contact(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Profile details updated.')

            return redirect('contact')

    form = ContactForm
    setting= Setting.objects.get(id=1)

    context = {
        'setting' : setting,
        'form': form,
    }
    return render(request, 'contact_view.html', context)



#search product part

def search_view(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity


        
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            product = Product.objects.filter(title__icontains=query)
            setting = Setting.objects.get(id=1)
            context = {
                'query': query,
                'product': product,
                'setting' : setting,
                'cart_product': cart_product,
                'total_amount': total_amount,

            }
            return render(request, 'category_based_product.html', context)
    return HttpResponseRedirect('category_product')



#subscribe newsleter form submission
def newsletter(request):
    url= request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        form = Newsletter_Form(request.POST)
        if form.is_valid():
            data = Newsletter()
            data.email = form.cleaned_data['email']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            print("its working form")
            messages.success(request, 'Congratulations,You are successfully subscribed')

            return redirect('Home')
    


   

