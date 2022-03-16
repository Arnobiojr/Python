from django import template
#from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
#@stringfilter
def palavras(string, quantidade):
    resultado = ""
    for contagem in range(int(quantidade)):
        resultado += str(string).split()[contagem]+" "
        
    return str(resultado)