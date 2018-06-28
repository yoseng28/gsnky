import xadmin

from information.models import Information, InformationType


class InformationAdmin(object):

    def get_readonly_fields(self):
        if self.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    readonly_fields = ('add_time',)
    list_display = ['name', 'publisher', 'type', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'publisher', 'type', 'add_time']
    model_icon = 'fa fa-upload'
    style_fields = {"detail": "ueditor"}


class InformationTypeAdmin(object):

    def get_readonly_fields(self):
        if self.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    readonly_fields = ('add_time',)
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    model_icon = 'fa fa-upload'


xadmin.site.register(Information, InformationAdmin)
xadmin.site.register(InformationType, InformationTypeAdmin)
