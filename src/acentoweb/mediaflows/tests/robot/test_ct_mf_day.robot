# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s acentoweb.mediaflows -t test_mf_day.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src acentoweb.mediaflows.testing.ACENTOWEB_MEDIAFLOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/acentoweb/mediaflows/tests/robot/test_mf_day.robot
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

Scenario: As a site administrator I can add a MF Day
  Given a logged-in site administrator
    and an add MF Day form
   When I type 'My MF Day' into the title field
    and I submit the form
   Then a MF Day with the title 'My MF Day' has been created

Scenario: As a site administrator I can view a MF Day
  Given a logged-in site administrator
    and a MF Day 'My MF Day'
   When I go to the MF Day view
   Then I can see the MF Day title 'My MF Day'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MF Day form
  Go To  ${PLONE_URL}/++add++MF Day

a MF Day 'My MF Day'
  Create content  type=MF Day  id=my-mf_day  title=My MF Day

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MF Day view
  Go To  ${PLONE_URL}/my-mf_day
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MF Day with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MF Day title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
