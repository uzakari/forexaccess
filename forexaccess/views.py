from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from .models import Faq1
from .forms import ContactForm, RegisterationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.


def index(request):
    return render(request, "forexaccess/index.html")


def about(request):
    return render(request, "forexaccess/About.html")


def open_demo_account(request):
    return render(request, "forexaccess/open_demo_acc.html")


def open_live_account(request):
    return render(request, "forexaccess/open_live_acc.html")


def getting_started(request):
    return render(request, "forexaccess/getting_started.html")


def account_types(request):
    faq = Faq1.objects.all().order_by('date')
    context = {'faq': faq}
    return render(request, "forexaccess/account_types.html", context)


def education(request):
    return render(request, "forexaccess/education.html")


def deposit_withdrawal(request):
    return render(request, 'forexaccess/deposit_withdrawal.html')


def investment(request):
    return render(request, 'forexaccess/Investment.html')


def contact_us(request):
    form = ContactForm(request.POST or None)
    try:
        if form.is_valid():
            # reason = form.cleaned_data['reason']

            form.save()
            messages.success(request, 'Your Request Is Successful')
    except Exception as e:
        form = ContactForm()
        messages.warning(request, 'Error: {}'.format(e))
    context = {'form': form}
    return render(request, 'forexaccess/contact_us.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def Economic_calender(request):
    return render(request, 'forexaccess/econominc_calender.html')


def platforms(request):
    return render(request, 'forexaccess/platforms.html')


def ecoIndicator(request):
    return render(request, 'forexaccess/EconominIndicators.html')


def copy_trading(request):
    return render(request, 'forexaccess/copy_trading.html')

def handler404(request, exception, template_name='404.html'):
    response = render_to_response('template_name', {}, context_instance=RequestContext(request))
    response.status_code = 400
    return response