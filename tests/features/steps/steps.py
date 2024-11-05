from behave import given, when, then

def f(x, y):
    return x + y

@given('two numbers {x:d} and {y:d}')
def step_given_two_numbers(context, x, y):
    context.x = x
    context.y = y

@when('they are added')
def step_when_added(context):
    context.result = f(context.x, context.y)

@then('the result should be {expected:d}')
def step_then_result_should_be(context, expected):
    assert context.result == expected, f"Правильный - {expected}, но получили - {context.result}"
