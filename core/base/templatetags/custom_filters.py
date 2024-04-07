from django import template

register = template.Library()


def month_abbr(date):
    return date.strftime("%b")


def eventsContentFormat(para):
    words = para.split()
    if len(words) > 55:
        return ' '.join(words[:55]) + "..."
    else:
        return para


register.filter('month_abbr', month_abbr)
register.filter('formatContent', eventsContentFormat)
