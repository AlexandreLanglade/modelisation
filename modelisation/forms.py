from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField
from .models import FabricPath, Topology, Member


class FabricPathForm(NetBoxModelForm):

    class Meta:
        model = FabricPath
        fields = ('name', 'slug', 'description', 'tags')

class TopologyForm(NetBoxModelForm):

    fabric_path = DynamicModelChoiceField(
        queryset=FabricPath.objects.all()
    )

    class Meta:
        model = Topology
        fields = ('name', 'slug', 'fabric_path', 'description', 'tags')

class MemberForm(NetBoxModelForm):

    topology = DynamicModelChoiceField(
        queryset=Topology.objects.all()
    )

    class Meta:
        model = Member
        fields = ('name', 'slug', 'type', 'topology', 'description', 'tags')