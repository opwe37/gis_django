from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])
        if request.user == target_article.writer:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated

