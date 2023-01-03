from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from ecommerce.apps.orders.models import Order

from .forms import CommentForm


@login_required
def post_comment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    try:
        m=order.comments
        messages.success(request, "您不能重复评价！")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    except:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.order = order
                new_comment.save()
                return redirect(reverse("account:user_orders"))
            else:
                return HttpResponse("出错啦，请重试。")

        elif request.method == 'GET':
            return render(request, 'comment/post_comment.html')
        else:
            return HttpResponse("请使用POST 或 GET。")
