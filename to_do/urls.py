from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    TaskListView,
    task_change_status, TagListView, TagUpdateView, TagDeleteView, TagCreateView, TaskDeleteView, TaskUpdateView,
    TaskCreateView,
)


class TegCreateView:
    pass


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/manage/<int:pk>/<action>", task_change_status, name="task_change_status"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("/create/", TaskCreateView.as_view(), name="to_do-create"),
    path("/<int:pk>/update/", TaskUpdateView.as_view(), name="to_do-update"),
    path("/<int:pk>/delete/", TaskDeleteView.as_view(), name="to_do-delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "to_do"
