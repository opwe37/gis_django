from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@transaction.atomic
def db_transaction(user, article):
    set_type = 'set'
    like_record = LikeRecord.objects.filter(user=user,
                                            article=article)
    if like_record.exists():
        set_type = 'unset'
        like_record.delete()
        article.like -= 1
    else:
        LikeRecord(user=user, article=article).save()
        article.like += 1

    article.save()
    return set_type


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        set_type = db_transaction(user, article)
        if set_type == 'set':
            messages.add_message(request, messages.INFO, '좋아요가 설정 되었습니다.')
        else:
            messages.add_message(request, messages.INFO, '좋아요가 해제 되었습니다.')

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})