from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices



fabricpath_butons = [
    PluginMenuButton(
        link='plugins:modelisation:fabricpath_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

topology_butons = [
    PluginMenuButton(
        link='plugins:modelisation:topology_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

member_buttons = [
    PluginMenuButton(
        link='plugins:modelisation:member_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:modelisation:fabricpath_list',
        link_text='Fabric Paths',
        buttons=fabricpath_butons
    ),
    PluginMenuItem(
        link='plugins:modelisation:topology_list',
        link_text='Topologies',
        buttons=topology_butons
    ),
    PluginMenuItem(
        link='plugins:modelisation:member_list',
        link_text='Members',
        buttons=member_buttons
    ),
)