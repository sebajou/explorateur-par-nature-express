from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as account_logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ArticlesApp.decorator import author_required
from ArticlesApp.models import Author, Article
from UsersApp.models import Badge
from ArticlesApp.article_app_form import ArticleCreationForm
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.utils.decorators import method_decorator


@method_decorator([login_required, author_required], name='dispatch')
class BibliographyView(ListView):
    model = Article
    ordering = ('title', )
    context_object_name = 'bibliography'
    template_name = 'ArticlesApp/bibliography.html'

    def get_queryset(self):
        queryset = self.request.user.bibliography \
            .select_related('username')
        return queryset


@method_decorator([login_required, author_required], name='dispatch')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'ArticlesApp/article_create.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.bibliography = self.request.user
        article.save()
        messages.success(self.request, 'The article was created with success!')
        return redirect('ArticlesApp/article_create.html', article.pk)


@method_decorator([login_required], name='dispatch')
class ArticleReadView(DetailView):
    model = Article
    template_name = 'ArticlesApp/article_read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator([login_required, author_required], name='dispatch')
class ArticleUpdateView(UpdateView):
    model = Article
    pass


@method_decorator([login_required, author_required], name='dispatch')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'ArticlesApp/article_delete.html'
    success_url = reverse_lazy('views:bibliography')

    def delete(self, request, *args, **kwargs):
        article = self.get_object()
        messages.success(request, 'The article %s was deleted with success!' % article.title)
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.bibliography.all()

########################################################################################################################


@method_decorator([login_required, author_required], name='dispatch')
class BadgeListView(ListView):
    model = Badge
    ordering = ('title', )
    template_name = 'ArticlesApp/badge_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Badge.objects.all()
        return queryset


@method_decorator([login_required, author_required], name='dispatch')
class BadgeCreateView(CreateView):
    model = Badge
    # form_class = ArticleCreationForm
    fields = ('title', 'category', 'level', 'image_badge')
    template_name = 'ArticlesApp/badge_create.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('badge_list')


@method_decorator([login_required], name='dispatch')
class BadgeReadView(DetailView):
    model = Badge
    template_name = 'ArticlesApp/badge_read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator([login_required, author_required], name='dispatch')
class BadgeUpdateView(UpdateView):
    model = Badge
    fields = ['title', 'category', 'level', 'image_badge']
    template_name = 'ArticlesApp/badge_update.html'

    def get_success_url(self):
        view_name = 'badge_list'
        return reverse_lazy(view_name)


@method_decorator([login_required, author_required], name='dispatch')
class BadgeDeleteView(DeleteView):
    model = Badge
    # template_name = 'ArticlesApp/badge_confirm_delete.html'
    success_url = "/"
    # success_url = reverse_lazy('badge_list')
    # context_object_name = 'badge'
    # success_url = reverse_lazy('views:badge_list')
    #
    # def delete(self, request, *args, **kwargs):
    #     badge = self.get_object()
    #     messages.success(request, 'The article %s was deleted with success!' % badge.title)
    #     return super().delete(request, *args, **kwargs)
