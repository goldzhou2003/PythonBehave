from behave import *
# from BehaveTest.utils.utils import *
# from pytest import fail
import os
import sys
sys.path.append('/Users/zhouguosheng/PythonBehave/BehaveTest')

def log(message):
    with open('./log.txt', 'a') as f:
        f.write(message)
        f.write(os.linesep)
        f.flush()

@given('have behave installed')
def step_impl(context):
    log('in given')
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):
    log('in when')
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    log('in then')
    assert context.failed is False
    assert context.tests_count >= 0


@given(u'login page open')
def step_impl(context):
    log('open login page here ?')
    pass

@when(u'input user name {username} and pass {pw}')
def step_impl(context, username, pw):
    log('try input user name and pass')
    assert username == 'test'
    assert pw == '1234'

@then(u'login into page')
def step_impl(context):
    log('check if login')
    assert context.failed is False

# @given(u'had something')
# def step_impl(context):
#     pass
#
# @given(u'had something else')
# def step_impl(context, str):
#     pass
#
# @then(u'this is {str}')
# def step_impl(context, str):
#     log(str)
#     pass

@given(u'look up a book')
def step_impl(context):
    pass

@given(u'look up an invalid book')
def step_impl(context):
    pass

@then('the result page will include "{text}"')
def step_impl(context, text):
    if text not in context.response:
        # fail('%r not in %r' % (text, context.response))
        log('%r not in %r' % (text, context.response))