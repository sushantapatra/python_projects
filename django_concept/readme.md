### create Hyperlinks and URL Tag

## way 1
urlpatterns =[
    path('/about', views.about),
]
<a href="/about">About</a>

## way 2
def about(request):
    return render(request, 'core/about.html',{'ab':'/about'})
urlpatterns =[
    path('/about', views.about),
]
<a href="{{ ab }}">About</a>

## way 3
urlpatterns =[
    path('/about', views.about, name="aboutus"),
]
<a href="{% url 'aboutus' %}">About</a>
"""  OR """  
{% url 'aboutus' as abpage %}
<a href="{{ abpage }}">About</a>


### create Model Form
from django.contrib import admin
from courses.models import Course , Payment , UserCourse , Tag , Prerequisite , Learning , Video
from django.utils.html import format_html
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.TabularInline):
    model = Video

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin , PrerequisiteAdmin , VideoAdmin]
    list_display = ["name" , 'get_price' , 'get_discount' , 'active']
    list_filter = ("discount" , 'active')

    def get_discount(self , course):
        return f'{course.discount} %'
    
    def get_price(self , course):
        return f'₹ {course.price}'
    
    get_discount.short_description= "Discount"
    get_price.short_description = "Price"

class PaymentAdmin(admin.ModelAdmin):
    model = Payment   
    list_display = [ "order_id" , 'get_user' , 'get_course' , 'status'] 
    list_filter = ["status" , 'course']

    def get_user(self , payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")
    

    def get_course(self , payment):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{payment.course.id}'>{payment.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"


class UserCourseAdminModel(admin.ModelAdmin):
    model = UserCourse   
    list_display = ['click' , 'get_user' , 'get_course'] 
    list_filter = ['course']

    def get_user(self , usercourse):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{usercourse.user.id}'>{usercourse.user}</a>")
    
    def click(self , usercourse):
        return "Click to Open"
    

    def get_course(self , usercourse):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{usercourse.course.id}'>{usercourse.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"

admin.site.register(Course , CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment , PaymentAdmin)
admin.site.register(UserCourse , UserCourseAdminModel)
