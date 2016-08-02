# Revamping Incident Response

## The Problem 

Symptom: The same people are "on call" all the time
Symptom: When system X fails, you always go to person Y
Symptom: When a problem occurs, the whole team gets waylaid
Symptom: In your incident retro you say "communication should have been better"

We may or may not have been having all of these symptoms (and more).
I can safely say, with a touch of pride, that we've resolved all of them.
Our uptime has increased markedly, and we've decreased engineer burnout
(as measured by employees WFH after a pager event).

Real Time Analytics Uptime - Four Week Rolling Average
Week 1: 99.34%
Week 2: 99.67%
Week 3: 99.76%
Week 4: 99.78%
Week 5: 99.95%
Week 6: 99.94%

## The Principals

*Organization*: 
_There can be only one _
    - place for tracking incidents
    - pagerduty schedule
    - workflow for incidents
This needs to be the same regardless of what system is impacted, and what team is impacted.

*Automation*: Dealing with a pagerduty can be stressful and any rote work should be automated. 

*Empathy*: This is inadvertently the most brilliant part of the system. When
discussing the rollout, an engineer said to me, "I don't like it, I don't want my mistakes to 
wake up someone else at 4am." This exposes something really interesting - people don't mind
inconveniencing themselves, especially if it's something small and infrequent. But the second
they realize it could be inconveniencing someone else, it becomes their top priority.

*Communication is equal priority as Fixing*: When an incident occurs, two people are paged.
One person is the "communicator" one person is the "fixer." This protects the engineer from being distracted
by others asking for status updates, and ratchets up the importance of communication.


## The Solution
### Two heads instead of one
Two people are on pager duty instead of one.
Their roles are clearly defined and separate.

*Incident Manager*
 * Send out emails and communicate in chat rooms
 * Set User-facing error messages when applicable
 * Label ticket, and update frequently
 * Handle communications with DevOps
 * Document process and update run-books

*Incident Engineer*
 * Research and Identify problem
 * Try applicable run-books
 * Problem solve

### One Schedule
Flatten out the pager duty structure entirely. Instead of each team tracking pages for their individual services,
there is one schedule which listens for pages from any service. The escalation strategy works like so

Level 1: Incident Manager, Incident Engineer
Level 2: Everyone except VP and CTO
Level 3: VP and CTO

_Note: The drastic rise in escalation sucks, but as a result we've never had an event escalate to level 2._


### Iterate and Improve
And then you take all this and make it "agile." Every week, we retro and discuss how it went.
Every page gets tracked in a spreadsheet where we can look for trends week over week.
Then we discuss the week. How is morale? What went wrong, and did we document or automate the resolution?
What could be better?

We've already improved the process based on these retros when we realized there was 
some confusion related to the urgency of the alerts. Which ones need to be worried about immediately,
and which can wait till we're back at the office? The retro helped us identify the ambiguity and address it by the second week.

So far, the trends have been positive and I'm certain we will continue to refine and improve the process.



