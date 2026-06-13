import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Switches Number and VoiceCircuit from ChangeLoggedModel to NetBoxModel.

    NetBoxModel adds the custom_field_data column (CustomFieldsMixin) and brings the
    journaling / bookmark / change-logging features (which live in separate tables and
    require no columns here).

    The VoiceCircuit.assigned_object generic FK keeps its content-type FK pointed at
    contenttypes.ContentType (Django's GenericForeignKey requires this -- a proxy like
    core.ObjectType trips the contenttypes.E004 system check). ObjectType is used only at
    the serializer/form/query layer, mirroring NetBox core. So the FK is unchanged here.

    NOTE: Regenerate/verify with `./manage.py makemigrations --check` against a NetBox 4.5
    install before release to ensure this matches the autodetector exactly.
    """

    dependencies = [
        ('phonebox_plugin', '0004_alter_number_created_alter_number_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='custom_field_data',
            field=models.JSONField(
                blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder
            ),
        ),
        migrations.AddField(
            model_name='voicecircuit',
            name='custom_field_data',
            field=models.JSONField(
                blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder
            ),
        ),
        migrations.AlterModelOptions(
            name='number',
            options={'ordering': ('number', 'tenant')},
        ),
        migrations.AlterModelOptions(
            name='voicecircuit',
            options={'ordering': ('name',)},
        ),
    ]
