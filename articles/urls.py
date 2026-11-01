from django.urls import path
from .views import (ArticleListView,
                    ArticleDeleteView,
                    ArticleDetailView,
                    ArticleUpdateView,
                    ArticleCreateView,)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path("<int:pk>/", ArticleDetailView.as_view(),name="article-detail"), # new
    path("<int:pk>/edit/", ArticleUpdateView.as_view(),name="article-edit"), # new
    path("<int:pk>/delete/", ArticleDeleteView.as_view(),name="article-delete"), # new
    path("new/", ArticleCreateView.as_view(), name="article-new"),
    ]