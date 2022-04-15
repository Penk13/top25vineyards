from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from .models import Vineyard, Region


class VineyardResource(resources.ModelResource):
    region = fields.Field(column_name='region', attribute='region', widget=ForeignKeyWidget(Region, field='name'))
    regions = fields.Field(column_name='regions', attribute='regions', widget=ManyToManyWidget(Region, field='name'))

    class Meta:
        model = Vineyard
        fields = ('id', 'name', 'rating', 'username', 'email1', 'email2', 
        'text', 'address', 'website', 'web_text', 'number', 'region', 
        'regions', 'wines', 'size', 'grapes', 'owner', 'visits', 
        'google_map', 'cover2', 'wine_rg_url', 'wines_url', 'owner_url', 
        'hide_rating', 'display', 'send_email',)
        export_order = ('id', 'name', 'rating', 'username', 'email1', 'email2', 
        'text', 'address', 'website', 'web_text', 'number', 'region', 
        'regions', 'wines', 'size', 'grapes', 'owner', 'visits', 
        'google_map', 'cover2', 'wine_rg_url', 'wines_url', 'owner_url', 
        'hide_rating', 'display', 'send_email',)
        import_id_fields = ['id']
        skip_unchanged = True
        report_skipped = True

    def after_import_instance(self, instance, new, **kwargs):
        instance.user = kwargs['user']
