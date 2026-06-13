from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu = PluginMenu(
    label='PhoneBox',
    groups=(
        ('Telephony', (
            PluginMenuItem(
                link='plugins:phonebox_plugin:number_list',
                link_text='Numbers',
                buttons=(
                    PluginMenuButton(
                        link='plugins:phonebox_plugin:number_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                    ),
                    PluginMenuButton(
                        link='plugins:phonebox_plugin:number_import',
                        title='Import',
                        icon_class='mdi mdi-upload',
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:phonebox_plugin:voicecircuit_list',
                link_text='Voice Circuits',
                buttons=(
                    PluginMenuButton(
                        link='plugins:phonebox_plugin:voicecircuit_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                    ),
                    PluginMenuButton(
                        link='plugins:phonebox_plugin:voicecircuit_import',
                        title='Import',
                        icon_class='mdi mdi-upload',
                    ),
                ),
            ),
        )),
    ),
    icon_class='mdi mdi-phone',
)
