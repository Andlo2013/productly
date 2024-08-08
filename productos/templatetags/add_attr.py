from django import template
register=template.Library()

@register.filter(name="add_attr")
def add_attr(field, css):
    attrs={}
    clase,valor=css.split(':')
    attrs[clase]=valor
    print(f"Applying filter to field: {field.name}")
    return field.as_widget(attrs=attrs) 