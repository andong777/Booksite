# coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,RequestContext
from django.contrib import auth
from django.db.models import Q
import forms, models
from datetime import datetime

show_book_num = 6    # 首页中每一栏显示的数量
show_tag_num = 20
show_comment_num = 10

def home(request):
    user = request.user
    new_books = models.Book.objects.order_by("-date")[:show_book_num]
    good_books = models.Book.objects.order_by("-score")[:show_book_num]
    hot_books = models.Book.objects.order_by("-vote")[:show_book_num]
    return render_to_response("home.html",locals())

def category(request):
    length = models.Tag.objects.count()
    num = show_tag_num if show_tag_num < length else length
    tags = models.Tag.objects.order_by("add_time")[:num]
    return render_to_response("category.html",{'user':request.user,'tags':tags})

def comment(request):
    length = models.Comment.objects.count()
    num = show_comment_num if show_comment_num < length else length
    comments = models.Comment.objects.order_by("add_time")[:num]
    return render_to_response("comment.html",{'user':request.user,'comments':comments})

def search(request):
    if request.method == 'GET':
        try:
            q = request.GET['q']
        except:
            return render_to_response("search.html",{'user':request.user})
        if q:
            books = models.Book.objects.filter(Q(name__icontains=q) | Q(writer__name__icontains=q) | Q(press__name__icontains=q) | Q(isbn__exact=q))
            if books:
                return render_to_response("search.html",{'books':books,'user':request.user})
        return render_to_response("search.html",{'user':request.user,'error':True})
    return render_to_response("search.html",{'user':request.user})

@login_required
def myinfo(request):
    if request.method == 'POST':
        form = forms.ModifyPasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            old_password = data['old_password']
            user = auth.authenticate(username=request.user.username,password=old_password)
            if user is not None:
                user.set_password(data['password'])
                user.save()
                return render_to_response("myinfo.html",context_instance=RequestContext(request,{'form':form,'success':True}))
    else:
        form = forms.ModifyPasswordForm()
    return render_to_response("myinfo.html",context_instance=RequestContext(request,{'form':form}))

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['username'],email=data['email'])
            user.set_password(data['password'])
            user.save()
            return HttpResponseRedirect(r'/accounts/login')
    else:
        form = forms.RegisterForm()
    return render_to_response('registration/register.html',context_instance=RequestContext(request,{'form':form }))

def Writer(request,id):
    writer = models.Writer.objects.get(pk=id)
    return render_to_response("writer.html",{'user':request.user,'writer':writer})

def Press(request,id):
    press = models.Press.objects.get(pk=id)
    return render_to_response("press.html",{'user':request.user,'press':press})

def Book(request,isbn):
    book = models.Book.objects.get(pk=isbn)
    if request.method == 'GET':
        form = forms.AddCommentForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            now = datetime.now()
            models.Comment.objects.create(user=request.user,book=book,title=data['title'],content=data['content'],add_time=now)
            return render_to_response("book.html",context_instance=RequestContext(request,{'form':form,'user':request.user,'book':book }))
    form = forms.AddCommentForm()
    return render_to_response("book.html",context_instance=RequestContext(request,{'user':request.user,'book':book,'form':form}))

def Tag(request,name):
    tag = models.Tag.objects.get(pk=name)
    return render_to_response("tag.html",{'user':request.user,'tag':tag})

def update_score(request):
    if request.method == 'GET':
        score = request.GET.get('score','')
        isbn = request.GET.get('isbn','')
        if score and isbn:
            book = models.Book.get(pk=isbn)
            book.score = score
            book.vote = book.vote + 1
