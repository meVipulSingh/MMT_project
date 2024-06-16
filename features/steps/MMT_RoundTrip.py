from behave import *
from features.pages.FlightDetailsPage import DetailsPage
from features.pages.FlightPage import FlightPage
from features.pages.FlightHomePage import HomePage
from features.pages.LoginPage import LoginPage
from features.pages.FlightPaymentPage import PaymentPage


@given(u'I am on flight home page')
def step_impl(context):
    home_Page = HomePage(context.driver)
    home_Page.get_to_the_flight_homepage()


@when(u'I login to the page')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_on_login_button()
    login_page.click_on_sign_in_button()
    login_page.enter_email_id("vipulxyz2@gmail.com")
    login_page.enter_password("Vipul123@")
    login_page.close()


@when(u'I select destinations for round trip')
def step_impl(context):
    home_Page = HomePage(context.driver)
    home_Page.click_on_round_trip()
    home_Page.from_city("Mumbai, India")
    home_Page.to_city("New Delhi, India")


@when(u'I choose departure and return date')
def step_impl(context):  # Date selector
    home_Page = HomePage(context.driver)
    home_Page.departure_and_return_month_date("August2024", '15', '24')
    home_Page.click_on_search()


@when(u'I choose my flights')
def step_impl(context):
    flight_page = FlightPage(context.driver)
    flight_page.add_handle()
    flight_page.flights_selection_from_departure_city_to_return_city()
    flight_page.book_now()


@when(u'I provide passenger detail')
def step_impl(context):
    detail_page = DetailsPage(context.driver)
    detail_page.adding_passenger_details()
    detail_page.first_name("Vipul")
    detail_page.last_name("Kumar")
    detail_page.gender_selection()
    detail_page.enter_phone_number("8085886692")
    detail_page.click_to_continue()


@then(u'I get to the payment gateway')
def step_impl(context):
    payment_page = PaymentPage(context.driver)
    payment_page.review_details()
    payment_page.yes_please()
    payment_page.skip_to_add_ons()
    payment_page.proceed_to_pay()
