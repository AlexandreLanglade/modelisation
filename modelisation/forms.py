from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField
from .models import Topology, Member


class TopologyForm(NetBoxModelForm):

    class Meta:
        model = Topology
        fields = ('name', 'slug', 'description', 'tags')

class MemberForm(NetBoxModelForm):

    topology = DynamicModelChoiceField(
        queryset=Topology.objects.all()
    )

    class Meta:
        model = Member
        fields = ('name', 'slug', 'type', 'topology', 'description', 'tags')