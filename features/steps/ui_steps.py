from behave import given, when, then
from src.ui.pages.search_page import SearchPage
from src.ui.pages.search_result_page import SearchResultsPage


@given(u'I navigate to SDAIA homepage')
def step_impl(context):
    context.spage = SearchPage(context.driver)
    base_url = context.cfg["ui"]["base_url"]
    context.spage.open_url(base_url)

@when(u'I click on search icon')
def step_impl(context):
    context.spage.click("search_icon_XPATH", True)

@when(u'I enter the search term "{search_term}"')
def step_impl(context, search_term):
    context.search_term = search_term
    context.spage.type("search_field_XPATH",search_term)

@when(u'I click on the search button')
def step_impl(context):
    context.spage.click("search_button_XPATH", True)

@then(u'I validate search results')
def step_impl(context):
    context.rpage = SearchResultsPage(context.driver)
    results = context.rpage.get_search_results()
    if context.rpage.validate_search_results(results, context.search_term):
        assert True
    else:
        assert False

@then(u'I should not be able to search')
def step_impl(context):
    if context.spage.validate_search_error():
        assert True
    else:
        assert False

@when(u'I enter a random search term')
def step_impl(context):
    context.search_term = context.spage.generate_random_string(10)
    context.spage.type("search_field_XPATH",context.search_term)

@then(u'I should not get any results')
def step_impl(context):
    if context.spage.validate_no_elements("no_results_XPATH"):
        assert True
    else:
        assert False

@when(u'I enter a select a suggested search term')
def step_impl(context):
    context.search_term = context.spage.select_suggestion()

@when(u'I enter an "{length_str}" characters long search term')
def step_impl(context, length_str):
    length = int(length_str)
    context.search_term = context.spage.generate_random_string(length)
    context.spage.type("search_field_XPATH", context.search_term)

@then(u'I validate error page')
def step_impl(context):
    if context.spage.validate_error_page():
        assert True
    else:
        assert False