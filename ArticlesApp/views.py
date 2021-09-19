from django.shortcuts import redirect
from django.urls import reverse_lazy
from ArticlesApp.decorator import author_required
from ArticlesApp.models import Author, Article, Image, Equipment
from UsersApp.models import Badge
from ArticlesApp.article_app_form import ArticleCreationForm, ImageUploadForm, EquipmentForm
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

# CRUD for Article table


@method_decorator([login_required, author_required], name='dispatch')
class BibliographyView(ListView):
    model = Article
    ordering = ('title', )
    template_name = 'ArticlesApp/bibliography.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Article.objects.filter(author=self.request.user.id_account)
        return queryset


@login_required
@author_required
def article_create_view(request):
    """
        Create article with user and images relationship
    """

    image_form_set = modelformset_factory(Image, form=ImageUploadForm, extra=5)
    equipment_form_set = modelformset_factory(Equipment, form=EquipmentForm, extra=15)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        post_form = ArticleCreationForm(request.POST)
        formset = image_form_set(request.POST, request.FILES, queryset=Image.objects.none())
        formset_equipment = equipment_form_set(request.POST, request.FILES, queryset=Equipment.objects.none())

        if post_form.is_valid() and formset.is_valid() and formset_equipment.is_valid():
            form_post = post_form.save(commit=False)
            form_post.user = request.user
            article_instance = post_form.save()
            image_instances = formset.save()
            equipment_instances = formset_equipment.save()

            # many to many relationship of article with author_bibliography
            print('request.user.id_account ', request.user.id_account)
            qs_username = Author.objects.get(account_author_id=request.user.id_account)
            print('qs_username', qs_username)
            print('article_instance', article_instance)
            qs_username.bibliography.add(article_instance)
            # many to many relationship of all images with article_list_image
            for image_instance in image_instances:
                article_instance.list_image.add(image_instance)

            # many to many relationship of article with equipment for all equipment list
            for equipment in equipment_instances:
                article_instance.list_equipement.add(equipment)

            messages.success(request,
                             "Yeeew, check it out on the home page!")

            return HttpResponseRedirect("/")
        else:
            print(post_form.errors, formset.errors)
    else:
        post_form = ArticleCreationForm()
        formset = image_form_set(queryset=Image.objects.none())
        formset_equipment = equipment_form_set(queryset=Equipment.objects.none())

    return render(request, 'ArticlesApp/article_create.html', {'postForm': post_form, 'formset': formset,
                                                               'formset_equipment': formset_equipment})


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
    fields = '__all__'
    template_name = 'ArticlesApp/article_update.html'

    def get_success_url(self):
        view_name = 'author_home'
        return reverse_lazy(view_name)


@method_decorator([login_required, author_required], name='dispatch')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'ArticlesApp/article_confirm_delete.html'
    success_url = reverse_lazy('author_home')

########################################################################################################################
# CRUD for Badge model


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
    success_url = reverse_lazy('badge_list')

