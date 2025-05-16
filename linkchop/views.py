from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Link
from .utils import generate_shortcode
from django.shortcuts import render, get_object_or_404

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


def redirect_to_original(request, shorten_code):
    link = get_object_or_404(Link, shorten_code=shorten_code)
    return HttpResponseRedirect(link.original_url)