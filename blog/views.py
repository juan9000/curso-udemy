from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic import CreateView
from . models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    #context_object_name = 'custom'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('autor','titulo','conteudo')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('titulo','conteudo')

"""
STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250)
    autor = models.ForeignKey(User,
    on_delete=models.CASCADE)
    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
    choices=STATUS,
    default='rascunho')
"""