from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views



base_patterns  = [
    # path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    path('api/auth/', include('project.api.api_auth.urls', namespace='api_auth')),
    
    
    path('admin/', admin.site.urls),
    path('api/users/', include('project.api.user_profile.urls', namespace='users')),
    path('api/knowledge/', include('project.api.knowledge.urls',
                                   namespace='api_knowledge')),
    path('api/home/', include('project.api.home.urls', namespace='home')),
    path('api/search/', include('project.api.search.urls', namespace='search')),
    path('api/comment/', include('project.api.comments.urls', namespace='comment')),
    path('api/rating/', include('project.api.rating.urls', namespace='rating')),
    path('api/knowledge_sharing/', include('project.api.knowledge_sharing.urls', namespace='knowledge_sharing')),
    path('docs/', include_docs_urls(title='ServiceSwap', public=True)),
]
if settings.DEBUG:
    base_patterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('backend/', include(base_patterns))
]
