from django.urls import path 
from post import views as post_views

urlpatterns = [   
    path('', post_views.PostListView.as_view(), name='post-list'),         

	path('post-create/', post_views.PostCreateView.as_view(), name='post-create'), 

    path('post-detail/<int:pk>/', post_views.PostDetailView.as_view(), name='post-detail'),  

    path('post-update/<int:pk>/', post_views.PostUpdateView.as_view(), name='post-update'),

    path('post-delete/<int:pk>/', post_views.PostDeleteView.as_view(), name='post-delete'),  

    path('post/<int:post_pk>/comment/edit/<int:pk>/', post_views.CommentEditView.as_view(), name="comment-edit"),

    path('post/<int:post_pk>/comment/delete/<int:pk>/', post_views.CommentDeleteView.as_view(), name="comment-delete"),   

    path('post/<int:post_pk>/comment/reply/<int:pk>/', post_views.CommentReplyView.as_view(), name='comment-reply'),
]