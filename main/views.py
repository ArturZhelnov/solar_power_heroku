from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact#, Social_link
from .forms import ContactForm
# Create your views here.


def index(request):
    '''
    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')#all()
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()
    '''
    ###
    '''
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was successfully sent!')
    '''
    ###
    
    #social_profiles = Social_link.objects.all()
    
   
    '''
<ul class="header_social nav d-flex align-items-center justify-content-center align-content-center">
    {% for social in social_profiles %}
        <li class="social_item nav-item col-md-6 col-lg-3 text-center"><a class="social_link nav-link" href="{{ social.link }}"><img class="" src="{% static 'images/social/instagram.svg' %}" alt="{{ social.social_name }}"/></a></li>
    {% empty %}
        <li class="social_item nav-item col-md-6 col-lg-3 text-center">
            <p>There are no social contacts yet..</p>
        </li>
    {% endfor %}
</ul>


    /*WORKING*/
    
    forms = ContactForm()
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.info(request, 'Your message was successfully sent! Thank You.')
            #messages.add_message(request, messages.INFO, 'Message sent successfully!')
            #messages.success(request, 'Your message was successfully sent!')
            return redirect('main:index')
        else:
            messages.warning(request, "Something went wrong.. Check up your email.")
        
     /*WORKING*/   
        
    '''
    
    forms = ContactForm()
    if request.method == 'POST':
        phone = request.POST.get("phone", None)
        phone_query = Contact.objects.filter(phone=phone)
        if phone:
            if phone_query.exists():
                messages.warning(request, "You are already on the waitlist.")
                return redirect('main:index')
            else:
                forms = ContactForm(request.POST)
                if forms.is_valid():
                    forms.save()
                    messages.info(request, 'Your message was successfully sent! Thank You.')
                    #messages.add_message(request, messages.INFO, 'Message sent successfully!')
                    #messages.success(request, 'Your message was successfully sent!')
                    return redirect('main:index')
                else:
                    messages.warning(request, "Something went wrong.. Check up your phone or name and try again.")
                    return redirect('main:index')
                
    '''
    form = NewsletterForm()
    if request.method == 'POST':
        email = request.POST.get("email", None)
        #email = NewsletterForm(request.POST.get("email", None))
        email_query = Newsletter.objects.filter(email=email)
        if email:
            if email_query.exists():
                messages.info(request, "You are already on the waitlist.")
            else:
                form = NewsletterForm(request.POST)
                if form.is_valid():
                    form = Newsletter.objects.create(email=email)
                    form.save()
                    messages.success(request,
                                     "Thank you for subscribing! Bear with us.")
                else:
                    messages.warning(request, "Something went wrong. Please check up your email and try again.")
            
    
    context = {'forms': forms, }
    #'social_profiles': social_profiles,
    '''
    context = {'forms': forms, }

    return render(request, 'main/index.html', context)