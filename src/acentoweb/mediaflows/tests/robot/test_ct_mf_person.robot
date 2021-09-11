# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s acentoweb.mediaflows -t test_mf_person.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src acentoweb.mediaflows.testing.ACENTOWEB_MEDIAFLOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/acentoweb/mediaflows/tests/robot/test_mf_person.robot
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

Scenario: As a site administrator I can add a MF Person
  Given a logged-in site administrator
    and an add MF Person form
   When I type 'My MF Person' into the title field
    and I submit the form
   Then a MF Person with the title 'My MF Person' has been created

Scenario: As a site administrator I can view a MF Person
  Given a logged-in site administrator
    and a MF Person 'My MF Person'
   When I go to the MF Person view
   Then I can see the MF Person title 'My MF Person'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MF Person form
  Go To  ${PLONE_URL}/++add++MF Person

a MF Person 'My MF Person'
  Create content  type=MF Person  id=my-mf_person  title=My MF Person

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MF Person view
  Go To  ${PLONE_URL}/my-mf_person
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MF Person with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MF Person title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
