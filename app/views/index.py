import http.client

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.models import Post, News, Activities
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')


def gallery(request):
    return render(request, 'gallery.html')


def blog(request):
    blog_posts = Post.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                subject='Message from Volti Website',
                message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
                from_email=email,
                recipient_list=['your_email@example.com'],
                fail_silently=False,
            )
            messages.success(request, 'Email successfully sent!')
        except ValidationError as e:
            messages.error(request, 'Email validation error occurred. Please try again.')
        except Exception as e:
            messages.error(request, 'An error occurred while sending the email. Please try again later.')

        return HttpResponseRedirect(reverse('contactus'))

    return render(request, 'contacts.html')


def money(request):
    return render(request, 'money.html')


def about(request):
    return render(request, 'about.html')


def money(request):
    return render(request, 'money.html')


def projects(request):
    return render(request, 'projects.html')


def team(request):
    return render(request, 'team.html')


def news(request):
    news_posts = News.objects.all()
    return render(request, 'news.html', {'news_posts': news_posts})


def carieers(request):
    all_positions = Activities.objects.all()
    return render(request, 'carieers.html', {'all_positions': all_positions})


def carierdes(request):
    return render(request, 'carierdes.html')


def newsDsc(request):
    return render(request, 'newsDsc.html')
