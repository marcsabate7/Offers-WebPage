from behave import *

use_step_matcher("parse")


@when('I view the details for offer "{name}"')
def step_impl(context, name):
    from offers.models import Offer
    offer = Offer.objects.get(product_name=name)
    context.browser.visit(context.get_url(offer))


@when('I edit the offer with name "{name}"')
def step_impl(context, name):
    from offers.models import Offer
    offer = Offer.objects.get(name=name)
    context.browser.visit(context.get_url('offers:offer-update', offer.pk))
    if context.browser.url == context.get_url('offers:offer-update', offer.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit Offer').first.click()