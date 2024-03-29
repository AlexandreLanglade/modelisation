from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    # --- Fabric Path ---
    path('fabric-paths/', views.FabricPathListView.as_view(), name='fabricpath_list'),
    path('fabric-paths/add/', views.FabricPathEditView.as_view(), name='fabricpath_add'),
    path('fabric-paths/<int:pk>/', views.FabricPathView.as_view(), name='fabricpath'),
    path('fabric-paths/<int:pk>/edit/', views.FabricPathEditView.as_view(), name='fabricpath_edit'),
    path('fabric-paths/<int:pk>/delete/', views.FabricPathDeleteView.as_view(), name='fabricpath_delete'),
    path('fabric-paths/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='fabricpath_changelog', kwargs={
        'model': models.FabricPath
    }),


    # --- Topology ---
    path('topologies/', views.TopologyListView.as_view(), name='topology_list'),
    path('topologies/add/', views.TopologyEditView.as_view(), name='topology_add'),
    path('topologies/<int:pk>/', views.TopologyView.as_view(), name='topology'),
    path('topologies/<int:pk>/edit/', views.TopologyEditView.as_view(), name='topology_edit'),
    path('topologies/<int:pk>/delete/', views.TopologyDeleteView.as_view(), name='topology_delete'),
    path('topologies/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='topology_changelog', kwargs={
        'model': models.Topology
    }),


    # --- Member ---
    path('members/', views.MemberListView.as_view(), name='member_list'),
    path('members/add/', views.MemberEditView.as_view(), name='member_add'),
    path('members/<int:pk>/', views.MemberView.as_view(), name='member'),
    path('members/<int:pk>/edit/', views.MemberEditView.as_view(), name='member_edit'),
    path('members/<int:pk>/delete/', views.MemberDeleteView.as_view(), name='member_delete'),
    path('members/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='member_changelog', kwargs={
        'model': models.Member
    }),

)