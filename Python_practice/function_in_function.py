def func(x):
    return x*x

def func2(f1, x):
    return f1(x) * x

print(func2(func, 5))


# def html_tag(tag):

#     def wrap_text(msg):
#         print ('<{0}>{1}</{0}>'.format(tag, msg))
    
#     return wrap_text

# use_h1 = html_tag('h1')
# use_h1('Test for t1 bitchoes')






# def logger(msg):

#     def log_message():
#         print ('Log:', msg)

#     return log_message

# log_hi = logger('hi')
# log_hi()