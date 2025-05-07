from django.shortcuts import render
from django.http import HttpResponse
from .models import Link
from .utils import generate_shortcode

# Create your views here.
#Index function

def home(request):
    if request.method == 'POST':
        original_url = request.POST['url']
        shorten_code = generate_shortcode()

        link = Link.objects.create(original_url=original_url, shorten_code=shorten_code)
        short_url = request.build_absolute_uri('/') + shorten_code
        
        return render(request, 'linkchop/index.html', {'short_url': short_url})
    return render(request, 'linkchop/index.html' )

