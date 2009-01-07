from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.views.generic import list_detail
from pressbox.models import PressItem

def press_list(request, template_name='pressbox/object_list.html', extra_context={}):
    return render_to_response(template_name, extra_context, RequestContext(request))

def press_regroup(request, template_name='pressbox/object_list_by_category.html', extra_context={}):
    return render_to_response(template_name, extra_context, RequestContext(request))

def press_with_templatetag(request, template_name='pressbox/object_list_by_category_tag.html', extra_context={}):
    return render_to_response(template_name, extra_context, RequestContext(request))

def press_detail(request, slug, template_name='pressbox/object_detail.html', extra_context={}):
    
    return list_detail.object_detail(request,
        queryset = PressItem.objects.active(),
        slug = slug,
        slug_field = "slug",
        template_name = template_name,
        extra_context = extra_context,
    )

