import datetime
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
    # Get text containing the number of active cases, e.g. "372 active cases"
    cases_text = py.get('.govuk-heading-m').text()
    # Extract the number from it (this is the first item separated by a space)
    original_active_cases = int(cases_text.split(' ')[0])
    print("Number of cases: " + str(original_active_cases))
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
    py.get('[value="public"]').check()
    py.get('select[name="sector"]').select('Local Government')
    py.get('#id_region_0').check() # Selects England
    py.get('[value="list"').check() # Selects "Website list"
    py.get('#id_trello_url').type('https://www.example.com/trello')
    py.get('#id_notes').type('This case has been automatically generated while running tests on the monitoring platform')
    py.get('[name="save_exit"]').click()

    # View case
    py.get('.govuk-heading-xl').should().contain_text('View case #')
    # Get case number
    case_number_text = py.get('.govuk-heading-xl').text()
    case_number = int(case_number_text.split('#')[1]) # Gets the case number after the '#' character
    print('Case number: ' + str(case_number))
    py.get('.govuk-grid-column-two-thirds').should().contain_text(test_organisation)

    # Check number of cases has increased by 1
    py.get('a[href="/"]').click()
    py.get('.govuk-grid-row.dashboard').contains('Cases').click()
    cases_text = py.get('.govuk-heading-m').text()
    new_active_cases = int(cases_text.split(' ')[0])
    print("Number of cases: " + str(new_active_cases))
    assert new_active_cases == original_active_cases + 1

    # Search for case
    py.get('#id_organisation').type(test_organisation)
    py.get('[value="Search"]').click()

    # Check that case appears in results with case number and today's date
    py.get('.govuk-table').should().contain_text('Case #' + str(case_number))
    py.get('.govuk-table').should().contain_text(test_organisation)
    py.get('.govuk-table').should().contain_text(datetime.datetime.now().strftime('%d/%m/%Y'))
    py.get('.govuk-heading-m').should().contain_text('1 cases found')
    # Access the case
    py.get('a[href*="/view"]').click()
    # TODO Unlist case
    # TODO Check that case no longer appears in results
    py.wait(use_py=True).sleep(2)

# todo: finish creating case
# stretch goal: check error messages
# stretch goal: add axe test