import os
    
def test_navigation(py):
    print('Login details:')
    print(os.environ.get('AMP_USERNAME'))
    print(os.environ.get('AMP_PASSWORD'))
    py.visit('https://accessibility-monitoring-platform-test.london.cloudapps.digital/')
    py.get('.govuk-heading-l').should().contain_text('Login')

# def test_tutorial(py):
#     py.visit('https://qap.dev')
#     py.get('a[href="/about"]').hover()
#     py.get('a[href="/leadership"][class^="Header-nav"]').click()
#     assert py.contains('Carlos Kidman')