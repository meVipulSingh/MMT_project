from behave import *
from features.pages.HotelDetailsPage import DetailPage
from features.pages.HotelHomePage import HomePage
from features.pages.HotelPage import HotelPage
from features.pages.HotelPaymentPage import PaymentPage


@given(u'I am on hotel home page')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.get_to_hotel_home_page()


@when(u'I select hotel for destination city')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_on_city_drop_down()
    home_page.selecting_city_from_drop_down("Delhi")


@when(u'I select checkin and checkout date')
def step_impl(context):  # Date selector
    home_page = HomePage(context.driver)
    home_page.checkin_and_checkout_month_and_date("August2024", '15', '24')
    home_page.selecting_guests()
    home_page.clicking_on_search()


@when(u'I choose preferred hotel')
def step_impl(context):
    hotel_page = HotelPage(context.driver)
    hotel_page.searching_for_good_hotel("The imperial")
    hotel_page.selecting_hotel_i_searched_for()
    hotel_page.booking_the_hotel()


@when(u'I provide booking details')
def step_impl(context):
    detail_page = DetailPage(context.driver)
    detail_page.i_provide_booking_details()
    detail_page.i_enter_phone_number("8085886692")


@then(u'I get on payment page')
def step_impl(context):
    payment_page = PaymentPage(context.driver)
    payment_page.i_click_on_pay_now()
