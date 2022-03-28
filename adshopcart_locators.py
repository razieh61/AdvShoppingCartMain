import datetime

from faker import Faker
fake = Faker(locale=['en_CA','en_US'])

#-------- AdvantageShoppingCart App DATA PARAMETERS ----------------
app = 'AdvantageShoppingCart'
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_home_page_title = ' Advantage Shopping'
adshopcart_signup_page_url = 'https://advantageonlineshopping.com/#/register'
adshopcart_myaccount_url = 'https://advantageonlineshopping.com/#/myAccount'
adshopcart_myorders_url = 'https://advantageonlineshopping.com/#/MyOrders'

new_username = fake.user_name()
new_password = fake.password(length=12)
email = fake.email()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phonenum = fake.phone_number()
country = fake.current_country()
city = fake.city()
address = fake.street_address()
state = fake.province_abbr()
postal_code = fake.postalcode()