from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogModel
from .forms import BlogForm


def detail_blog_view(request, slug):
    obj = get_object_or_404(BlogModel, slug=slug)
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

def list_blog_view(request):
    qs = BlogModel.objects.all()
    # if request.user.is_authenticated:
    #     user_qs = BlogModel.objects.filter(user=request.user)
    #     qs = (qs | user_qs).distinct()
    context = {'object_list': qs}
    template_name = 'blog/list.html'
    return render(request, template_name, context)

def create_blog_view(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogForm()
    template_name = 'blog/create.html'
    context = {'form': form}
    return render(request, template_name, context)

def delete_blog_view(request, slug):
    obj = get_object_or_404(BlogModel, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog/')
    template_name = 'blog/delete.html'
    context = {'object': obj}
    return render(request, template_name, context)

def update_blog_view(request, slug):
    obj = get_object_or_404(BlogModel, slug=slug)
    form = BlogForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = BlogForm()
        return redirect('/')
    template_name = 'blog/update.html'
    context = {'object': obj, 'form': form}
    return render(request, template_name, context)
