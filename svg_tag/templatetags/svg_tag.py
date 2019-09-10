from django import template
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from lxml import html
from scour import scour

register = template.Library()


def get_scour_options():
    options = scour.sanitizeOptions()
    options.remove_descriptions = True
    options.remove_descriptive_elements = True
    options.remove_metadata = True
    options.remove_titles = True
    options.shorten_ids = False
    options.strip_comments = True
    options.strip_xml_prolog = True
    options.strip_xml_space_attribute = True
    return options


@register.simple_tag()
def svg_tag(svg):
    t = get_template(svg)
    if t.template.source:
        svg_source = t.template.source
    else:
        svg_source = open(t.template.origin.name, 'r').read()
    scour_options = get_scour_options()
    scour_string = scour.scourString(svg_source, options=scour_options)
    lxml_object = html.fragment_fromstring(str(scour_string))
    for fill_node in lxml_object.cssselect('[fill]'):
        if getattr(fill_node.attrib, 'fill', None):
            del fill_node.attrib.fill
    svg_out = html.tostring(lxml_object, encoding='unicode')
    return mark_safe(svg_out)
