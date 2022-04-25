from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import OrganizationalModel, NetBoxModel
from utilities.choices import ChoiceSet

class MemberTypeChoices(ChoiceSet):
    key = 'Member.type'

    CHOICES = [
        ('device', 'Device', 'purple'),
        ('device_role', 'Device Role', 'blue'),
        ('vlan', 'VLAN', 'orange'),
    ]

class Topology(OrganizationalModel):

    def __str__(self):
        return self.name

class Member(NetBoxModel):

    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True
    )
    type = models.CharField(
        max_length=20,
        choices=MemberTypeChoices,
    )
    topology = models.ForeignKey(
        to=Topology,
        on_delete=models.PROTECT,
        related_name='Members'
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        ordering = ('topology','name')

    def __str__(self):
        return self.name

    def get_type_color(self):
        return MemberTypeChoices.colors.get(self.type)