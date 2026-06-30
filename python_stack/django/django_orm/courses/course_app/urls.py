from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='courses_dashboard'),                  # الصفحة الرئيسية (الفورم والجدول معاً)
    path('create', views.create, name='create_course'),       # معالجة إضافة كورس جديد
    path('destroy/<int:course_id>', views.confirm_delete, name='confirm_delete'), # صفحة تأكيد الحذف
    path('destroy/<int:course_id>/delete', views.delete, name='delete_course'),   # الحذف الفعلي
    path('<int:course_id>/comment', views.add_comment, name='add_comment'), # بونص إضافة تعليق
]