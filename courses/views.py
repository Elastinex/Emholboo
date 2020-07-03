from django.template import RequestContext
from django.shortcuts import render_to_response
import secrets
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from src.courses.models import Subject, Lesson, Course
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CourseForm, LendaForm, MesimiForm
# Create your views here.


class HomeView(TemplateView):
    template_name = 'course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Course.objects.all()
        context['category'] = category
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


def CourseListView(request, category):
    courses = Subject.objects.filter(course=category)
    context = {
        'courses': courses
    }
    return render(request, 'courses/course_list.html', context)


class CourseDetailView(DetailView):
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
    model = Subject


class LessonDetailView(View, LoginRequiredMixin):
    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course = get_object_or_404(Subject, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        context = {'lesson': lesson}
        return render(request, "courses/lesson_detail.html", context)


@login_required
def SearchView(request):
    if request.method == 'POST':
        kerko = request.POST.get('search')
        results = Lesson.objects.filter(title__contains=kerko)
        context = {
            'results': results
        }
        return render(request, 'courses/search_result.html', context)


@login_required
def krijo_klase(request):
    if not request.user.profile.is_teacher == True:
        messages.error(
            request, f'Llogaria juaj nuk ka akses ne kete url vetem llogarite e mesuesve!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Course juaj u krijua.')
            return redirect('courses:home')
    else:
        form = CourseForm()
    context = {
        'form': form
    }
    return render(request, 'courses/krijo_klase.html', context)


@login_required
def krijo_lende(request):
    if not request.user.profile.is_teacher == True:
        messages.error(
            request, f'Llogaria juaj nuk ka akses ne kete url vetem llogarite e mesuesve!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = LendaForm(request.POST)
        if form.is_valid():
            form.save()
            course = form.cleaned_data['course']
            slug = course.id
            messages.success(request, f'Lenda juaj u krijua.')
            return redirect('/courses/' + str(slug))
    else:
        form = LendaForm(
            initial={'user': request.user.id, 'slug': secrets.token_hex(nbytes=16)})
    context = {
        'form': form
    }
    return render(request, 'courses/krijo_lende.html', context)


@login_required
def krijo_mesim(request):
    if not request.user.profile.is_teacher == True:
        messages.error(
            request, f'Llogaria juaj nuk ka akses ne kete url vetem llogarite e mesuesve!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = MesimiForm(request.POST)
        if form.is_valid():
            form.save()
            lenda = form.cleaned_data['lenda']
            slug = lenda.slug
            messages.success(request, f'Mesimi juaj u krijua.')
            return redirect('/courses/' + str(slug))
    else:
        form = MesimiForm(initial={'slug': secrets.token_hex(nbytes=16)})
    context = {
        'form': form
    }
    return render(request, 'courses/krijo_mesim.html', context)


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

# def get(self,request,course_slug,lesson_slug,*args,**kwargs):
#
#     course_qs = Course.objects.filter(slug=course_slug)
#     if course_qs.exists():
#         course = course_qs.first()
#     lesson_qs = course.lessons.filter(slug=lesson_slug)
#     if lesson_qs.exists():
#         lesson = lesson_qs.first()
#     user_membership = UserMembership.objects.filter(user=request.user).first()
#     user_membership_type = user_membership.membership.membership_type
#
#     course_allowed_membership_type = course.allowed_memberships.all()
#     context = {'lessons':None}
#
#     if course_allowed_membership_type.filter(membership_type=user_membership_type).exists():
#         context = {'lesson':lesson}
#
#     return render(request,'courses/lesson_detail.html',context)
