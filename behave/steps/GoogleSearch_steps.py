"""
Given The word "<wrongword>"
When I search that word in google
And Google returns the word "<correctword>" as suggestion
And I click on the "<correctword>"
Then I should see more than "<n>" results
"""

@given("Given The word '{wrongword}'")
def step_impl(context):
    pass

@when("I search that word in google")
def step_impl(context):
    pass

@step("Google returns the word '{correctword>' as suggestion")
def step_impl(context):
    pass

@step("I click on correct word '{correctword}'")
def step_impl(context):
    pass

@then("I should see more than {'n'} results")
def step_impl(context):
    pass
