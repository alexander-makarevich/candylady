# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext as _
from schedule.models import Lesson

class SchedulePlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Schedule Plugin")
    render_template = "plugin.html"

    def render(self, context, instance, placeholder):
        #собираю по дням
        lessons_by_day = {}
        for lesson in Lesson.objects.all():
            if not lesson.day in lessons_by_day:
                lessons_by_day[lesson.day] = []
            lessons_by_day[lesson.day].append(lesson)

        #отсортировали по времени внутри дня
        for day in lessons_by_day:
            lessons_by_day[day].sort(key=lambda lesson: lesson.start)

        #отсортировали по дням
        lessons = []
        days = [
            u'Понедельник', u'Вторник', u'Среда', u'Четверг',
            u'Пятница', u'Суббота', u'Воскресение'
        ]
        for day in days:
            if day in lessons_by_day:
                lessons.append(lessons_by_day[day])

        context.update({
            'lessons_by_day': lessons
        })
        return context

plugin_pool.register_plugin(SchedulePlugin)

