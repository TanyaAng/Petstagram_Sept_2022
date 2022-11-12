class DisableFormMixin:
    disable_fields = ()
    fields = None

    def _disable_fields(self):
        if self.disable_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disable_fields
        for field_name in fields:
            if field_name in self.fields:
                field=self.fields[field_name]
                # field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'