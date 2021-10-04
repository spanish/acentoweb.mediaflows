# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s acentoweb.mediaflows -t test_mf_news.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src acentoweb.mediaflows.testing.ACENTOWEB_MEDIAFLOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/acentoweb/mediaflows/tests/robot/test_mf_news.robot
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

Scenario: As a site administrator I can add a MF News
  Given a logged-in site administrator
    and an add MF News form
   When I type 'My MF News' into the title field
    and I submit the form
   Then a MF News with the title 'My MF News' has been created

Scenario: As a site administrator I can view a MF News
  Given a logged-in site administrator
    and a MF News 'My MF News'
   When I go to the MF News view
   Then I can see the MF News title 'My MF News'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MF News form
  Go To  ${PLONE_URL}/++add++MF News

a MF News 'My MF News'
  Create content  type=MF News  id=my-mf_news  title=My MF News

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MF News view
  Go To  ${PLONE_URL}/my-mf_news
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MF News with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MF News title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
