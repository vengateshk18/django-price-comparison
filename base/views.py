from imaplib import _Authenticator
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.contrib.auth import logout as auth_logout  
from . import process
def home(request):
    flipkart=[]
    update=False
    if request.method=='POST' and request.user.is_authenticated:
        product_name=request.POST.get('product_name')
        flipkart=search(request,product_name)
      #  print(flipkart)
        update=True
    return render(request,'home.html',{'products': flipkart, 'update': update})
def email(request):
    if request.method=='POST':
        username=request.POST['username']
        subject=request.POST['title']
        message=request.POST['message']
        email_from=settings.EMAIL_HOST_USER
        recipient_list=request.POST['email']
        send_mail(subject,message,email_from,recipient_list)
        return redirect('home')
    return render(request,'email.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import UserProfileForm  # Import your user registration form

def signup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request,user)
            # Send a "Thanks for your registration" email
            subject = 'Registration Successful'
            message = 'Thanks for registering with us. Your account has been created.'
            from_email = 'vengateshk18@hotmail.com'  # Change to your email
            to_email = form.cleaned_data.get('email')
            send_mail(subject, message, from_email, [to_email])
            messages.success(request, 'Registration successful! A confirmation email has been sent.')
            return redirect('home')  # Replace 'login' with your login page URL
        else:
            messages.error(request, 'Error in registration. Please check your input.')
            return redirect('signup')

    else:
        form = UserProfileForm()
    return render(request, 'signup.html')



def login_view(request):
    print(request.POST)
    if request.user.is_authenticated:
        return redirect('home')
    
    elif request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user) 
            messages.success(request, f"Logged in successfully!!! {user}")
            print("login success")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username Or Password")
            print("1login success")
            return redirect('login')
    return render(request, 'login.html')
def logout_view(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, "Logged out successfully")
    return redirect("home")
from django.shortcuts import render
def qr(request):
    if request.method == 'POST':
        qr_data = request.POST.get('qr_data')
        print(qr_data)
        return redirect('home')
    return render(request, 'qr.html')
from django.shortcuts import render, redirect
from .forms import ProductSelectionForm
from . import process

def search(request, product_name):
    process.main_allocate(product_name)
    flipkart = process.comparison_product_flipkart(product_name)
    return flipkart

    # if request.method == 'POST':
    #     print(request.POST)
    #     return redirect('home')
    #     # selected_product_index = int(request.POST.get('product_list'))
    #     # selected_product = flipkart[selected_product_index]

    #     # # Save the selected product to the database or perform other actions as needed
    #     # # For example, you can create a Django model to store selected products
    #     # # Replace this part with your actual model and save logic
    #     # # Example: ProductModel.objects.create(name=selected_product)

    #     # # Pass the selected product back to the home view using a session or URL parameter
    #     # request.session['selected_product'] = selected_product

    #     return redirect('home')

   # form = ProductSelectionForm(choices=enumerate(flipkart))
    
def select_item(request, selected_value):
    process.comparison_product_flipkart_amazon('realme 8')
    # Do something with the selected value, e.g., save it to the session
   # print(selected_value)
   # request.session['selected_value'] = selected_value
    return redirect('home')