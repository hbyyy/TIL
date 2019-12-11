import os

from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from blog.models import Post


def post_list(request):
    # cur_file_path = os.path.abspath(__file__)
    # parent_file_path = os.path.dirname(os.path.dirname(cur_file_path))
    # target_file_path = os.path.join(parent_file_path, 'templates', 'post_list.html')
    #
    # with open(target_file_path, 'rt') as f:
    #     html = f.read()
    #
    # return HttpResponse(html)

    posts = Post.objects.all()
    context = dict(posts=posts)
    return render(request, 'post_list.html', context)
