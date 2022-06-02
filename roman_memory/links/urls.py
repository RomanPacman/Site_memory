from django.urls import path
from . import views

urlpatterns = [
    path('', views.LinksList.as_view(), name='links'),
    path('add_link', views.add_link, name='add_link'),
    # path('add_link', views.LinksCreate.as_view(), name='add_link'),
    path('<int:pk>', views.LinksDetailView.as_view(), name='links_detail'),
    path('<int:pk>/update', views.LinksRedactView.as_view(), name='links_update'),
    path('<int:pk>/delete', views.LinksDeleteView.as_view(), name='links_delete')



]
