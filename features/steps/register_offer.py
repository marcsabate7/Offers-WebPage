from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")


@given('Exists an offer registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from offers.models import Offer
    for row in context.table:
        offer = Offer(author=user)
        for heading in row.headings:
            setattr(offer, heading, row[heading])
        offer.save()


@when('I register Offer')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('offers:offer-create'))
        if context.browser.url == context.get_url('offers:offer-create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit Offer').first.click()


@then('There are {count:n} offers')
def step_impl(context, count):
    from offers.models import Offer
    assert count == Offer.objects.count()


@then('I\'m viewing the details page for offer by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from offers.models import Offer
    offer = Offer.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(offer)
