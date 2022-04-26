import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Topology, Member

class TopologyTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    member_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Topology
        fields = ('pk', 'id', 'name', 'slug', 'member_count', 'description', 'actions')
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
