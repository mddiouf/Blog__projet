from django .urls import path # type: ignore
from .views import post_list
from .views import post_detail,le_formulaire , blog , index
urlpatterns = [
       path('post/', post_list, name='post_list'),

       path('post/<int:id>',post_detail,name='post_detail'),

       path('formulaire/',le_formulaire,name='le_formulaire'),

       path('vers_blog/',blog,name='blog'),

       path('index/',index,name='index'),

] 