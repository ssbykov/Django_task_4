from django.shortcuts import render

from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().prefetch_related('scopes')
    context = {
        'object_list': articles,
    }

    return render(request, template, context)
