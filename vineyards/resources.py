from import_export import resources, fields, widgets
from .models import Vineyard
from django.contrib.auth import get_user_model


User = get_user_model()


class VineyardResource(resources.ModelResource):

    email2 = fields.Field(attribute="email2", column_name="email2", widget=widgets.CharWidget(), default="")
    text = fields.Field(attribute="text", column_name="text", widget=widgets.CharWidget(), default="")
    address = fields.Field(attribute="address", column_name="address", widget=widgets.CharWidget(), default="")
    website = fields.Field(attribute="website", column_name="website", widget=widgets.CharWidget(), default="")
    web_text = fields.Field(attribute="web_text", column_name="web_text", widget=widgets.CharWidget(), default="")
    number = fields.Field(attribute="number", column_name="number", widget=widgets.CharWidget(), default="")
    wine_rg = fields.Field(attribute="wine_rg", column_name="wine_rg", widget=widgets.CharWidget(), default="")
    wines = fields.Field(attribute="wines", column_name="wines", widget=widgets.CharWidget(), default="")
    size = fields.Field(attribute="size", column_name="size", widget=widgets.CharWidget(), default="")
    grapes = fields.Field(attribute="grapes", column_name="grapes", widget=widgets.CharWidget(), default="")
    owner = fields.Field(attribute="owner", column_name="owner", widget=widgets.CharWidget(), default="")
    visits = fields.Field(attribute="visits", column_name="visits", widget=widgets.CharWidget(), default="")
    google_map = fields.Field(attribute="google_map", column_name="google_map", widget=widgets.CharWidget(), default="")
    wine_rg_url = fields.Field(attribute="wine_rg_url", column_name="wine_rg_url", widget=widgets.CharWidget(), default="")
    wines_url = fields.Field(attribute="wines_url", column_name="wines_url", widget=widgets.CharWidget(), default="")
    owner_url = fields.Field(attribute="owner_url", column_name="owner_url", widget=widgets.CharWidget(), default="")
    filter_tags = fields.Field(attribute="filter_tags", column_name="filter_tags", widget=widgets.CharWidget(), default="")

    class Meta:
        model = Vineyard
        fields = ('id', 'name', 'rating', 'username', 'email2', 
        'text', 'address', 'website', 'web_text', 'number', 'wine_rg', 
        'region', 'regions', 'wines', 'size', 'grapes', 'owner', 'visits', 
        'google_map', 'cover', 'wine_rg_url', 'wines_url', 'owner_url', 
        'hide_rating', 'display', 'send_email', 'filter_tags')
        export_order = ('id', 'name', 'rating', 'username', 'email2', 
        'text', 'address', 'website', 'web_text', 'number', 'wine_rg', 
        'region', 'regions', 'wines', 'size', 'grapes', 'owner', 'visits', 
        'google_map', 'cover', 'wine_rg_url', 'wines_url', 'owner_url', 
        'hide_rating', 'display', 'send_email', 'filter_tags')
        import_id_fields = ['id']
        skip_unchanged = True
        report_skipped = True

    def after_import_instance(self, instance, new, **kwargs):
        instance.user = kwargs['user']

    def before_save_instance(self, instance, using_transactions, dry_run):
        if instance.name == "" or instance.text == "" or not instance.cover:
            instance.display = 0

        if instance.username:
            current_user = User.objects.get(username=instance.username)
            instance.user = current_user
            instance.email1 = current_user.email
        else:
            instance.username = instance.user.username
            instance.email1 = instance.user.email
        return instance
