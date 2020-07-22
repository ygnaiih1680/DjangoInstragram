from django.shortcuts import render, get_object_or_404
from .models import Content


def home(request):
    contents = Content.objects.all()
    return render(request, 'home.html', {'contents': contents})


def detail(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    return render(request, 'detail.html', {'content': content})
