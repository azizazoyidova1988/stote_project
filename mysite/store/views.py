from django.shortcuts import render, redirect
from . import services
from store.models import Teams, Commenter,  Contact
from .forms import CommenterForm, ContactForm
from django.core.paginator import Paginator, EmptyPage

var = [{
    "title": "About Us",
    "image1": "../static/store/images/post-2.jpg",
    "image2": "../static/store/images/44.jpg",
    "desc": "Far far away, behind the word mountains, ' \
        'far from the countries Vokalia and Consonantia,' \
        ' there live the blind texts. Separated they live ' \
        'in Bookmarksgrove right at the coast of the ' \
        'Semantics, a large language ocean. Sed porttitor lectus nibh.' \
        ' Vivamus magna justo, lacinia eget consectetur sed, convallis at ' \
        'tellus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. ' \
        'Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus."
}]


def home(request):
    model = Contact()
    form = ContactForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    projects = services.get_projects()
    service = services.get_services()
    teams = services.get_teams()
    blog = services.get_news()
    testimonials = services.get_testimonials()

    ctx = {
        "index": 'active',
        "projects": projects,
        "teams": teams,
        "service": service,
        "testimonials": testimonials,
        'var': var,
        "blog": blog
    }
    return render(request, 'store/index.html', ctx)


def about(request):
    teams = Teams.objects.all().order_by("-created_at")[4:]
    testimonials = services.get_testimonials()
    ctx = {
        "about": 'active',
        "var": var,
        "teams": teams,
        'testimonial': testimonials
    }
    return render(request, 'store/about.html', ctx)


def blog(request):
    blogs = services.get_posts()
    p = Paginator(blogs, 3)
    page_num = request.GET.get('page', 1)
    total_pages = len(blogs)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    ctx = {
        "blog": 'active',
        "blogs": blogs,
        "page": page,
        "page_num": page_num,
        "total_pages": total_pages

    }
    return render(request, 'store/blog.html', ctx)


def blog_single(request, news_id):
    model = Commenter()
    form = CommenterForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()

    new = services.get_news_by_id(news_id=news_id)
    blogs = services.get_posts()
    commenter = services.get_commenter()
    comment_limit = services.get_commenter_by_limit()
    length_comment = len(commenter)
    ctx = {
        "blog-single": 'active',
        "commenter": commenter,
        "new": new,
        'blogs': blogs,
        'comment_limit': comment_limit,
        'length': length_comment

    }
    return render(request, 'store/blog-single.html', ctx)


def project(request):
    model = Contact()
    form = ContactForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()

    projects = services.get_projects()
    p = Paginator(projects, 3)
    page_num = request.GET.get('page', 1)
    total_pages = len(projects)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    ctx = {
        "project": 'active',
        "projects": projects,
        "page": page,
        "page_num": page_num,
        "total_pages": total_pages,



    }
    return render(request, 'store/project.html', ctx)


def project_single(request, project_id):
    model = Commenter()
    form = CommenterForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()

    product = services.get_products_by_id(project_id=project_id)
    teams = services.get_team_by_limit()
    print(teams)
    ctx = {
        "property-single": 'active',
        "product": product,
        "teams": teams,

    }
    return render(request, 'store/project-single.html', ctx)


def teams(request):
    teams = services.get_teams()
    p = Paginator(teams, 3)
    page_num = request.GET.get('page', 1)
    total_pages = len(teams)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    ctx = {
        "team": 'active',
        "teams": teams,
        "page": page,
        "page_num": page_num,
        "total_pages": total_pages

    }
    return render(request, 'store/team.html', ctx)



def contact(request):
    model = Contact()
    form = ContactForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)
    ctx = {
        "contact": 'active',

    }
    return render(request, 'store/contact.html', ctx)
