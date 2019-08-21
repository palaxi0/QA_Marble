
from behave import *
from test_google.googlesearch_test import testing_google

@given('Search in google')
def step_impl(context):
    testing_google.setUp()
    testing_google.test_1_navigate_to_google()

@when('I search the word "{wrongword}"')
def step_impl(context, wrongword):
    context.word = wrongword
    testing_google.test_2_google_search(context.word)

@step('I click on correct word suggestion "{correctword}"')
def step_impl(context, correctword):
    context.correct_word = correctword
    testing_google.test_3_google_correct_search()

@then('I should see more than "{n}" results')
def step_impl(context, n):
    context.n = n
    testing_google.test_4_google_verify_results(context.n)
    testing_google.tearDown()
