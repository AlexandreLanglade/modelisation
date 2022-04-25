from extras.plugins import PluginConfig

class ModelisationConfig(PluginConfig):
    name = 'modelisation'
    verbose_name = ' Modelisation'
    description = 'FabricPaths & Topologies modelisation'
    version = '0.1'
    base_url = 'modelisation'


config = ModelisationConfig