
from behave import *
from QA_Marble.test_google.googlesearch_test import testing_google

@given("Search in google")
def step_impl(context):
    testing_google.setUp()
    testing_google.test_1_navigate_to_google()

@when("I search the word {'wrongword'}")
def step_impl(context, wrongword):
    context.wrongword = wrongword
    testing_google.test_1_navigate_to_google()
    testing_google.test_2_google_search(context.wrongword)

@step("I click on correct word suggestion {'correctword'}")
def step_impl(context, correctword):
    context.correct_word =correctword
    testing_google.test_3_google_correct_search()

@then("I should see more than {'n'} results")
def step_impl(context):
    testing_google.test_4_google_verify_results()
    testing_google.tearDown()
