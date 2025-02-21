from django.shortcuts import render ,redirect# type: ignore
from django.shortcuts import render , get_object_or_404 # type: ignore
from .models import Post
from .forms import PostForm
def post_list(request):
   posts = Post.objects.all().order_by('-created_at')
   return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    print("#==="*40)
    print(post)
    print("#==="*40)

def blog(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request,'blog/blog.html',{'posts': posts})

 
def index(request):

    return render(request,'blog/index.html',{'index':index})
 
# fonction pour le  formulaire
def le_formulaire(request):
    if request.method =="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form =PostForm()
    return render(request,'blog/formulaire.html',{'form':form})

