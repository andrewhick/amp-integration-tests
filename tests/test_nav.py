import os
import random
    
# def test_login_and_navigate(py):
#     print('Login details: ' + os.environ.get('AMP_USERNAME') + " " + os.environ.get('AMP_PASSWORD'))
#     py.visit('https://accessibility-monitoring-platform-test.london.cloudapps.digital/')
#     py.get('.govuk-heading-l').should().contain_text('Login')
#     # Invalid password
#     py.get('[name="username"]').type(os.environ.get('AMP_USERNAME'))
#     py.get('[name="password"]').type('cheese')
#     py.get('[value="Submit"]').click()
#     py.get('.govuk-body').should().contain_text('Your username and password didn\'t match.')
#     py.get('[name="username"]').clear()
#     # Valid login
#     # (ideally this would be a repeatable function)
#     py.get('[name="username"]').type(os.environ.get('AMP_USERNAME'))
#     py.get('[name="password"]').type(os.environ.get('AMP_PASSWORD'))
#     py.get('[value="Submit"]').click()
#     py.get('.govuk-heading-xl').should().contain_text('Dashboard')
#     # Go to cases page from link in page body
#     py.get('.govuk-grid-row.dashboard').contains('Cases').click()
#     py.get('.govuk-heading-xl').should().contain_text('Cases and reports')
#     py.get('a[href*="/cases/create"').should().be_visible()
#     py.go('back')
#     # Go to websites page from link in page body
#     py.get('.govuk-grid-row.dashboard').contains('Websites').click()
#     py.get('.govuk-heading-xl').should().contain_text('Query Domain Register')
#     py.get('#id_service').should().be_visible()
#     py.go('back')
#     # Go to account details from header link
#     py.get('a[href*="/user/account_details/"').click()
#     py.get('.govuk-heading-l').should().contain_text('Your account details')
#     py.get('[name="first_name"]').should().be_visible()
#     py.go('back')
#     # Sign out
#     py.get('a[href*="/accounts/logout/"').click()
#     py.get('.govuk-heading-l').should().contain_text('Login')

def test_create_case(py):
    # Test that a case can be created, is searchable, and increments the number of active cases
    py.visit('https://accessibility-monitoring-platform-test.london.cloudapps.digital/')
    # Would prefer to call a function to log in here:
    py.get('[name="username"]').type(os.environ.get('AMP_USERNAME'))
    py.get('[name="password"]').type(os.environ.get('AMP_PASSWORD'))
    py.get('[value="Submit"]').click()
    py.get('.govuk-heading-xl').should().contain_text('Dashboard')

    # Start creating simplified case
    py.get('.govuk-grid-row.dashboard').contains('Cases').click()
    # Get text containing the number of active cases
    cases_text = py.get('.govuk-heading-m').text()
    # Extract the number from it (this is the first item separated by a space)
    original_active_cases = int(cases_text.split(' ')[0])
    py.get('a[href*="/cases/create"').click()
    py.get('.govuk-heading-xl').should().contain_text('Create case')

    # Populate new case details
    py.get('select[name="auditor"]').select('Andrew Hick')
    py.get('[value="simple"]').should().be_checked()
    py.get('[name="home_page_url"]').type("https://www.andrewhick.com/")
    # Generate random organisation name
    test_organisation = "Case " + str(random.randint(0, 999999))
    py.get('[name="organisation_name"]').type("Case " + test_organisation)
    print("Case name: " + test_organisation)
    py.wait(use_py=True).sleep(2)

# todo: add test to create case
# check case has increased by 1 and you can search for it