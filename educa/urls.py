from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('course/', include('courses.urls')),
    path('q/', include('quiz.urls')),
    path('', views.CourseListView.as_view(), name='course_list'),
    #path('',include('courses.urls'),name='home'),
    path('students/', include('students.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]