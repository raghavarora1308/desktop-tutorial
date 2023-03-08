def hello_func():
    print('Hello Function!')

hello_func()

def hello_func():
    return 'Hello Function.'

print(hello_func().upper())

def hello_func(greeting):
    return '{} Function'.format(greeting)

print(hello_func('Japnaam'))

def hello_func(greeting,name = 'You'):
    return '{} {}'.format(greeting,name)

print(hello_func('Japnaam',name = 'Corey'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('Math','Art',name = 'John',age = 22)

def is_leap(year):
    return year%4 == 0 and (year%100 != 0   or year%400 == 0)

print(is_leap(2000))

def days_in_month(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month == 2 and is_leap(year):
        return 29
    else:
        return 28

print(days_in_month(2000,2))