from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template


@login_required(login_url="/login/")
def index(request):
    return render(request, "index2.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def uploadFile(request):
    if 'inputDescription' in request.POST:
        mapname = request.POST['inputDescription']
        if not mapname:
            return HttpResponse("missing value for map name")
        else:
            return HttpResponse("%s" % mapname)
    else:
        return HttpResponse("missing map name")
