import os
    
def test_navigation(py):
    # Navigates through each main page on the platform
    py.visit('https://accessibility-monitoring-platform-test.london.cloudapps.digital/')
    py.get('.govuk-heading-l').should().contain_text('Sign in')
    # Invalid password
    py.get('[name="username"]').type(os.environ.get('AMP_USERNAME'))
    py.get('[name="password"]').type('cheese')
    py.get('[value="Submit"]').click()
    py.get('.govuk-body').should().contain_text('Your username and password didn\'t match.')
    py.get('[name="username"]').clear()
    # Valid login
    # (ideally this would be a repeatable function)
    py.get('[name="username"]').type(os.environ.get('AMP_USERNAME'))
    py.get('[name="password"]').type(os.environ.get('AMP_PASSWORD'))
    py.get('[value="Submit"]').click()
    py.get('.govuk-heading-xl').should().contain_text('Dashboard')
    # Go to cases page from link in page body
    py.get('.govuk-grid-row.dashboard').contains('Cases').click()
    py.get('.govuk-heading-xl').should().contain_text('Cases and reports')
    py.get('a[href*="/cases/create"').should().be_visible()
    py.go('back')
    # Go to websites page from link in page body
    py.get('.govuk-grid-row.dashboard').contains('Websites').click()
    py.get('.govuk-heading-xl').should().contain_text('Query domain register')
    py.get('#id_service').should().be_visible()
    py.go('back')
    # Go to account details from header link
    py.get('a[href*="/user/account_details/"').click()
    py.get('.govuk-heading-l').should().contain_text('Your account details')
    py.get('[name="first_name"]').should().be_visible()
    py.go('back')
    # Sign out
    py.get('a[href*="/accounts/logout/"').click()
    py.get('.govuk-heading-l').should().contain_text('Sign in')