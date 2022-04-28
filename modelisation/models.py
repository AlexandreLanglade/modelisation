from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import OrganizationalModel, NetBoxModel
from utilities.choices import ChoiceSet
from django.urls import reverse

class MemberTypeChoices(ChoiceSet):
    key = 'Member.type'

    CHOICES = [
        ('device', 'Device', 'purple'),
        ('device_role', 'Device Role', 'blue'),
        ('vlan', 'VLAN', 'orange'),
    ]

class FabricPath(OrganizationalModel):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:modelisation:fabricpath', args=[self.pk])

class Topology(OrganizationalModel):

    fabric_path = models.ForeignKey(
        to=FabricPath,
        on_delete=models.PROTECT,
        related_name='topologies'
    )

    class Meta:
        ordering = ('fabric_path','name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:modelisation:topology', args=[self.pk])

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
        related_name='members'
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        ordering = ('topology','name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:modelisation:member', args=[self.pk])

    def get_type_color(self):
        return MemberTypeChoices.colors.get(self.type)