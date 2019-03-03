from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .models import Blog, Category
#model 사용하겠다는 거 알려줘야 함
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BlogPost
from django.db.models import Q
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView
# from django.views.generic import ListView
# from example.config import pagination



def blog(request):
    blogs = Blog.objects
    #모델로부터 받아 처리할 수 있게끔
    #쿼리셋(을 기능적으로 처리하게 해주는 방법 --> 메소드)
    #모델이름.쿼리셋(objects).메소드()
    blog_list = Blog.objects.all() #블로그 모든 글들을 대상으로
    paginator = Paginator(blog_list, 3) #블로그 객체 세개를 한 페이지로 자르기
    page = request.GET.get('page') #request된 페이지가 뭔지를 알아내고
    try:
        posts = paginator.page(page) #request된 페이지(page변수)를 얻어온 뒤 return해 준다.
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    categories = Category.objects.all()
    return render(request, 'blog.html', {'blogs' : blogs, 'posts' : posts, 'categories' : categories})

def detail(request, blog_id, self):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    blog_list = Blog.objects.all()
    queryset = super(blog_list, self).get_queryset()
    category_id = self.request.GET.get('category')
    if category_id:
        queryset = queryset.filter(category=category_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail, 'queryset' : queryset})

def new(request):
    # Category = Category.objects.all()
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    category = Category()
    category.name = request.GET['name']
    category.save()
    return redirect('/blog/' + str(blog.id)) #pylint: disable=E1101
    # render가 '요청이 들어오면 이 html 파일을 보여줘 라는 녀석'이였다면, redirect는 '요청을 들어오면 저쪽 url로 보내버려' 하는 녀석

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능

    if request.method == 'POST' :
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:blog')

    #2. 빈 페이지를 띄워주는 기능
    else:
        form = BlogPost()
        return render(request, 'blog/new.html', {'form':form})


    # model = Blog
def search(request):
    template = 'blog/post_list.html'
    # blog_search_results = get_object_or_404(Blog, pk=blog_id)
    query = request.GET.get('q')
    if query:
            results = Blog.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
            results = Blog.objects.all()
    
    # pages = pagination(request, results, num=1)
    paginator = Paginator(results, 2) #블로그 객체 세개를 한 페이지로 자르기
    page = request.GET.get('page') #request된 페이지가 뭔지를 알아내고
    try:
        posts = paginator.page(page) #request된 페이지(page변수)를 얻어온 뒤 return해 준다.
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context = {
        'results' : results,
        # 'page_range' : posts[1],
        'query' : query,
        'posts' : posts,
    }
    return render(request, template, context)

def me(request) :
    return render(request, 'blog/me.html')


def get_context_data(self, **kwargs):
    blog_list = Blog.objects.all()
    context = super(blog_list, self).get_context_data(**kwargs)
    categories = Category.objects.all()
    context['categories'] = categories
    return context

def get_queryset(self):
    blog_list = Blog.objects.all()
    queryset = super(blog_list, self).get_queryset()
    category_id = self.request.GET.get('category')
    if category_id:
        queryset = queryset.filter(category=category_id)
    return queryset

# class PostCategory(ListView):
#     model = Blog
#     template_name = 'blog/blog_category_list.html'
#     def get_queryset(self):
#         category = get_object_or_404(Category, pk=self.kwargs['pk'])
#         return Blog.objects.filter(category=self.category)

#     def get_context_data(self, **kwargs):
#         context = super(PostCategory, self).get_context_data(**kwargs)
#         context['category'] = self.category
#         return context

# class IndexView(ListView):
#     # template_name = 'blog/post_list.html'
    
#     model = Blog
#     context_object_name = 'all_posts'
#     template = 'blog/post_list.html'
#     def search(self):
#         queryset_list = Blog.objects.all()
#         query = self.request.GET.get("q")
#         if query:
#             queryset_list = queryset_list.filter(
#                     Q(title__icontains=query) |
#                     Q(body__icontains=query)
#                     ).distinct()

#         paginator = Paginator(queryset_list, 5)  # Show 5 contacts per page
#         page = self.request.GET.get('page')
#         try:
#             queryset_list = paginator.page(page)
#         except PageNotAnInteger:
#             # If page is not an integer, deliver first page.
#             queryset_list = paginator.page(1)
#         except EmptyPage:
#             # If page is out of range (e.g. 999), deliver last page of results.
#             queryset_list = paginator.page(paginator.num_pages)
