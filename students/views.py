from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from courses.models import Course, Module, Subject
from .forms import CourseEnrollForm
import shlex, subprocess


class StudentRegistrationView(CreateView):
    template_name = 'students/student_registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super(StudentRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password2'])
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course_list.html'

    def get_queryset(self):
        return super(StudentCourseListView, self).get_queryset().filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(StudentCourseListView, self).get_context_data(**kwargs)
        result = Course.objects.all()
        l = []
        p = []
        c = 0
        a = self.request.user.username
        for s in result:
            l.append(s.students.all())
        for j in l:
            for i in j:
                b = i.username
                if a == b:
                    break
            c += 1
            p.append(c)
        # c =
        # print(c[0].slug)
        v = Course.objects.in_bulk(p)
        context['course_list'] = v.values()
        return context


class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course_detail.html'

    def get_queryset(self):
        return super(StudentCourseDetailView, self).get_queryset().filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        module = Module
        #workspace = User.username
        #cmd = 'yarn theia start /{workspace} --hostname 127.0.0.1 --port 3000 --plugins=local-dir:/home/hari/theia/plugins/'
        #args = shlex.split(cmd)
        # os.system('cd /home/theia;yarn theia start /{workspace} --hostname 0.0.0.0 --port 8080 --plugins=local-dir:/home/hari/theia/plugins/')
        #popen = subprocess.Popen(args, cwd='theia', stdout=subprocess.PIPE, universal_newlines=True)
        if 'module_id' in self.kwargs:
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            context['module'] = module.objects.filter(course=course)
        return context
