from netbox.plugins import PluginConfig


class PhoneBoxConfig(PluginConfig):
    name = 'phonebox_plugin'
    verbose_name = 'PhoneBox Plugin'
    description = 'Telephone Number Management Plugin for NetBox.'
    version = '1.0.0'
    author = 'Isaiah Olson'
    author_email = 'insignia96@gmail.com'
    base_url = 'phonebox'
    min_version = '4.5.0'
    max_version = '4.6.99'
    required_settings = []
    default_settings = {}


config = PhoneBoxConfig
