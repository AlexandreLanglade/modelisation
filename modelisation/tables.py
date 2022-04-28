import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import FabricPath, Topology, Member

class FabricPathTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    topology_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = FabricPath
        fields = ('pk', 'id', 'name', 'slug', 'topology_count', 'description', 'actions')
        default_columns = ('name', 'slug', 'topology_count', 'description')

class TopologyTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    fabric_path = tables.Column(
        linkify=True
    )

    member_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Topology
        fields = ('pk', 'id', 'name', 'slug', 'fabric_path', 'member_count', 'description', 'actions')
        default_columns = ('name', 'slug', 'member_count', 'description')


class MemberTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    topology = tables.Column(
        linkify=True
    )

    type = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = Member
        fields = ('pk', 'id', 'name', 'slug', 'type', 'topology', 'description', 'actions')
        default_columns = ('name', 'slug', 'type', 'topology', 'description', 'actions')
