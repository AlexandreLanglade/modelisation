from netbox.views import generic
from . import forms, models, tables
from django.db.models import Count


# --- Fabric Path ---

class FabricPathView(generic.ObjectView):
    queryset = models.FabricPath.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.TopologyTable(instance.topologies.all())
        table.configure(request)

        return {
            'topologies_table': table,
        }

class FabricPathListView(generic.ObjectListView):
    queryset = models.FabricPath.objects.annotate(
        topology_count=Count('topologies')
    )
    table = tables.FabricPathTable

class FabricPathEditView(generic.ObjectEditView):
    queryset = models.FabricPath.objects.all()
    form = forms.FabricPathForm

class FabricPathDeleteView(generic.ObjectDeleteView):
    queryset = models.FabricPath.objects.all()


# --- Topology ---

class TopologyView(generic.ObjectView):
    queryset = models.Topology.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.MemberTable(instance.members.all())
        table.configure(request)

        return {
            'members_table': table,
        }


class TopologyListView(generic.ObjectListView):
    queryset = models.Topology.objects.annotate(
        member_count=Count('members')
    )
    table = tables.TopologyTable


class TopologyEditView(generic.ObjectEditView):
    queryset = models.Topology.objects.all()
    form = forms.TopologyForm


class TopologyDeleteView(generic.ObjectDeleteView):
    queryset = models.Topology.objects.all()


# --- Member ---

class MemberView(generic.ObjectView):
    queryset = models.Member.objects.all()


class MemberListView(generic.ObjectListView):
    queryset = models.Member.objects.all()
    table = tables.MemberTable


class MemberEditView(generic.ObjectEditView):
    queryset = models.Member.objects.all()
    form = forms.MemberForm


class MemberDeleteView(generic.ObjectDeleteView):
    queryset = models.Member.objects.all()