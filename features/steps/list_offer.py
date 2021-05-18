from behave import *

use_step_matcher("parse")

@when('I list offers')
def step_impl(context):
    context.browser.visit(context.get_url('offers:main'))

@then('I\'m viewing a list containing')
def step_impl(context):
    offers_links = context.browser.find_by_xpath('//html/body/div/article/div/h2/a')
    for i, row in enumerate(context.table):
        assert row['name'] == offers_links[i].text

@step('The list contains {count:n} Offers')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('//html/body/div/article/div/h2/a'))

