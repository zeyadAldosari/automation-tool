from behave import given, when, then
from src.api.client import Client
from src.api.token import TokenStore
from src.api.schema_validator import validate_schema
from src.api.schemas import (
    AUTH_LOGIN_SUCCESS_SCHEMA, AUTH_ME_SCHEMA, AUTH_ERROR_SCHEMA
)

@given("I have valid credentials")
def step_valid_creds(context):
    context.client = Client(context.cfg["api"]["base_url"])
    context.username = "emilys"
    context.password = "emilyspass"
    context.token_store = TokenStore()

@given("I have invalid credentials")
def step_invalid_creds(context):
    context.client = Client(context.cfg["api"]["base_url"])
    context.username = "wronguser"
    context.password = "badpass"
    context.token_store = TokenStore()

@when("I login")
def step_login(context):
    resp = context.client.login(context.username, context.password)
    context.response = resp
    context.body = resp.json()
    if resp.status_code == 200:
        validate_schema(context.body, AUTH_LOGIN_SUCCESS_SCHEMA, where="/auth/login")
        context.token_store.set(context.body.get("accessToken"))

@then("I receive an access token")
def step_assert_token(context):
    assert context.response.status_code == 200, f"Expected 200, got {context.response.status_code}"
    assert context.token_store.get(), "No accessToken found in response"

@then("I see an authentication error")
def step_auth_error(context):
    assert context.response.status_code != 200, f"Expected non-200 for invalid login"
    try:
        validate_schema(context.body, AUTH_ERROR_SCHEMA, where="auth error")
    except Exception:
        pass

@given("I am logged in")
def step_logged_in(context):
    context.execute_steps(u"""
        Given I have valid credentials
        When I login
        Then I receive an access token
    """)

@when("I fetch current user data")
def step_me(context):
    token = context.token_store.get()
    resp = context.client.me(token)
    context.response = resp
    context.body = resp.json()
    if resp.status_code == 200:
        validate_schema(context.body, AUTH_ME_SCHEMA, where="/auth/me")

@then("I receive user information")
def step_user_info(context):
    assert context.response.status_code == 200, f"Expected 200, got {context.response.status_code}"
    assert isinstance(context.body, dict), "User info is not a JSON object"

@then('it includes a "{key}" field')
def step_has_field(context, key):
    assert key in context.body, f"Missing field {key} in user_info"
