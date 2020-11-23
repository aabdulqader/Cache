from django.shortcuts import render
from django.core.cache import cache



# def home(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == "has_expired":
#         cache.set('movie', 'the one', 30)
#         mv = cache.get('movie')
#     return render (request, 'course.html', {'mv':mv})




# def home(request):
#     mv = cache.get_or_set('movie', '40000', 30, version=2)
#     return render (request, 'course.html', {'mv':mv})




# def home(request):
#     data = {'name':'shimul', 'roll':201}
#     cache.set_many(data, 40)
#     sv = cache.get_many(data)
#     return render (request, 'course.html', {'sv':sv})


# def home(request):
#     # cache.delete('movie', version=2)
#     cache.delete('roll')
#     return render (request, 'course.html')


# def home(request):
#     cache.set('roll', '101', 30)
#     rv = cache.get('roll')
#     return render (request, 'course.html',{'rv':rv})


# def home(request):
#     # cache.set('roll', '101', 600)
#     rv = cache.decr('roll', delta=2)
#     rv = cache.incr('roll', delta=2)
#     print(rv)
#     return render (request, 'course.html')


def home(request):
    cache.clear()
    return render (request, 'course.html')

### delete it from shell...
    # python manage.py shell
    # from django.core.cache import cache
    # cache.clear()
    # quit()

















