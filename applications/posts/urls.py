from django.urls import path, include

from applications.posts.views import CategoryApiView, CommentApiView, PostAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryApiView)
router.register('comment', CommentApiView)
router.register('', PostAPIView)

urlpatterns = [
    # path('', PostAPIView.as_view({'get':'list', 'post':'create'}))
    # path('', include(router.urls))
]

urlpatterns += router.urls