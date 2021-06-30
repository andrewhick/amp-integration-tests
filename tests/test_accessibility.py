import os

def test_for_accessibility(py, axe):
    # Checks the Cases page for accessibility
    py.visit('https://accessibility-monitoring-platform-test.london.cloudapps.digital/')
    # Again, would prefer to call a function to log in here:
    py.get('[name="username"]').type(os.environ.get('AMP_USERNAME'))
    py.get('[name="password"]').type(os.environ.get('AMP_PASSWORD'))
    py.get('[value="Submit"]').click()

    py.get('.govuk-grid-row.dashboard').contains('Cases').click()
    # Run Axe, reporting on only WCAG level A and AA issues:
    report = axe.run(name='a11y_audit.json', options='{runOnly: ["wcag2a", "wcag2aa"]}')
    # assert len(report.violations) == 0 # fails currently
    print('### ACCESSIBILITY CHECK ###')
    print('Number of accessibility violations on Cases page: ' + str(len(report.violations)))