from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from models import Page, Edit

def index(request):
    all_pages = Page.objects.extra(order_by=['title'])
    return render_to_response('wiki/index.html', {'all_pages': all_pages})

def page(request, title):
    page = Page.exist(title)
    if page is None:
        context = {'title': title}
        context.update(csrf(request))
        return render_to_response('wiki/form.html', context)
    return render_to_response('wiki/page.html', {'page': page})

def save(request, title):
    body = request.POST['body']
    page = Page.upsert(title, body)
    comment = request.POST['comment']
    edit = Edit(page=page, comment=comment)
    edit.save()
    return redirect("/wiki/%s" % title)

def edit(request, title):
    page = Page.objects.get(title=title)
    context = {'title': title, 'body': page.body}
    context.update(csrf(request))
    return render_to_response('wiki/form.html', context)

def log(request, title=None):
    if title is None:
        all_edits = Edit.objects.extra(order_by=['-date_created'])
    else:
        all_edits = Edit.objects.filter(page__title=title)
    return render_to_response('wiki/log.html', {'all_edits': all_edits})

