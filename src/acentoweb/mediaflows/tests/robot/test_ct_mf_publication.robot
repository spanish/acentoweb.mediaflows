# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s acentoweb.mediaflows -t test_mf_publication.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src acentoweb.mediaflows.testing.ACENTOWEB_MEDIAFLOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/acentoweb/mediaflows/tests/robot/test_mf_publication.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a MF Publication
  Given a logged-in site administrator
    and an add MF Publication form
   When I type 'My MF Publication' into the title field
    and I submit the form
   Then a MF Publication with the title 'My MF Publication' has been created

Scenario: As a site administrator I can view a MF Publication
  Given a logged-in site administrator
    and a MF Publication 'My MF Publication'
   When I go to the MF Publication view
   Then I can see the MF Publication title 'My MF Publication'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MF Publication form
  Go To  ${PLONE_URL}/++add++MF Publication

a MF Publication 'My MF Publication'
  Create content  type=MF Publication  id=my-mf_publication  title=My MF Publication

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MF Publication view
  Go To  ${PLONE_URL}/my-mf_publication
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MF Publication with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MF Publication title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
