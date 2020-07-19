from django.shortcuts import render
from django.shortcuts import redirect
from .models import Blog, Author
from .forms import Blogform, Authorform
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form1 = Blogform(request.POST)
        form2 = Authorform(request.POST)
        if form1.is_valid() and form2.is_valid():
            blog_model = form1.save()
            author_model = form2.save(commit=False)
            author_model.blog_id = blog_model.id
            author_model.save()
            messages.success(request,'blog created sucessfully')
        return redirect('/blog')

    context ={
        'blogform': Blogform,
        'authorform': Authorform
    }
    return render(request, 'Blog/home.html', context= context)


def blog(request):
    context = {
        'blog_list': Blog.objects.all()
    }
    return render(request, 'Blog/blog.html', context=context)


def author(request):
    context = {
        'author_list': Author.objects.all()
    }
    return render(request, 'Blog/author.html', context=context)


def delete_blog(request, id):
    obj = Blog.objects.get(id=id)
    obj.delete()
    messages.error(request, 'blog deleted sucessfully')
    return redirect('/blog')


def delete_author(request, id):
    obj = Author.objects.get(id=id)
    obj.delete()
    messages.error(request, 'author deleted sucessfully')
    return redirect('/author')
