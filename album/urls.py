from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.base, name='inicio'),
    url(r'^categorias/$', views.CategoriaListView.as_view(), name='lista-categorias'),
    #url(r'^categorias$', views.listar_categorias, name='lista-categorias'),
    url(r'^categoria/(?P<pk>\d+)/detalle/$', views.CategoriaDetailView.as_view(), name='detalle-categoria'),
    #url(r'^categoria/(?P<id_categoria>\d+)/detalle$', views.detalle_categoria, name='detalle-categoria'),
    #create
    url(r'^categoria/nueva/$', views.CategoriaCreate.as_view(), name='nueva-categoria'),
    #update
    url(r'^categoria/(?P<pk>\d+)/editar/$', views.CategoriaUpdate.as_view(), name='editar-categoria'),
    #delete
    url(r'^categoria/(?P<pk>\d+)/eliminar/$', views.CategoriaDelete.as_view(), name='eliminar-categoria'),

    url(r'^fotos/$', views.FotoListView.as_view(), name='lista-fotos'),
    url(r'^foto/(?P<pk>\d+)/detalle/$', views.FotoDetailView.as_view(), name='detalle-foto'),
    #url(r'^foto/(?P<slug>\d+)/detalle$', views.FotoDetailView.as_view(), name='detalle-foto'),
    #create
    url(r'^foto/nueva/$', views.FotoCreate.as_view(), name='nueva-foto'),
    #update
    url(r'^foto/(?P<pk>\d+)/editar/$', views.FotoUpdate.as_view(), name='editar-foto'),
    #delete
    url(r'^foto/(?P<pk>\d+)/eliminar/$', views.FotoDelete.as_view(), name='eliminar-foto'),
]
