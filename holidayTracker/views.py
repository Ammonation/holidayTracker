from django.http import HttpResponse
from django.template import loader


def frontPage(self):
    template=loader.get_template('harbon/frontPage.html')
    return HttpResponse(template.render())
