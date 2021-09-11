# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s acentoweb.mediaflows -t test_mf_program.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src acentoweb.mediaflows.testing.ACENTOWEB_MEDIAFLOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/acentoweb/mediaflows/tests/robot/test_mf_program.robot
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

Scenario: As a site administrator I can add a MF Program
  Given a logged-in site administrator
    and an add MF Program form
   When I type 'My MF Program' into the title field
    and I submit the form
   Then a MF Program with the title 'My MF Program' has been created

Scenario: As a site administrator I can view a MF Program
  Given a logged-in site administrator
    and a MF Program 'My MF Program'
   When I go to the MF Program view
   Then I can see the MF Program title 'My MF Program'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MF Program form
  Go To  ${PLONE_URL}/++add++MF Program

a MF Program 'My MF Program'
  Create content  type=MF Program  id=my-mf_program  title=My MF Program

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MF Program view
  Go To  ${PLONE_URL}/my-mf_program
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MF Program with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MF Program title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
