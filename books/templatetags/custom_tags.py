from django import template


register=template.Library()

@register.filter

def average(queryset):
    values=[obj.stars  for obj in queryset if obj.stars  is not None]

    if not values:
        return "no ratings"
    
    return round(sum(values)/len(values),1)






    
    

    
    
