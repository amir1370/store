from django import template

register = template.Library()


@register.filter
def list_item(lst, i):
    try:
        return lst[i]
    except:
        return None

@register.filter
def list_item_brand(lst, i):
    try:
        return lst[i].brand
    except:
        return None

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()