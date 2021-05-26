from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm

# Create your views here.

# home page
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 4

# postdetail home
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# create home
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = PostForm()
        context = {'form':form}
        return render(request, 'blog/create.html', context)

# update page
def update(request, id):
    prefill = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST ,instance=prefill)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm(instance=prefill)
        context = {'form':form}
        return render(request, 'blog/update.html', context)

# search bar
def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('s')
        post_list = Post.objects.filter(title__icontains = search)
        return render(request, 'blog/index.html', {'post_list':post_list})

# dashboard
def dashboard(request):
        user = request.user.id
        userlist = Post.objects.filter(author=user)
        return render(request, 'blog/user.html', {'userlist':userlist})