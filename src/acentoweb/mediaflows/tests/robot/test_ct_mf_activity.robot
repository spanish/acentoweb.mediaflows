# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s acentoweb.mediaflows -t test_mf_activity.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src acentoweb.mediaflows.testing.ACENTOWEB_MEDIAFLOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/acentoweb/mediaflows/tests/robot/test_mf_activity.robot
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

Scenario: As a site administrator I can add a MF Activity
  Given a logged-in site administrator
    and an add MF Activity form
   When I type 'My MF Activity' into the title field
    and I submit the form
   Then a MF Activity with the title 'My MF Activity' has been created

Scenario: As a site administrator I can view a MF Activity
  Given a logged-in site administrator
    and a MF Activity 'My MF Activity'
   When I go to the MF Activity view
   Then I can see the MF Activity title 'My MF Activity'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MF Activity form
  Go To  ${PLONE_URL}/++add++MF Activity

a MF Activity 'My MF Activity'
  Create content  type=MF Activity  id=my-mf_activity  title=My MF Activity

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MF Activity view
  Go To  ${PLONE_URL}/my-mf_activity
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MF Activity with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MF Activity title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
