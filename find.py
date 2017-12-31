from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import getpass

def send_email():
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(GMAIL_ACCOUNT, GMAIL_PASSWORD)
    server.sendmail( 'BoYu Mac', 'jyt0532@gmail.com', 'New seat open' )

def check_available(pswd):
    browser = webdriver.Firefox()
    browser.get('https://www.united.com/ual/en/us/account/account/signin')


    username = browser.find_element_by_id("MpNumber")
    password = browser.find_element_by_id("Password")

    username.send_keys(UNITED_ACCOUNT)
    password.send_keys(pswd)

    browser.find_element_by_id("btnSignIn").click()

    browser.get('https://www.united.com/ual/en/tw/mytrips/trips/flightseats?cn=XXX')

    availables = browser.find_elements_by_class_name('available')

    for item in availables:
        text = item.text
        if "Economy Plus" not in text and "Window" in text and "premium cabin" not in text:
            print "Got it"
            send_email()
            break
    print "First flight Not found"

    browser.get('https://www.united.com/web/en-US/apps/booking/flight/seatSelector.aspx?sk=1')

    availables = browser.find_elements_by_class_name('available')

    for item in availables:
        text = item.text
        if "Economy Plus" not in text and "Window" in text and "premium cabin" not in text:
            print "Got it"
            send_email()
            break

    print "Second flight Not found"
    browser.close()

if __name__ == "__main__":
    pswd = getpass.getpass('Password:')
    check_available(pswd)
