from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.http import Http404
from comments.models import Comment
from .forms import CommentForm

# Create your views here.

def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comments:index')
    else:
        form = CommentForm()
    return render(request,'comments/add.html', {'form':form})

def index(request):
    # comments = get_list_or_404(Comment, pk__gt=10)
    comments = Comment.objects.all()
    paginator = Paginator(comments, 5)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    return render(request, 'comments/index.html', {'comments':comments_page})

def update(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()
            return redirect('comments:index')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/add.html', {'form':form, 'comment':comment})    

def delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('comments:index')