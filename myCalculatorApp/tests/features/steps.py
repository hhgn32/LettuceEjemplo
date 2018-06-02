from lettuce import *
from nose.tools import assert_equals
from calculator import Calculator

@step(u'Given: I am using the calculator')
def i_am_using_the_calculator(step):
    print ('Attempting to use calculator...')
    world.calc = Calculator()

#Scenario: Calculate 2 plus 2 on our calculator (verbose)

@step('Given: I have the first number (\d+)')
def have_the_number(step, x):
    world.number1 = int(x)

@step('And: I have the second number (\d+)')
def have_the_number(step, y):
    world.number2 = int(y)

@step(u'When: I input (\d+) add (\d+)')
def i_input_add(step, x, y):
    world.result = world.calc.add(world.number1 , world.number2)

@step(u'Then: I should see (\d+)')
def I_should_see(step, expected_result):
    actual_result = world.result
    assert_equals(int(expected_result), actual_result)


#Scenario: Calculate 2 plus 2 on our calculator

@step(u'I input "([^"]*)" add "([^"]*)"')
def given_i_input_group1_add_group1(step, x, y):
    world.result = world.calc.add(int(x), int(y))

@step(u'I should see "([^"]+)"')
def result(step, expected_result):
    actual_result = world.result
    assert_equals(int(expected_result), actual_result)


#Scenario: Calculate 1 minsinweeks on our calculator

@step('Given: I have the week number (\d+)')
def have_the_number(step, x):
    world.number = int(x)

@step(u'When: I input (\d+) minsinweeks')
def i_input_add(step, x):
    world.result = world.calc.minsinweeks(world.number)

@step(u'Then: I should see (\d+)')
def I_should_see(step, expected_result):
    actual_result = world.result
    assert_equals(int(expected_result), actual_result)


#Scenario: Calculate 2304811 / 47 module with out % calculator

@step('Given: I have the week number (\d+)')
def have_the_number(step, x):
    world.number=int(x)

@step(u'When: I input (\d+) task_052')
def i_input_add(step, x):
    world.result = world.calc.task_052(world.number1)

@step(u'Then: I should see (\d+)')
def I_should_see(step, expected_result):
    actual_result = world.result
    assert_equals(int(expected_result), actual_results)
