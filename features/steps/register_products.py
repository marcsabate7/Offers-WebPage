from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")


@given('Exists a product registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from offers.models import Product
    for row in context.table:
        product = Product(author=user)
        for heading in row.headings:
            setattr(product, heading, row[heading])
        product.save()


@when('I register Product')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('offers:product-create'))
        if context.browser.url == context.get_url('offers:product-create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit and go back to offer').first.click()


@then('There are {count:n} products')
def step_impl(context, count):
    from offers.models import Product
    assert count == Product.objects.count()


@then('I\'m viewing the details page for products by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from offers.models import Product
    product = Product.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(product)
