import smtplib

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mass_mail, send_mail
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import *
from django.utils.html import strip_tags
from django.views.generic import View


# if 页数>=10:
#     当前页<=5时，起始页为1
#     当前页>(总页数-5)时，起始页为(总页数-9)
#     其他情况 起始页为(当前页-5)
def get_page_list(paginator, page):
    page_list = []
    if paginator.num_pages > 10:
        if page.number <= 5:
            start_page = 1
        elif page.number > paginator.num_pages - 5:
            start_page = paginator.num_pages - 9
        else:
            start_page = page.number - 5

        for i in range(start_page, start_page + 10):
            page_list.append(i)
    else:
        for i in range(1, paginator.num_pages + 1):
            page_list.append(i)

    return page_list


def ajax_required(f):
    """Not a mixin, but a nice decorator to validate than a request is AJAX"""

    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
