import datetime
from django import template
from django.conf import settings
from pressbox.models import PressItem, PressImage, PressCategory

register = template.Library()

@register.inclusion_tag('includes/templatetags/press_items.html', takes_context=True)
def press_items(context, max=10):
    items = PressItem.objects.active()
    return {
        'objects': items[:max],
    }
    
@register.inclusion_tag('includes/templatetags/press_item.html', takes_context=True)
def press_item(context):
    return context
    
 
@register.inclusion_tag('includes/templatetags/press_items_by_category.html', takes_context=True)
def press_items_by_category(context):
    items = PressCategory.objects.all()
    return {
        'objects': items,
    }  
    

def do_get_press_category_items(parser, token):
    """    
    A template tag to retrieve PressCategory by slug.
    
    Example:
    
    {% get_category_press_items "press-release" as category %}
    
    """
    
    import re
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]

    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return PressCategoryNode(format_string[1:-1], var_name)

class PressCategoryNode(template.Node):
    """ """
    
    def __init__(self, slug, var_name):
       self.slug = slug
       self.var_name = var_name

    def render(self, context):
        try:
            category = PressCategory.objects.get(slug=self.slug)
        except PressCategory.DoesNotExist:
            category = None
        
        context[self.var_name] = category
        return ''

register.tag('get_category_press_items', do_get_press_category_items)
