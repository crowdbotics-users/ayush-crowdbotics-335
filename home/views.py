from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'django-tastypie', 'url': 'http://pypi.python.org/pypi/django-tastypie/0.14.0'},
	{'name':'django-rest-framework', 'url': 'http://pypi.python.org/pypi/django-rest-framework/0.1.0'},
	{'name':'djangorestframework', 'url': 'http://pypi.python.org/pypi/djangorestframework/3.7.7'},
	{'name':'django-bootstrap4', 'url': 'http://pypi.python.org/pypi/django-bootstrap4/0.0.5'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
