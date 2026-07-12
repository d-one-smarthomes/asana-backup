# General (IN PROGRESS -- PARTIAL BACKUP, DO NOT TREAT AS COMPLETE)
**GID:** 905674768180011
**Last updated:** 2026-07-12
**Project total tasks (per Asana):** 3680 (3659 completed, 21 incomplete)
**Tasks captured in this partial backup:** 2800 (2781 completed)

> NOTE FOR FUTURE BACKUP RUNS: This project is too large to fully back up in a
> single automated run (3680 tasks vs ~100/API call). This file is intentionally
> NOT named General.md so the backup job does not mistake it for a completed
> backup and skip General forever.
>
> STATE AS OF 2026-07-12 (latest run): 1800/3680 tasks captured (pages 1-18 of
> ~37, 100 tasks/page). Raw fetched pages (name/completed/assignee/due_on/notes,
> 100 tasks each, in Asana's default stable task order) are cached in
> _raw_general/page15.json..page18.json in this repo -- pages 1-14 were NOT
> re-cached this run (pages 1-14 were only walked with opt_fields=name to reach
> the resume offset; their content matches what's already written to this file
> for tasks 1-1400).
>
> IMPORTANT: the Asana pagination offset token expires after ~15 minutes, so a
> saved next_offset from a previous session (even one recorded in a cached
> page*.json file) will almost certainly be EXPIRED by the time a new session
> starts. Do NOT try to resume directly from _raw_general/page18.json's
> next_offset if it's been more than a few minutes since it was fetched --
> it will fail. Instead: re-walk pages 1-18 fresh with lightweight
> opt_fields="name" only (fast, ~18 calls, discard the data) to obtain a
> valid pagination cursor pointing at task 1801, confirming you've reached the
> right spot by checking the border_rank/gid in the new offset matches the
> stale one cached in page18.json (they should be identical JWT payloads other
> than iat/exp). THEN switch to full opt_fields="name,completed,
> assignee.name,due_on,notes" for all subsequent pages (19 onward).
>
> TO RESUME (once you have a fresh valid offset at task 1801): for each new
> page: save the raw JSON to _raw_general/page19.json (etc, matching the page
> number), convert to the same markdown format as below and append to this
> file (NOT General.md), update the two "Tasks captured" counts in the
> header/section title above, and commit+push after every page or two.
> IMPORTANT GIT WORKAROUND: this repo
> lives on a FUSE-mounted Downloads folder that does not support deleting files
> -- git's own lock files (.git/HEAD.lock, .git/index.lock) sometimes survive a
> completed git command and block the next one. Before every `git commit` or
> `git push`, run `for f in .git/index.lock .git/HEAD.lock; do [ -e "$f" ] &&
> mv "$f" "$f.bak$(date +%s%N)"; done` first (mv works even though rm/rename
> unlink of the ORIGINAL name is blocked -- git still creates a fresh lock
> file each time and moving the stale one out of the way is enough). The
> "warning: unable to unlink tmp_obj..." messages during commit are harmless.
> Continue until all ~3680 tasks are captured, then rename this file to
> General.md and remove the _raw_general/ cache directory (or leave it; it's
> harmless) and update INDEX.md.

## Tasks captured so far (2800 of 3680 total, 2781 completed)

### ⬜ Lutron homeworks training
- **Assignee:** Mekyle Cerff
- **Due:** 2026-08-18
- **Notes:** Please remember we have the following dates scheduled for HOMEWORKS training - 

August - 18th to the 21st
October - 13th to the 16th
December - 5th to the 8th

### ⬜ Leave request 16th July
- **Assignee:** Caren Bailey
- **Due:** 2026-07-15

### ✅ Stock Booked out
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Booked out Stock today

Oakvale x1 96313

Clouds Estate x2 UPoe 48-60 W cable & U7-Pro0 Outdoor

Desvaux x3 
x2 cable switch
x1 modem
and stafford took the USw 24 max pro already

### ✅ Let Workshop17 know that I am now an EO member which means we get 10% discount on our memberships.
- **Assignee:** Caren Bailey
- **Due:** 2026-07-09

### ✅ Invite Berna to Tech meetings
- **Assignee:** Stafford
- **Due:** 2026-07-02

### ✅ PAIA Legislation to confirm and sign please .
- **Assignee:** Amanda
- **Due:** 2026-06-29
- **Notes:** Hi Darren & Amanda

As per the email from Andrea this has been registered .

I will print the certificate as per the other email sent to us.

Please review and initial the necessary documents and send them back to either Andrea or me once you are finished.

Thank you all documents are attached .

### ✅ Off sick Justin
- **Assignee:** Caren Bailey
- **Due:** 2026-06-22
- **Notes:** Hi Caren 

Please note Justin is off sick today

### ⬜ 35A2 - Quote New Swivel Bracket
- **Assignee:** Caleb Thetard
- **Due:** 2026-06-19
- **Notes:** 35A2 Constantia Road - TV and Sonos Arc is to heavy for the Current bracket , client can’t move the bracket to different positions for viewing

### ⬜ Caleb Leave Dates to be Approved
- **Assignee:** Caren Bailey
- **Due:** 2026-07-15
- **Notes:** Hi D-One

I would like to put in for 8 Days of consecutive leave for the 15th of July to the 24th of July. 

Please advise if this is okay?

### ✅ Snapshot Follow Ups
- **Assignee:** Caren Bailey
- **Due:** 2026-06-11
- **Notes:** Hi Caleb

I trust you well.
Payment in and Snapshot Updated.
WE Quote Labour still outstanding, please check these out.

14 Harrigan Quote 0353 Facial Access. Labour 
43 JNA - Quote 303 & 340, Must we invoice?
52 Kuessner - Quote 355, Must we invoice?
17 Desvaux - Quote 326, 365 & 366: labour to be invoiced?
81 Hassan - Quote 357 invoiced, not paid.

Please let me know.

### ✅ Escalate savant SA support not helpful if Mohammed not around
- **Assignee:** Darren Swanepoel
- **Due:** 2026-06-01

### ✅ Continue Claude AI setup experimentation – validate different configuration with transcripts
- **Assignee:** Mekyle Cerff
- **Due:** 2026-05-27
- **Notes:** Darren has been experimenting with a different Claude configuration. Mekyle to continue testing the new setup. Validate behaviour using captured meeting transcripts and screenshots. Currently Claude does not have a native note-taker skill.

### ✅ Add dedicated note-taker role to Claude AI setup
- **Assignee:** Mekyle Cerff
- **Due:** 2026-05-27
- **Notes:** Without a note-taker role, Claude can only process transcripts and screenshots reactively after the fact. Adding a dedicated note-taker role will allow Claude to actively populate action items and produce a fuller, real-time meeting summary. Open item – no timeline yet.

### ✅ Develop snagging and project sign-off process – close the final 20% gap
- **Assignee:** Darren Swanepoel
- **Due:** 2026-05-29
- **Notes:** Team consistently gets to 80-90% on projects then gets pulled onto new ones. Loose ends drag: speaker changes, intercom items, volume caps, etc. Darren working on a formal sign-off system. Key idea: use a formal sign-off document per system category (CCTV signed off, network signed off, etc.) so projects close cleanly. Benji/Caleb/Darren to do dedicated snagging sweep at each project before closing.

### ✅ Contract Justin B Job Description
- **Assignee:** Caren Bailey
- **Due:** 2026-05-26
- **Notes:** Hi Stafford

Please could you draft a contract Annexures for the role he has taken on Junior Technision as per your WhatsApp content.

### ✅ General stock
- **Assignee:** Caren Bailey
- **Due:** 2026-05-21

### ✅ Re-allocate 5 leave days for Mekyle - he only took 5
- **Assignee:** Caren Bailey
- **Due:** 2026-05-21

### ⬜ Daily Productivity & Admin Guideline - Justin Bailey
- **Assignee:** Justin Bailey
- **Due:** None
- **Notes:** Hi Justin,

This guideline has been put together to help you build better daily habits - both on-site and administratively. Following this consistently will make a real difference to your output, your growth, and how the team can rely on you.

---
MORNING ROUTINE (Start of Day)
- Check Asana first thing, before picking up any tools. Review all tasks assigned to you.
- If a task has no due date, set one yourself. Don't leave tasks floating.
- If you're unsure about a task or don't have what you n

### ✅ Leave Request
- **Assignee:** Amanda
- **Due:** 2026-06-04
- **Notes:** Hi Amanda & Darren

I hereby request a leave Day for 5th June 2026. I will make sure most of my stuff is up to date. 

Going away for the weekend.

Thank you, and let me know.
Caren

### ✅ Leave request
- **Assignee:** Caren Bailey
- **Due:** 2026-06-08
- **Notes:** Plese book me off for the following days 

5th June, 8th June and 15th June

### ✅ Purchase Justin a work pants
- **Assignee:** Tristan Capes
- **Due:** 2026-05-18

### ✅ Renew Caddy and Polo license
- **Assignee:** Caren Bailey
- **Due:** 2026-05-18

### ✅ Arrange immune booster vitamins for techs
- **Assignee:** Caren Bailey
- **Due:** 2026-05-11

### ✅ Check details and resolve
- **Assignee:** Caren Bailey
- **Due:** 2026-05-05
- **Notes:** REMINDER: A court summons may be issued for traffic fine G/80/259579/653 R200. Ignore if finalised. To pay visit www.paymyfines.co.za

### ✅ Odoo Categories
- **Assignee:** Amanda
- **Due:** 2026-05-12
- **Notes:** ALARM
    CCTV
    Intercom & Access Control
    Network
    Audio
    Home Theatre 
    TV
    Lighting Control
    System Integration
    Window Treatment
    Labour - Design
    Labour - Service
    Labour - Cabling
    Labour - Installation
    Labour  - Programming
    Labour - Project Management
        DESIGN
        SERVICE
        CABLING
        INSTALLATION
        PROGRAMMING
        PROJECT MANAGEMENT

Categories
Alarm
    Sensors
    Panels
    Alarm accessories

CCTV
    Cameras
 

### ✅ Consider Claude Team Plan (everyone could use the same subscription)
- **Assignee:** Darren Swanepoel
- **Due:** 2026-05-05
- **Notes:** https://app.asana.com/app/asana/-/get_asset?asset_id=1214468622360546

### ✅ Collect Benji's t-shirts from heyday
- **Assignee:** Tristan Capes
- **Due:** 2026-04-29

### ✅ Overtime
- **Assignee:** Amanda
- **Due:** 2026-05-20

### ✅ Leave taken
- **Assignee:** Caren Bailey
- **Due:** 2026-04-21
- **Notes:** Hi Caren 

Please allocate the 10th, 13th and 14th April to family responsibility leave. 

15th,16th and 17th allocate from annual leave.

Thank you

### ✅ Check fines
- **Assignee:** Caren Bailey
- **Due:** 2026-04-21
- **Notes:** REMINDER: A court summons may be issued for traffic fine ST/81/310585/760 R600. Ignore if finalised. To pay visit http://www.paymyfines.co.za

REMINDER: A court summons may be issued for traffic fine ST/81/310620/760 R200. Ignore if finalised. To pay visit http://www.paymyfines.co.za

### ✅ Send Bryan (Homemation) the value we spent at Scoop + Miro for the last 3 years.
- **Assignee:** Caren Bailey
- **Due:** 2026-04-21

### ✅ Tech Meeting
- **Assignee:** Stafford
- **Due:** 2026-04-20
- **Notes:** Tech meeting agenda — project-by-project status and action items.

### ✅ Sort with Tristan
- **Assignee:** Caren Bailey
- **Due:** 2026-05-04

### ✅ Cancel tracker on Audi
- **Assignee:** Caren Bailey
- **Due:** 2026-04-28

### ✅ Increase Fibre 1 May 26 -33 Belmont
- **Assignee:** Caren Bailey
- **Due:** 2026-04-16
- **Notes:** Hi Caren

Please increase the Invoice on 15th April via Xero.

Email sent out to client today.
R1551.82 to R1621.82 R70.00 revenue.

### ✅ Santam Clean Up Insurance - Removing and Adding New devised
- **Assignee:** Caren Bailey
- **Due:** 2026-05-22
- **Notes:** Hi Amanda & Darren

Clean up of removing and adding new devices on the Santam Schedule.
Please see the attached schedule and Excel document. I have a few ???

Thank you

### ✅ Justin off today
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Check account details with Mauricio
- **Assignee:** Darren Swanepoel
- **Due:** 2026-03-30

### ✅ Cowork for team
- **Assignee:** Darren Swanepoel
- **Due:** 2026-03-26

### ✅ Help sort stores out
- **Assignee:** Justin Bailey
- **Due:** 2026-03-23

### ✅ 🟠 PHASE 3: Multi-Room Audio Fundamentals
- **Assignee:** Justin Bailey
- **Due:** 2026-03-23
- **Notes:** What you must understand _  find and add your own videos to the below

🎥 Mandatory Videos 
    Whole-Home Audio Systems Explained (Beginner Level)
    👉 https://www.youtube.com/watch?v=Yh7h1bLZx6Q
    How Multi-Room Audio Works (Zones, Sources, Amps)
    👉 https://www.youtube.com/watch?v=Z6Gz6S3G4zE
    AV Rack Basics – Clean & Professional Installs
    👉 https://www.youtube.com/watch?v=V8n0tK6zZ6E

### ✅ Follow Up Task for Email to Clients Nexus/Izwe
- **Assignee:** Caren Bailey
- **Due:** 2026-03-24

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2026-03-16

### ✅ Cancel Google Workspace AI on personal
- **Assignee:** Darren Swanepoel
- **Due:** 2026-03-25

### ✅ Meklye off sick
- **Assignee:** Caren Bailey
- **Due:** 2026-03-11
- **Notes:** Mekyle to provide medical certificates

### ✅ Trinov and Barco Training
- **Assignee:** Tristan Capes
- **Due:** 2026-03-05

### ✅ Tasks incomplete from last week for tech meeting review
- **Assignee:** Stafford
- **Due:** 2026-03-09

### ✅ Schedule medicals with the previous company I think in parow please
- **Assignee:** Caren Bailey
- **Due:** 2026-03-16
- **Notes:** 64 Industria Ring Rd, Ravensmead, Cape Town, 7504

Medsafe

### ✅ Add Mekyle to Homemation training Thursday
- **Assignee:** Caleb Thetard
- **Due:** 2026-03-03

### ✅ Leave request 23rd March 2026
- **Assignee:** Caren Bailey
- **Due:** 2026-03-23

### ✅ Internet Increase in April -Vumatel -Immerman
- **Assignee:** Caren Bailey
- **Due:** 2026-03-09
- **Notes:** Internet Increase 

Your Vumatel Fibre package price change 1 April 2026
24 Glencoe Road
200|200 Mbps
R1137.00 PM
until 31 Mar 2026
R1167.00 PM
from 01 Apr 2026

24 Glencoe Rd Oranjezicht .

### ✅ Weekly Check up We Quote Approvals
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Hi Caleb

This will just be me assisting with any Invoices, Approved Quotes and PO for our Revenue.

### ✅ Caleb Leave Request Friday 6 March
- **Assignee:** Caren Bailey
- **Due:** 2026-03-06

### ✅ Check details REMINDER: A court summons may be issued for traffic fine ST/81/191664/760 R1200. Ignore if finalised. To pay visit www.paymyfines.co.za
- **Assignee:** Caren Bailey
- **Due:** 2026-02-24

### ✅ Mekyle’s Mac to digicape
- **Assignee:** Stafford
- **Due:** 2026-02-24

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2026-02-16

### ✅ Crestron forms
- **Assignee:** Darren Swanepoel
- **Due:** 2026-02-16

### ✅ Add new Ridge project Unathi/Sutherland to asana
- **Assignee:** Caleb Thetard
- **Due:** 2026-02-16

### ✅ Renew Fingerprint for VDV Access
- **Assignee:** Tristan Capes
- **Due:** 2026-02-11

### ✅ Check big store for large site boards
- **Assignee:** Tristan Capes
- **Due:** 2026-02-24

### ✅ Change Flat wheel on Caddy
- **Assignee:** Tristan Capes
- **Due:** 2026-02-11

### ✅ Tracker Mileage 2026
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Sick leave
- **Assignee:** Caren Bailey
- **Due:** 2026-02-10

### ✅ Review our rates for the new year
- **Assignee:** Caleb Thetard
- **Due:** 2026-02-16

### ✅ Drop Ap's and Subwoofer at Office for Mekyle
- **Assignee:** Tristan Capes
- **Due:** 2026-02-05

### ✅ Collection at Miro
- **Assignee:** Tristan Capes
- **Due:** 2026-02-05

### ✅ Drop off t-shirts DVDV
- **Assignee:** Tristan Capes
- **Due:** 2026-02-05

### ✅ Age Analysis Feb 26
- **Assignee:** Caren Bailey
- **Due:** 2026-02-04
- **Notes:** Hi Amanda and Caleb

Snapshot check in on Fibre Invoices and outstanding Revenue.

As per the attached spreadsheet, these were all actioned and emailed to the clients.
SLA, Outstanding Invoices ect....

Thanks

### ✅ Check out oodo accounts package
- **Assignee:** Amanda
- **Due:** 2026-02-03
- **Notes:** Not sure of spelling

### ✅ Pick up Justin & Mekyle
- **Assignee:** Tristan Capes
- **Due:** 2026-02-02

### ✅ TRAINING 🟢 PHASE 1: Networking Fundamentals (Week 1–2)
- **Assignee:** Justin Bailey
- **Due:** 2026-03-03
- **Notes:** Purpose: Understand how networks work and why everything depends on them.

Complete all subtask (videos). 

Monday will be test/practical.

### ✅ Collect hdmi audio extractor from Linkqage
- **Assignee:** Tristan Capes
- **Due:** 2026-01-29

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2026-01-29

### ✅ Collect point to point from Scoop
- **Assignee:** Tristan Capes
- **Due:** 2026-01-29

### ✅ TRAINING🟡 PHASE 2: IP CCTV Systems (Week 2–3)
- **Assignee:** Justin Bailey
- **Due:** 2026-03-19
- **Notes:** What YOU must understand 
    What an IP camera is
    Difference between IP vs Analogue
    How POE powers cameras
    What an NVR does
    Camera → Switch → NVR → Network → App

Find and add your own videos for every subtask below - FRIDAY IS DUE DATE

### ✅ Collect router from office
- **Assignee:** Tristan Capes
- **Due:** 2026-01-29

### ✅ Clear stock from Caddy and load onto Flatbed
- **Assignee:** Tristan Capes
- **Due:** 2026-01-27

### ✅ Office/Get Mekyle and Justin
- **Assignee:** Tristan Capes
- **Due:** 2026-01-27

### ✅ Collect Caddy
- **Assignee:** Tristan Capes
- **Due:** 2026-01-27

### ✅ LInkqage/Regal/AcDc
- **Assignee:** Tristan Capes
- **Due:** 2026-01-26

### ✅ Fast car Meeting
- **Assignee:** Tristan Capes
- **Due:** 2026-01-26

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2026-01-26

### ✅ Confirm Caddy and Polo insurance, whos its with?
- **Assignee:** Caren Bailey
- **Due:** 2026-01-26

### ✅ Take small Samsung Galaxy Tablet for Stafford
- **Assignee:** Caren Bailey
- **Due:** 2026-01-21

### ✅ Collect laptop in black backpack in garage
- **Assignee:** Stafford
- **Due:** 2026-01-21

### ✅ Order boots for the guys
- **Assignee:** Caren Bailey
- **Due:** 2026-01-21

### ⬜ Blinq for business cards
- **Assignee:** Unassigned
- **Due:** None

### ✅ Register justin for VDV access
- **Assignee:** Caren Bailey
- **Due:** 2026-01-22

### ✅ Setup Uber for business account
- **Assignee:** Caren Bailey
- **Due:** 2026-01-14
- **Notes:** For Mekyle and deliveries to all be managed from a central place that you and Mekyle can manage directly.

### ✅ Ask your kids to help us find Junior techs. Dudes that love tech that just finished school/college
- **Assignee:** Stafford
- **Due:** 2026-01-12

### ✅ Update D-One address on Duxbury account info.
- **Assignee:** Caren Bailey
- **Due:** 2026-01-12

### ✅ Credit Card Recon Updated
- **Assignee:** Caren Bailey
- **Due:** 2026-01-08
- **Notes:** Hi Amanda 

All Credit Cards recon done and slips held.

### ✅ Overtime December Mekyle
- **Assignee:** Amanda
- **Due:** 2025-12-24
- **Notes:** 8.30Hours for December - thank you

### ✅ Review overdue tasks
- **Assignee:** Darren Swanepoel
- **Due:** 2025-12-17

### ✅ Return to planet world. This is the wiring harness
- **Assignee:** Caren Bailey
- **Due:** 2026-01-14

### ✅ Add: ISE System integrator of the year 2025
- **Assignee:** Amanda
- **Due:** 2025-12-10
- **Notes:** Add this to all of our email signatures

### ✅ Overtime
- **Assignee:** Amanda
- **Due:** 2025-11-24
- **Notes:** 25th September 2hrs Hely hutch
29th September 2hrs Hely hutch
3rd November 1hr 30mins svelte
6th November 4hrs Brandt
10th Nov 2hrs Svelte
12th Nov 3hrs Svelte
14th Nov 4hrs Svelte
18th November 5hrs Svelte
19th November 4hrs Svelte

### ✅ Mekyle Overtime
- **Assignee:** Amanda
- **Due:** 2025-11-24
- **Notes:** Svelte _ 31 Hrs
Brandt_ 5 Hrs
Hely Hutch_ 4Hrs

### ✅ High level goals for 2025
- **Assignee:** Darren Swanepoel
- **Due:** 2025-11-24
- **Notes:** Orange items

### ✅ Cancel subscriptions on apple account
- **Assignee:** Darren Swanepoel
- **Due:** 2025-11-19

### ✅ Share your Google calendar. We are integrating WeQuote time tracking
- **Assignee:** Mekyle Cerff
- **Due:** 2025-11-17
- **Notes:** Share calendar with:
Darren
Accounts@d-one
Amanda
Caleb
Tristan

### ✅ Please replace battery for iphone im using - doesn’t even last me 30mins 😪. Pakistani is fine
- **Assignee:** Stafford
- **Due:** 2025-11-17

### ✅ TakeAlot Invoice R1899.00
- **Assignee:** Amanda
- **Due:** 2025-11-10
- **Notes:** Hi Darren


Invoice please 
TakealotTAKEALOT ONLINE ZZ 194371583General MerchandiseMore details
Spent1,899.00

### ✅ WeQuote Planetworld integration
- **Assignee:** Caleb Thetard
- **Due:** 2026-03-20
- **Notes:** Connect WeQuote and Planetworld, to get live pricing. Then we try homemation too.
A Live spreadsheet can work. If need be AI could even translate the data.

### ✅ Send Kyle from Planetworld the invoice from Digicape for Caleb’s MacBook
- **Assignee:** Caren Bailey
- **Due:** 2025-11-04

### ✅ Grab notebook and pen - make sure Mekyle and Tristan have for planning, designs, notes etc.
- **Assignee:** Stafford
- **Due:** 2025-10-31

### ✅ Create UniFi for Caleb
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-30

### ✅ Sick Leave Tristan Capes
- **Assignee:** Caren Bailey
- **Due:** 2025-10-27
- **Notes:** Hi Amanda

1 Sick date captured for Tristan, 23 October 25.

### ✅ Week plan VRY+HAR?
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-27

### ✅ Update on WeQuite integration
- **Assignee:** Amanda
- **Due:** 2025-10-23

### ✅ Confirm tracker mileage
- **Assignee:** Caren Bailey
- **Due:** 2025-10-24
- **Notes:** Just confirming if you're still adjusting tracker mileage for business and personal travel?

### ✅ Train team on time tracking with Snagg app
- **Assignee:** Amanda
- **Due:** 2025-10-29

### ✅ Do Reseller Application
- **Assignee:** Caren Bailey
- **Due:** 2025-10-15

### ✅ Confirm if we still have any of this demo stock from Planetworld
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** And let Kyle know +27 66 397 3288

9155017 - FLUSH MOUNT BOX FOR SINGLE HEIGHT DOOR STATION
eZi-PSU-12V-5A - P5 power supply 
FNIP-6x2AD - 6 Channel Dimmer 
(I thought we returned these units)


PAV-AIO1C-00 - Savant Single in out module 
(This was supplied because the Sipa wouldn’t power the Patio series speakers. And we couldn’t invoice afterwards - the system didn’t do its job properly. Even Sonance came to site when they were here.)

SON-HARNESS - Complete Wiring Harness for Demo of Garden a

### ✅ Check account and see if there is anything outstanding for BNI. My last session was end August 2025
- **Assignee:** Caren Bailey
- **Due:** 2025-10-09
- **Notes:** andre@bni.com

### ✅ Access for VDV
- **Assignee:** Caren Bailey
- **Due:** 2025-10-06
- **Notes:** Dear CM THETARD your access to Val de Vie Estate will expire in 3 days 11/09/2025, Please report to the Security Registration office to extend your access period.

### ✅ T-Shirts
- **Assignee:** Amanda
- **Due:** 2025-10-08
- **Notes:** Team urgently need t-shirts please. 

Current ones are broken and branding coming off. 

Subtasks created for each to give sizes I’m recommending 5 each please

### ✅ Team to Catchup Harvest until end September
- **Assignee:** Stafford
- **Due:** 2025-10-09
- **Notes:** We will move over to WeQuote from 1 October.

### ✅ Setup discovery meeting with WeQuote
- **Assignee:** Amanda
- **Due:** 2025-09-29

### ✅ Harvest time tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-07

### ✅ Harvest time tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-08

### ✅ Harvest time tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-09

### ✅ Harvest time tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-10

### ✅ Harvest time tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-13

### ✅ Harvest time tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-14

### ✅ Harvest time tracking
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Harvest time tracking
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Create hik-partner pro admin user / change email address to tech@d-one.co.za
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-01

### ✅ Resolve so I don't go to jail
- **Assignee:** Caren Bailey
- **Due:** 2025-10-02
- **Notes:** REMINDER: A court summons may be issued for traffic fine ST/80/3257662/760 R400. Ignore if finalized. To pay visit www.paymyfines.co.za

### ✅ Email all clients that have split ISP’s
- **Assignee:** Darren Swanepoel
- **Due:** 2025-09-18

### ✅ Come swop laptops with Darren when done
- **Assignee:** Tristan Capes
- **Due:** 2025-09-12

### ✅ Drop off 4 MacBooks and collect the 13’ at DVDV
- **Assignee:** Stafford
- **Due:** 2025-09-15
- **Notes:** 2 old ones
Tristan’s
Stafford’s 

I’ll figure out what goes where. Then redistribute.

### ✅ Dashboard for Monday end of year
- **Assignee:** Stafford
- **Due:** 2025-09-09

### ✅ Caddy Brakes
- **Assignee:** Caren Bailey
- **Due:** 2025-09-02

### ✅ Recurring SLA task
- **Assignee:** Mekyle Cerff
- **Due:** 2025-09-01

### ✅ VDV fine
- **Assignee:** Amanda
- **Due:** 2025-09-01
- **Notes:** Hi Amanda 

Please make suitable arrangements with Tristan regarding the fine of R4000 🥺

### ✅ Delete Edwin from asana
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-29

### ✅ Innovation Group for Quote for Caddy sales for WBC
- **Assignee:** Caren Bailey
- **Due:** 2025-09-12

### ✅ Caddy service plan
- **Assignee:** Caren Bailey
- **Due:** 2025-08-28
- **Notes:** Please confirm what’s covered on the caddy service plan motor warranty etc

### ✅ Pay balance of invoice to Creatory.
- **Assignee:** Caren Bailey
- **Due:** 2025-08-27
- **Notes:** I think we have only paid the deposit so far. Just confirm with Marcelle design@creatory.co.za

### ✅ Planetworld orders
- **Assignee:** Caleb Thetard
- **Due:** 2025-09-12
- **Notes:** Planetworld is keen to get their invoicing out. And will help us on the Barcelona leaderboard and earning interest, by giving us 60 days to pay. 

So we can order all of the PW stock for projects that will happen this year. And sit on the rest. 

So if there’s anything we can still order for 2025 projects. We can proceed.

### ✅ Format your macbook, and deliver it to Digicape for credit
- **Assignee:** Tristan Capes
- **Due:** 2025-08-25

### ✅ Format your macbook, and deliver it to Digicape for credit
- **Assignee:** Mekyle Cerff
- **Due:** 2025-08-25

### ✅ Macbooks to Digicape - chat to the, about what to keep for you, and what to trade.
- **Assignee:** Stafford
- **Due:** 2025-08-26

### ✅ Leave request 10 October 2025
- **Assignee:** Caren Bailey
- **Due:** 2025-10-10

### ✅ Thanks Imti
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-25

### ✅ Call Jason Stevens back
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-25

### ✅ Send Darius new Mac details
- **Assignee:** Caleb Thetard
- **Due:** 2025-08-22

### ✅ Send kids iPad details to Darius for DISCOVERY home insurance
- **Assignee:** Amanda
- **Due:** 2025-08-18

### ✅ Send your iPad details to Darius serial, model and value
- **Assignee:** Amanda
- **Due:** 2025-08-18

### ✅ Send Darius the make, model and serial number of your Apple Watch
- **Assignee:** Amanda
- **Due:** 2025-08-18

### ✅ Send Apple Watch serial to Darius
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-20

### ⬜ Test alarm system at warehouse
- **Assignee:** Unassigned
- **Due:** None

### ✅ Drakenstein Bill
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-20
- **Notes:** Please create a rule for me to get the Drakenstein bills

### ✅ MacBooks to Digicape
- **Assignee:** Stafford
- **Due:** 2025-08-18
- **Notes:** M2 R17999
M1 R11999

### ✅ Check this out
- **Assignee:** Mekyle Cerff
- **Due:** None
- **Notes:** https://www.tiktok.com/@crosstalksolutions/video/7537363216171584798

### ✅ Add payment details to quote template if they are not there already
- **Assignee:** Caleb Thetard
- **Due:** 2025-09-02

### ✅ How do we streamline Netclick?
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-21

### ✅ Print one of these for We Buy Cars from D-One
- **Assignee:** Amanda
- **Due:** 2025-08-08

### ✅ Send Mauricio videos of savant with camera feeds
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-08

### ✅ Wickus re email fraud
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-06

### ✅ Contact fraud lines FNB and Absa to report this fraud
- **Assignee:** Caren Bailey
- **Due:** 2025-08-06

### ✅ Kobus (Base) alarm quote see what we’ve got on general
- **Assignee:** Caleb Thetard
- **Due:** 2025-08-11
- **Notes:** 3X180 degree beams 
Panel 50/50+battery+keypad+transformer 
Centurion receiver 
1X blue led

### ✅ ChatGPT asana
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-15
- **Notes:** https://www.adenin.com/apps/asana/chatgpt/

### ✅ Cancel Cartrack for the old Caddy
- **Assignee:** Caren Bailey
- **Due:** 2025-08-18

### ✅ Integrate ChatGPT agent to Google
- **Assignee:** Darren Swanepoel
- **Due:** 2025-09-03

### ✅ Recon & Payments In & Out
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Payments in and out.
Fibre & Service Call
Invoices, Income and Suppliers.

### ✅ New Projects in asana issue for Mekyle.. (comment only permission)
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-16
- **Notes:** https://app.asana.com/app/asana/-/get_asset?asset_id=1210931892285554

### ✅ Have caddy badge, window and door handle fixed for private resale.
- **Assignee:** Tristan Capes
- **Due:** 2025-07-31
- **Notes:** We should get more than what WeBuyCars is offering if we fix these things.

### ✅ Meet WBC at the Berg river gate at 16:00 with the old caddy
- **Assignee:** Tristan Capes
- **Due:** 2025-07-29

### ✅ swop out laptops and attempt again
- **Assignee:** Tristan Capes
- **Due:** 2025-07-29

### ✅ Please order from takealot (ask stafford if any questions)
- **Assignee:** Caren Bailey
- **Due:** 2025-07-31
- **Notes:** Sizes

Mekyle : 30
Stafford : 36
Tristan : 34

### ✅ New caddy battery
- **Assignee:** Tristan Capes
- **Due:** 2025-07-28

### ⬜ add sfp's + flyleads to rack equipmwnt sales bundles
- **Assignee:** Caleb Thetard
- **Due:** None

### ✅ snag website, look for glitches
- **Assignee:** Caleb Thetard
- **Due:** 2025-08-15

### ✅ Double check how many of the attached we have in general them sell it on gum tree etc get pricing from spectrum
- **Assignee:** Caren Bailey
- **Due:** 2025-07-25

### ✅ Let me know if you see an Apple USBc cable on the jacket somewhere. I lost it in my car where the jacket was
- **Assignee:** Caleb Thetard
- **Due:** 2025-07-24

### ✅ SNAPSHOT
- **Assignee:** Caleb Thetard
- **Due:** 2025-07-25
- **Notes:** Hey Caleb

On the snapshot, we have TO BE Invoiced .

Please double check your formulas, I picked up an error - Gnobbe Base doesn't seem right.

Once your confident with the info, please can you estimate what is still to be invoiced for ONLY this year?

### ✅ Access extension application mail these people please notes on pic
- **Assignee:** Caren Bailey
- **Due:** 2025-07-18

### ✅ Change Farzeen passwords
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Arrange with Amanda’s guy to drop old caddy at Grahams repairs Monday by 08:30-09:00
- **Assignee:** Caren Bailey
- **Due:** 2025-07-21
- **Notes:** The old caddy is parked by Darren on the field

### ✅ Sick Leave For Mekyle Cerff
- **Assignee:** Caren Bailey
- **Due:** 2025-07-18
- **Notes:** Hi Amanda 

Sick leave captured for M Cerff certificate attached.

https://app.asana.com/app/asana/-/get_asset?asset_id=1210819697600478

16 July 25 - 21 July 2025.

### ✅ Please book my polo for a service Paarl VW
- **Assignee:** Caren Bailey
- **Due:** 2025-07-17
- **Notes:** 62619km 
Inspection light is on
CAA 474453

### ✅ Please renew access
- **Assignee:** Caren Bailey
- **Due:** 2025-07-18

### ✅ Ask Tam about Urban fabrics delivery to Ivy Decor
- **Assignee:** Darren Swanepoel
- **Due:** 2025-07-16

### ✅ Put new number plates on new caddy and license disc
- **Assignee:** Tristan Capes
- **Due:** 2025-07-26

### ✅ Get a quote from Syntech
- **Assignee:** Caren Bailey
- **Due:** 2025-07-10
- **Notes:** https://www.syntech.co.za/product/ugreen-nasync-dxp2800-2-bay-nas/

### ✅ FNB card
- **Assignee:** Caren Bailey
- **Due:** 2025-07-07
- **Notes:** We had to cancel the main business card. 
Please list all subscriptions that we need to change over to a new card.

### ✅ FNB Card
- **Assignee:** Amanda
- **Due:** 2025-07-07

### ✅ When applying for fibre for all clients please confirm if a static public is going to be required for the site instead of applying twice
- **Assignee:** Caren Bailey
- **Due:** 2025-08-22

### ✅ Met with Tawana Sajeni graduate via email
- **Assignee:** Darren Swanepoel
- **Due:** 2025-07-22

### ✅ Log your time in Harvest
- **Assignee:** Unassigned
- **Due:** 2025-07-01
- **Notes:** Ask Mekyle/Tristan for help if required.

### ✅ Log your time in Harvest
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Ask Mekyle/Tristan for help if required.

### ✅ Add a comment to this task to summarize what you’ve learnt at the end of each day
- **Assignee:** Unassigned
- **Due:** 2025-07-01

### ✅ Add a comment to this task to summarize what you’ve learnt at the end of each day
- **Assignee:** Unassigned
- **Due:** 2025-07-02

### ✅ Add a comment to this task to summarize what you’ve learnt at the end of each day
- **Assignee:** Unassigned
- **Due:** None

### ✅ Arguscarhire.com for car rental
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Comfirm if my iPhone 16 Pro Max is specified on the insurance policy
- **Assignee:** Caren Bailey
- **Due:** 2025-06-27

### ✅ Ensure insurance is updated with cars added and removed accordingly once sold.
- **Assignee:** Caren Bailey
- **Due:** 2025-08-06

### ✅ Kit the Caddy
- **Assignee:** Amanda
- **Due:** 2025-06-30

### ✅ Touch base with Farzeen, then schedule with him. We can put him onto projects@d1 calendar and Asana
- **Assignee:** Stafford
- **Due:** None
- **Notes:** farzeenahmed62@gmail.com +27 79 199 5103

### ✅ Reimburse Caleb Flight Tickets to PE
- **Assignee:** Caren Bailey
- **Due:** 2025-06-20
- **Notes:** R959.82 + R285 + R824 = R2068.82

### ✅ Arrange val de vie access for our intern
- **Assignee:** Caren Bailey
- **Due:** 2025-06-24
- **Notes:** farzeenahmed62@gmail.com +27 79 199 5103

### ✅ ChatGPT into meetings
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-21

### ✅ Report
- **Assignee:** Caren Bailey
- **Due:** 2025-06-23
- **Notes:** Prepare a document that shows all of our accounts and which Fibre lines they’re connected to with which ISP and which Fibre provider.

### ✅ Check in Ghaliep when purchasing speaker cable (soundlab)
- **Assignee:** Caleb Thetard
- **Due:** 2025-06-27

### ✅ License to Darren
- **Assignee:** Stafford
- **Due:** 2025-06-13

### ✅ Sort out caddy with we buy cars
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Leave request
- **Assignee:** Amanda
- **Due:** 2025-06-17
- **Notes:** Hi Amanda 

I’ll be on leave 2 days 

26th and 27th June 2025

### ✅ Snapshot for June 2025
- **Assignee:** Caren Bailey
- **Due:** 2025-06-10
- **Notes:** Hi Caren. I Have updated the snapshot for June

### ✅ Name quotes in WeQuote, where it says Untitled Quote
- **Assignee:** Caleb Thetard
- **Due:** 2025-06-06
- **Notes:** As a general habit, lets give each quote a name at the top where it says "Untitled Quote"

### ✅ Process CFS quote it’s for tools/team
- **Assignee:** Caren Bailey
- **Due:** 2025-06-05

### ✅ Get Darren’s proof of tax registration from RTA
- **Assignee:** Caren Bailey
- **Due:** 2025-06-04

### ✅ Discuss Quote doc template
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-10

### ⬜ WeQuote bundles template
- **Assignee:** Caleb Thetard
- **Due:** 2025-08-15
- **Notes:** Create pre-populated bundles with the items we are repeatedly quoting to speed up the process.

### ⬜ Arrange live catalogs from following suppliers
- **Assignee:** Caleb Thetard
- **Due:** 2025-08-15
- **Notes:** Find out what we need to do to get our suppliers to provide pricelists that can automatically be pulled into WeQuote's database and update our database pricing.

### ✅ LAN tester and Cable Toner needed
- **Assignee:** Stafford
- **Due:** 2025-06-03
- **Notes:** https://app.asana.com/0/1202681619836688/1202681619836688 needs a LAN tester .

We need a tester and a toner -we operating with broken things at the moment

### ✅ Buy immune booster supplements for team
- **Assignee:** Stafford
- **Due:** 2025-06-02

### ✅ Asana reports
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-05
- **Notes:** Mekyle's AI reports are EXCELLENT. But can only pull data that's in Asana, so if anything is happening outside of Asana, it's excluded and missed. All work needs to flow through Asana.

### ✅ Please book Sick Leave - note attached  (mekyle)
- **Assignee:** Caren Bailey
- **Due:** 2025-05-29

### ✅ Ask Oonagh (from HB life insurance brokers) if they charge an admin fee as a percentage of the monthly premium
- **Assignee:** Caren Bailey
- **Due:** 2025-05-28
- **Notes:** We are negotiating with a new broker, and the new broker charges a 5% admin fee on our monthly premium. I want to know if that is common practice and if HB life does the same. I don’t remember paying that.

### ✅ Contact private banker and ask to link my company card to my cell number for SMS and Tristan’s card to his phone number
- **Assignee:** Caren Bailey
- **Due:** 2025-05-28

### ✅ 0861236666 to change contract to data only
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-09

### ✅ Add Otter to tech meeting la
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-26

### ✅ Veejay for line drawings?
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-26

### ✅ i only have "comment only" persmission on all new projects created ?
- **Assignee:** Caleb Thetard
- **Due:** 2025-05-26
- **Notes:** sunset/13 steensway etc....any new added project

### ✅ Review mindmap projects and sales
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-26

### ✅ Arrange finance with Chezne from Webuy cars ‪+27 60 538 7164‬
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-30
- **Notes:** Hi Darren 

Both forms are completed as best i could .
You need to complete your personal banking and income info.

### ✅ Arrange Caddy with WeBuy cars.
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-23

### ✅ Day off (family responsibility) for Mekyle
- **Assignee:** Caren Bailey
- **Due:** 2025-05-21

### ✅ Assign AI tool task to everyone
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-23

### ✅ Caddy hunting
- **Assignee:** Caleb Thetard
- **Due:** 2025-05-22
- **Notes:** See if you can find a Diesel 2.0 Caddy cargo panels not windows long wheel base in Western Cape. Under R400k, less than 100k km.

### ✅ What AI tool are you implementing. And how is it going to turbo charge your department?
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-26

### ✅ Fee for BNI
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-29

### ✅ ChatGPT into google meet
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-22

### ✅ Subscribe to projects updates on overview.
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-28

### ✅ Build a D-One custom GPT
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-21

### ✅ Asana AI to give weekly updates across all projects? Or is it per project?
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-19

### ✅ Optimize Opex with AI
- **Assignee:** Amanda
- **Due:** 2025-05-30
- **Notes:** Finance & Invoicing AI
	•	Tool: Xero + AI tools like Vic.ai or Ramp
	•	Use: Automate expense tracking, suggest profit leaks, optimize cash flow.
	•	Benefit: Improve financial visibility and decision-making.


    ChatGPT (Custom GPT) + Xero API
    Use a GPT to answer finance questions or generate a financial summary from Xero data.
    Benefit: You get insights without needing to login or dig through reports.

### ✅ SLA scheduling automated? Caren to have automatic scheduling email
- **Assignee:** Mekyle Cerff
- **Due:** 2025-06-02

### ✅ Pay this please
- **Assignee:** Caren Bailey
- **Due:** 2025-05-19

### ✅ Cancel Shopify site
- **Assignee:** Darren Swanepoel
- **Due:** 2025-07-16

### ✅ Service history to Marinus - phone VW
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-16

### ✅ Contact Medsafe
- **Assignee:** Caren Bailey
- **Due:** 2025-05-14

### ✅ Pay website deposit to AquaWave design - email and send POP
- **Assignee:** Amanda
- **Due:** 2025-05-13

### ✅ Please pay
- **Assignee:** Caren Bailey
- **Due:** 2025-05-13

### ✅ Lutron logins
- **Assignee:** Stafford
- **Due:** None
- **Notes:** integrator@d-one.co.za
qijzi2-kobweq-Wufjaq

### ✅ Memo to Wes LSRA
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-12

### ✅ Mark one H&S?
- **Assignee:** Stafford
- **Due:** 2025-05-12

### ✅ Checkups on status and POA
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Tell Savant to improve their camera feeds in the app. It’s not acceptable
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-14

### ✅ Add Mekyle to medical Aid, remove Rob
- **Assignee:** Caren Bailey
- **Due:** 2025-05-14
- **Notes:** Note that I advised Heinrich that we are going to be moving to a new broker in Paarl soon. Ask them how we can make the changes.

### ✅ Buy network training for Tristan and Mekyle
- **Assignee:** Amanda
- **Due:** 2025-05-12

### ✅ Check if we can register directly with Dahua
- **Assignee:** Mekyle Cerff
- **Due:** 2025-05-09

### ✅ Get into bitcoin - remove from Luno into my wallet
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-08

### ✅ Get Car, laptop and jacket from Rob to Darren
- **Assignee:** Stafford
- **Due:** 2025-05-09

### ✅ check out network IT courses on websites from darren
- **Assignee:** Mekyle Cerff
- **Due:** 2025-05-07
- **Notes:** Udemy
Coursera
IT fundamentals

### ✅ Vehicle license renewals
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Dear   D-ONE ELECTRONICS,
Your vehicle licence for CAA148903 expires on 2025-06-30. The total amount due is R534.00. Renew your licence online at https://online.natis.gov.za/ and your disc will be delivered within 3 to 5 working days to your preferred address.
Alternatively present this notice number 100136903937 at the licensing offices.
Brought to you by the RTMC.

### ✅ Source a new vehicle to upgrade the caddy
- **Assignee:** Amanda
- **Due:** 2025-05-16
- **Notes:** Caddy

### ✅ Finish Crestron training
- **Assignee:** Unassigned
- **Due:** 2025-05-06

### ✅ Confirm if we have the following on General
- **Assignee:** Caren Bailey
- **Due:** 2025-05-07
- **Notes:** Team can help to identify these items

### ✅ Mekyle & Tristan IT networking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-05
- **Notes:** Udemy
Coursera
IT fundamentals
Documentation 
Digital Dice and Pin Point for cabling etc.

### ✅ Pin Point  Please Approve for Month End May 25
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-07
- **Notes:** Hi Darren 

Please approve these?


Invoice 7534 R1564.00 20 Leeukoppie.
Call Out
20 Leeukoppie
23 April 2025
Programmed 6x REM101 remotes to the alarm for panic remotes. Labelled and tested the remotes.
Stafford also asked me to give the guys some training on how to program the remotes to the alarm.

Invoice 7535 R782.00 13 Steensways
Call Out 13 Steens Way 23 April 2025 Programmed 3x REM101 remotes to the alarm for panic remotes. Labeled and tested the remotes.


Invoice 7536 R782.00 6 Barbara

### ✅ Help with summons + Other Added Fines
- **Assignee:** Caren Bailey
- **Due:** 2025-05-02
- **Notes:** I just got this sms. Please arrange sorting or payment. Tx

A summons Ref: B9/16875/803/034562 was issued. Pay within 7 days to stop this process.Please view on http://www.cityofctviewfines.co.za or pay on http://www.paythat.co.za

### ⬜ Build bundles (Systems) in WeQuote
- **Assignee:** Caleb Thetard
- **Due:** None
- **Notes:** See video in WeQuote

### ✅ Optimize Asana notifications so that you are only notified for tasks relevant to you
- **Assignee:** Unassigned
- **Due:** 2025-04-25

### ✅ Find out from WeQuote if we can change our quote number to start at 4xyz so it doens't look like we've only done 100 odd quotes.
- **Assignee:** Caleb Thetard
- **Due:** 2025-05-30

### ✅ Programming Darren's house (programming exercise)
- **Assignee:** Unassigned
- **Due:** 2025-05-06
- **Notes:** While its not so busy its a good time to do some hands on training.

### ⬜ Setup a SLA site for remote monitoring of devices going offline
- **Assignee:** Unassigned
- **Due:** 2025-05-09
- **Notes:** We need to explore remote monitoring of critical devices going offline. This should update us with an email notification.

### ✅ Contact homemation (JHB) ask for Craig Paxman
- **Assignee:** Unassigned
- **Due:** 2025-04-23
- **Notes:** Ask Craig Ovrc questions packedge and araknis

Ask him if he can direct you to tutorials etc 

(011) 781-8887

### ✅ Service 13 Steensway
- **Assignee:** Mekyle Cerff
- **Due:** 2025-04-23

### ✅ Arrange payment
- **Assignee:** Caren Bailey
- **Due:** 2025-04-24

### ✅ Please order paradox programming cable from spectrum
- **Assignee:** Caren Bailey
- **Due:** 2025-04-24

### ✅ Update VAT
- **Assignee:** Amanda
- **Due:** 2025-04-30
- **Notes:** Ensure that VAT is increased to 15.5% on Xero, WeQuote etc.

### ✅ Nexus accounts update
- **Assignee:** Unassigned
- **Due:** 2025-04-22
- **Notes:** As part of ongoing updates and maintenance on the Izwi network we are in the process of migrating our Openserve fibre services to a updated model.
Due to the nature of this update your PPPoE username and password on your router will have to be updated.
This update needs to be completed by 22 April or your service will fail to re-authenticate, possibly resulting in a charged call out being required to restore your service.

Our team will be happy to assist you with this update remotely.
Please le

### ✅ Leave day 2nd of May
- **Assignee:** Caren Bailey
- **Due:** 2025-05-02

### ✅ Update WeQuote quote template copy
- **Assignee:** Caleb Thetard
- **Due:** 2025-05-14

### ✅ Ask Paul for iPad pen Bomax
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-17

### ✅ Find out where the Sipa50 on General shelf is from
- **Assignee:** Caren Bailey
- **Due:** 2025-04-15

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-14

### ✅ Tools and lan tester for Rob
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-14

### ✅ Get a quote for a new window for the Caddy
- **Assignee:** Caren Bailey
- **Due:** 2025-04-16

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-29

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-29

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-30

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-02

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-03

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-11

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-20

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-22

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-23

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-26

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-27

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-29

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-05-30

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-02

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-04

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-05

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-06

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-09

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-10

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-12

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-13

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-17

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-18

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-20

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-23

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-25

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-26

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-06-27

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-07-21

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-07-22

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-07-25

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-25

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-08-26

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-09-01

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-09-02

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-09-05

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-14

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-15

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** 2025-10-16

### ✅ Harvest tracking
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Leave request
- **Assignee:** Amanda
- **Due:** 2025-04-17
- **Notes:** I'd like to request leave for the 17th & 22nd April please

### ✅ Order a UniFi router to test parental controls for devices from Scoop
- **Assignee:** Caren Bailey
- **Due:** 2025-04-07
- **Notes:** Must have unifi cloud, manager, OS and parental control for devices. Looking for the most cost-effective solution under three grand cost.

### ✅ Clean/car wash Silver polo/Robs car
- **Assignee:** Mekyle Cerff
- **Due:** 2025-04-05

### ✅ Sort out caddy/clean up check for door handles etc scrap yard
- **Assignee:** Tristan Capes
- **Due:** 2025-04-03

### ✅ Setup projects@d-one.co.za
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-03

### ✅ Notifications asana
- **Assignee:** Amanda
- **Due:** 2025-04-04
- **Notes:** Is everyone getting only the notifications that they should get on Asana so that it’s actually useful?

### ✅ Think about if you know any electrical engineers that might want to work with Robin.
- **Assignee:** Caleb Thetard
- **Due:** 2025-04-11

### ✅ Send Tristan windows machine for fan repairs
- **Assignee:** Stafford
- **Due:** 2025-05-05

### ✅ Fibre Report
- **Assignee:** Caren Bailey
- **Due:** 2025-04-04
- **Notes:** Run a fibre report for Previous month

### ✅ Fibre Report & Aged Anaylis
- **Assignee:** Caren Bailey
- **Due:** 2025-04-17
- **Notes:** Run a fibre report for Previous month

### ✅ Fibre Report
- **Assignee:** Caren Bailey
- **Due:** 2025-06-05
- **Notes:** Run a fibre report for Previous month

### ✅ Fibre Report
- **Assignee:** Caren Bailey
- **Due:** 2025-07-03
- **Notes:** Run a fibre report for Previous month

### ✅ Fibre Report
- **Assignee:** Caren Bailey
- **Due:** 2025-08-07
- **Notes:** Run a fibre report for Previous month

### ✅ Fibre Report & Payment in Rprt
- **Assignee:** Caren Bailey
- **Due:** 2025-05-27
- **Notes:** Run a fibre report for Previous month

### ✅ Fibre Report & Payment in Rprt
- **Assignee:** Caren Bailey
- **Due:** 2025-06-05
- **Notes:** Run a fibre report for Previous month

### ✅ Monthly Age Analysis June 25
- **Assignee:** Caren Bailey
- **Due:** 2025-07-08
- **Notes:** Run a fibre report for Previous month

### ✅ Do we want another intern like Tiffany?
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-31

### ✅ Spectrum order Tony Faraar
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Tony Farrar (Base construction)

1X medium door mag 

1X large door mag

Reyaan will collect today please

### ✅ Asana Project updates will run Mondays for past week ..
- **Assignee:** Mekyle Cerff
- **Due:** None
- **Notes:** °Keep your tasks due dates current or ahead 

•Feedback - if task is ongoing , a feedback/progress comment   and adjust due date

•new automation rules in testing phase but everyone's input with the above could speed up things 🙂

### ✅ Ensure we have a system to check that every output has an input and a profit
- **Assignee:** Amanda
- **Due:** 2025-03-26

### ✅ SLA services schedule
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-31

### ✅ Leave request for the 31st March
- **Assignee:** Amanda
- **Due:** 2025-03-27

### ✅ Sick Leave Tristan Capes
- **Assignee:** Caren Bailey
- **Due:** 2025-03-25
- **Notes:** Hi All

2 Day Sick leave captured for Tristan. Certificate attached

### ✅ Tony Farrar (Base) projects order asap we are invoicing him afterwards
- **Assignee:** Caren Bailey
- **Due:** 2025-03-24
- **Notes:** Please order the equipment as per subtasks

### ✅ Wall of fame/shame
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-27

### ✅ SnapShot Invoice/Follow up
- **Assignee:** Caren Bailey
- **Due:** 2025-03-24
- **Notes:** HI Guys

On the match snapshot i have a column for comments.

We need to invoice some, this is on the snapshot page, then also follow up on Monday in.

Caren will you sit with Caleb to make sure the final invoices are making sense before you send them off to clients?

We need to focus ALOT of attention for getting money in. Please start on this ASAP!. This is vital. We have lots of money that we need to pay at the end of the month.

Thanks

### ✅ Projections
- **Assignee:** Caleb Thetard
- **Due:** None
- **Notes:** HI Guys

I need to start for-casting more accurately.

Can us three have a meeting next week to kick this off?

When suits you both?

### ✅ Service alarms
- **Assignee:** Mekyle Cerff
- **Due:** 2025-04-01

### ✅ Call Andrian the builder (Loy builder) number sent on WhatsApp
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-12

### ✅ Rob to Llands?
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-12

### ✅ Asana reporting looking really good. We're going in the right direction
- **Assignee:** Mekyle Cerff
- **Due:** 2025-03-10

### ✅ Annual discussion timing schedule
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-10

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-03-10

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-03-17

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-03-24

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-04-03

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-04-07

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-05-19

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-05-26

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-06-02

### ✅ Wall of shame Harvest & Asana reports
- **Assignee:** Stafford
- **Due:** 2025-06-09

### ✅ Do tutorials on the following:
- **Assignee:** Tristan Capes
- **Due:** None

### ✅ Do Trinnov exam, so Bryan can give us our hoodies
- **Assignee:** Caleb Thetard
- **Due:** 2025-03-11

### ✅ Trinnov exam and sizes to Bryan
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-12

### ✅ Please get rob registered for Val die Vie
- **Assignee:** Caren Bailey
- **Due:** 2025-03-18
- **Notes:** Caren please comment what you require from Rob

### ✅ Increase our hourly rates
- **Assignee:** Caleb Thetard
- **Due:** 2025-03-07
- **Notes:** Please increase our hourly rates for installation R800 ph and programming R1000 ph. ex VAT.

### ✅ Change calendar name from Imti to Rob or integrator
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-05

### ✅ Update Asana photo
- **Assignee:** Unassigned
- **Due:** 2025-03-03

### ✅ Send Mands Mileage for travel
- **Assignee:** Unassigned
- **Due:** 2025-03-28

### ✅ Rob Tee email signature
- **Assignee:** Unassigned
- **Due:** 2025-03-07
- **Notes:** "System Integrator"
+27 (79) 166-9663

### ✅ Printer Set Up Dalven
- **Assignee:** Unassigned
- **Due:** 2025-03-04
- **Notes:** Hi Rob

Please could you install the program and set up the Printer in the Office at Dalven?

2 Jaguar Park 
14th Avenue, Voortrekker road Maitland 7405

### ✅ Staff Tees and caps
- **Assignee:** Amanda
- **Due:** 2025-03-04
- **Notes:** Caleb L, Cap
Mekyle S, Cap, Shorts, Jacket
Tristan M, Shorts, Cap
Edwin S, Beanie
Rob L, Cap, Beanie, Jacket
Stafford, XXL, Shorts, Beanie
Darren, Beanie

### ✅ [Duplicate] Make D-One shirts for Rob Tee
- **Assignee:** Amanda
- **Due:** 2025-03-03

### ✅ Team Meetup @DVDV
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-03

### ✅ Handover Imti’s laptops to Darren
- **Assignee:** Stafford
- **Due:** 2025-02-28

### ✅ Ask Rob if we can pay him a travel allowance
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-03

### ✅ Discuss car with Rob
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-03

### ✅ Arrange for Rob to get car and laptops
- **Assignee:** Stafford
- **Due:** 2025-03-02

### ✅ Asana training session and Rob intro Monday + Daily checkins Asana
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-03

### ✅ Asana FA Cup Group discussion and morning checkins
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-03

### ✅ Annual increase discussion
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-21

### ✅ BNI
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-20

### ✅ Feedback on Asana project management
- **Assignee:** Stafford
- **Due:** 2025-02-20

### ✅ Fibre Suspension- Challenger Coal
- **Assignee:** Caren Bailey
- **Due:** 2025-02-20
- **Notes:** Good day Stafford and Team

Please could you confirm that Unit 401 AVH Battery Elemental on Battery has been suspended as the client cancelled the fibre with us?

Is there anything that we need to remove for this unit?

I will collect the arrears owed please just let me know if they cannot use our fibre ONT.

### ✅ Asana colour-coding and project status
- **Assignee:** Mekyle Cerff
- **Due:** 2025-02-19
- **Notes:** I like what I'm seeing with the project colours updating. Lets agree what the colours are, and apply it across D-One.

### ✅ Refund Caleb
- **Assignee:** Amanda
- **Due:** 2025-02-16

### ✅ Recon, Payments Invoices
- **Assignee:** Caren Bailey
- **Due:** 2025-02-13

### ✅ Share B&O speakers model numbers etc for research on setting them up for B&O day
- **Assignee:** Mekyle Cerff
- **Due:** 2025-02-12

### ✅ Invoice - Zenni
- **Assignee:** Caren Bailey
- **Due:** 2025-02-10
- **Notes:** Hi Darren

Please could you send me the Invoice?
ZENNI D-ONE ELECTRONICSElectronics R14999.00.

Thank you
Caren

### ✅ Data for Mekyle
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-10
- **Notes:** Cellc - 0627372487


This is only for when not at home or on sites without WiFi in car etc...  not much is required 

Sent some data. Keep me posted.

### ✅ Query Flight change fee on email
- **Assignee:** Caren Bailey
- **Due:** 2025-02-10

### ✅ Chat to Mekyle about Asana dominance
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-10

### ✅ UPDATE SAVANT PROFILE EMAIL
- **Assignee:** Mekyle Cerff
- **Due:** None

### ✅ Have We claimed our projects onto SAVANT Central Management? I Only see your Home
- **Assignee:** Mekyle Cerff
- **Due:** 2025-02-10

### ✅ Rules
- **Assignee:** Mekyle Cerff
- **Due:** 2025-02-07
- **Notes:** According to Asana, we should have rules available. Let me know if you're able to create the automations that you want to. Otherwise we can reach out to Asana help to find out how.

Rules (250 actions per month)

### ✅ Phone for Edwin
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-05
- **Notes:** His phone was broken on site while helping Steve upping with a mirror now he’s not able to do a sauna or get colds etc. is there something we can do to help him arrange a smart phone?

### ✅ See if we can trace the unit that’s in the attachment
- **Assignee:** Stafford
- **Due:** 2025-02-07

### ✅ Unifi
- **Assignee:** Unassigned
- **Due:** None

### ✅ Email forwarding integrator
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-06

### ✅ Leave Approval for 14th February 2025
- **Assignee:** Amanda
- **Due:** 2025-02-07
- **Notes:** Hi Darren & Amanda

May I have 1 Leave day for the 14th of February 2025?

It's my 25th Wedding Anniversary. 

Let me know, thank you

### ✅ Bring that massive D-One banner from the upstairs office. For the B&O day
- **Assignee:** Tristan Capes
- **Due:** 2025-02-11

### ✅ Wifi at 101 Element on Battery Alison Howard Smith
- **Assignee:** Caren Bailey
- **Due:** 2025-01-31
- **Notes:** Hi Team

New owner took over unit 101 at Elements of Battery.

Alison and Edwin Smith.

I have confirmed this the July Mashwana, he sold his apartment.

I will invoice them as the account is up to date until the end Jan 25.
Will load a new client onto Xero .

They will need the following:

Questions: 
1.  Is there a password that we should use? 
2.  Also, what "profile/name" should we log onto? 

thank u

### ✅ Temu racket Stafford
- **Assignee:** Darren Swanepoel
- **Due:** 2025-01-28

### ✅ Consignment stock list to Marc
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-04

### ✅ Admin emails to Caren not Mekyle
- **Assignee:** Darren Swanepoel
- **Due:** 2025-01-29

### ✅ Please order below for my Laptop  - as mine is currently damaged
- **Assignee:** Caren Bailey
- **Due:** 2025-01-28
- **Notes:** https://www.takealot.com/3m-long-fast-type-c-to-type-c-charging-cable-ca-8085/PLID92651516

https://www.takealot.com/multiport-5-in-1-anv-type-c-to-hdtv/PLID96363560

### ✅ Handover document
- **Assignee:** Unassigned
- **Due:** 2025-01-30
- **Notes:** Prepare a handover document with all the necessary credentials for computers, software, logins sites, etc.

### ✅ Rob Tee contract
- **Assignee:** Amanda
- **Due:** 2025-02-03
- **Notes:** Write up an employment contract with all employment details and probation specifics, benefits, expectations, values, etc.

### ✅ Hely Hutch no Payment made Apparently will only get paid end of next month
- **Assignee:** Unassigned
- **Due:** None

### ✅ Collect Sonos port from Darren’s
- **Assignee:** Stafford
- **Due:** 2025-01-22

### ✅ Sell indoor AC
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Fond details for the indoor AC unit we bought for Imti. And sell it on Facebook marketplace

### ✅ Hunt this P013857 if possible it was used at homemation
- **Assignee:** Caren Bailey
- **Due:** 2025-01-22

### ✅ Cable pricing from Ghalieb. See if it’s cheaper for next order
- **Assignee:** Stafford
- **Due:** 2025-01-24

### ✅ Send list of Ajax stock on general shelf
- **Assignee:** Caren Bailey
- **Due:** 2025-01-22
- **Notes:** George Steyn needs to buy some

### ✅ Suspend Internet Accounts 2 Month Arrears
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Good Day Team

I have Invoiced, emailed and called these clients.

No reply received, please suspend the account.

Thank you

### ✅ Istore Invoice for R25 299.00
- **Assignee:** Darren Swanepoel
- **Due:** 2025-01-23
- **Notes:** Hi Darren

Please send me the Invoice for Istore once received.

ISTORE CAVENDISH 485442*4307 15 JAN 74067245015143242660659 R25 299.00.

Thank you.
C

### ✅ Accounts Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2025-01-20

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2025-01-16

### ✅ Settle Vodacom
- **Assignee:** Darren Swanepoel
- **Due:** 2025-01-20

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-24

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-25

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-26

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-27

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-28

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2025-03-31

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-01

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2025-04-02

### ✅ Log Harvest
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** Rescheduled for review week of 16 Mar

### ✅ Tech Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2025-01-16

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2025-01-16

### ✅ Chat to Marc (Planetworld) regarding upcoming projects
- **Assignee:** Caleb Thetard
- **Due:** 2025-01-16

### ✅ Harvest tracking for team
- **Assignee:** Stafford
- **Due:** 2025-01-16
- **Notes:** Remeber to get back in the Harvest rhythm and track time.

### ✅ IR Learner
- **Assignee:** Unassigned
- **Due:** 2025-01-17

### ✅ Sort Google Drive syncing on Mac
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-08

### ✅ Sign in to Unifi app and afrihost
- **Assignee:** Darren Swanepoel
- **Due:** 2025-01-13

### ✅ Renew vehicle license
- **Assignee:** Darren Swanepoel
- **Due:** 2025-02-08
- **Notes:** Dear   D-ONE ELECTRONICS,
Your vehicle licence for DONEWP expires on 2025-02-28. The total amount due is R780.00. Renew your licence online at https://online.natis.gov.za/ and your disc will be delivered within 3 to 5 working days to your preferred address.
Alternatively present this notice number 100136604058 at the licensing offices.
Brought to you by the RTMC.

### ✅ Send Imti travel log report in excel from Cartrack from Aug - End Dec
- **Assignee:** Caren Bailey
- **Due:** 2025-01-13
- **Notes:** With the mileage on the right hand side.

### ✅ Overtime
- **Assignee:** Amanda
- **Due:** 2024-12-20

### ✅ Send invoices to Marc
- **Assignee:** Caren Bailey
- **Due:** 2025-01-15
- **Notes:** Search our system for all supplier invoices and POs for the Savant Intercoms that we sent back to Planetworld yesterday. 

And send them to Marc.

### ✅ Book out
- **Assignee:** Caren Bailey
- **Due:** 2024-12-18

### ✅ Add P5 dimmer in upstairs office to general shelf
- **Assignee:** Caren Bailey
- **Due:** 2025-01-17

### ✅ Collect PSIRA docs
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Snapshot schedule meeting
- **Assignee:** Amanda
- **Due:** 2024-12-17

### ✅ Query if staff that didn’t reply received bonus email
- **Assignee:** Amanda
- **Due:** 2024-12-17

### ✅ Clean Asana
- **Assignee:** Darren Swanepoel
- **Due:** 2024-12-23

### ✅ Collect PSIRA registration.
- **Assignee:** Darren Swanepoel
- **Due:** 2025-01-27
- **Notes:** Check where we are with this I can’t remember where we got to

### ✅ Follow up on RMA for Savant Remote. Email Kevin
- **Assignee:** Caren Bailey
- **Due:** 2025-03-13

### ✅ Caleb Leave Thursday December 12th
- **Assignee:** Caren Bailey
- **Due:** 2024-12-12
- **Notes:** I would like to take Leave on Thursday December 12th

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-12-09

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-12-05

### ✅ Service phone plan
- **Assignee:** Darren Swanepoel
- **Due:** 2024-12-12

### ✅ Locations Update Invoice
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** HI Caren

Please add the locations for these invoices/Credit

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-12-02

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-12-02

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-12-02

### ✅ NeaMetrics Account Form
- **Assignee:** Caleb Thetard
- **Due:** 2024-12-05
- **Notes:** As per my 2 emails please complete the dealer reg form

### ✅ Leave
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** https://Www.simplepay.co.za

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-11-25

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-11-25

### ✅ Invoice Dave Whitehead for the speakers he collected.
- **Assignee:** Caren Bailey
- **Due:** 2024-12-02

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-11-25

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-11-18

### ✅ Replenish speaker cable for VDV store
- **Assignee:** Caren Bailey
- **Due:** 2024-11-13
- **Notes:** Order 5 rolls of speaker cable from supplier to replenish stock.

### ✅ Imti leave Friday afternoon 22 Nov
- **Assignee:** Amanda
- **Due:** 2024-11-12
- **Notes:** Imti has requested leave for the afternoon of 22 November. I said I am ok with it. We just need to prioritize sites etc.

### ✅ Check with Kevin Regarding SAVANT PDU
- **Assignee:** Caleb Thetard
- **Due:** 2024-11-11

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-12-09

### ✅ Tetnis Tristan
- **Assignee:** Darren Swanepoel
- **Due:** 2024-11-11

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-11-11

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-11-11

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-11-11

### ✅ Get Asana running smoothly
- **Assignee:** Stafford
- **Due:** None

### ✅ Edwin on leave Friday the 8th November
- **Assignee:** Amanda
- **Due:** 2024-11-08

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-11-04

### ✅ See where we can get job card books from please
- **Assignee:** Caren Bailey
- **Due:** 2024-11-08

### ✅ Mands asana notifications
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Please check my cell phone contract age and whens its due for upgrade
- **Assignee:** Caren Bailey
- **Due:** 2024-11-04

### ✅ Get Logins for Tristan and Mekyle for Crestron
- **Assignee:** Caleb Thetard
- **Due:** 2024-11-07

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-11-04

### ✅ Programming opportunities
- **Assignee:** Mekyle Cerff
- **Due:** None
- **Notes:** Are you interested in developing your programming abilities? 
We have Crestron that we are starting. 
And can develop Savant further if you are interested.

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-11-04

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-11-04

### ✅ Renew Edwin access to VDV
- **Assignee:** Caren Bailey
- **Due:** 2024-11-06
- **Notes:** Dear Edwin Lyons your access to Val de Vie Estate will expire in 7 days 08/11/2024, Please report to the Security Registration office to extend your access period.

### ✅ Drop ladder at sales hire
- **Assignee:** Tristan Capes
- **Due:** 2024-10-30

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-10-31

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-31

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-10-31

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-31

### ✅ Get glands and hole saw from hardware
- **Assignee:** Tristan Capes
- **Due:** 2024-10-28

### ✅ Collect Strydom stock at office
- **Assignee:** Tristan Capes
- **Due:** 2024-10-28

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-10-28

### ✅ Leave
- **Assignee:** Tristan Capes
- **Due:** 2024-10-25

### ✅ Collect ladder at sales hire
- **Assignee:** Tristan Capes
- **Due:** 2024-10-30

### ✅ Call Judith
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-31

### ✅ Cartrack Imti Schedule for Oct 24
- **Assignee:** Caren Bailey
- **Due:** 2024-10-30
- **Notes:** Hi 

Send tracker report to Imti for Sept 24.

### ✅ Jetbuilt pull plug confirmation
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-29
- **Notes:** Last check… Can I pull the plug?

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-28

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-10-28

### ✅ Confirm invoicing projects for this month
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-25

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-10-24

### ✅ Bryner (Neil’s wife name)
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-21

### ✅ Review last 2 months calendar
- **Assignee:** Stafford
- **Due:** 2024-10-21
- **Notes:** Go through your calendar over the last two months and find ad hoc billing that Caren can invoice for.

### ✅ Tech meeting notes
- **Assignee:** Stafford
- **Due:** 2024-10-21

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-21

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-17

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-10-17

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-14

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-10-14

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-14

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-10

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-10-10

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-10

### ✅ Setup admin email for Mekyle
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-18

### ✅ Accounts meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-10-07

### ✅ meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-07

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-10-07

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-07

### ⬜ Integrate Crestron pricing into WeQuote
- **Assignee:** Caleb Thetard
- **Due:** 2025-05-30

### ✅ Confirm if there is an araknis 16 port switch in general
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-03

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-10-03

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-10-03

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-10-03

### ✅ Attend Crestron Home Webinar
- **Assignee:** Unassigned
- **Due:** 2024-10-02

### ✅ Reconfigure Sonos at Heyday
- **Assignee:** Unassigned
- **Due:** 2024-10-03

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-03

### ✅ Leave Request Mekyle
- **Assignee:** Amanda
- **Due:** 2024-10-07
- **Notes:** Hi Mands... I'd like to book leave for the day's 28th, 29th , 30th ,  31st October and 1st November please 
TIA

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-09-30

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-09-30

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-30

### ✅ Tristan leave request
- **Assignee:** Amanda
- **Due:** 2024-09-27
- **Notes:** Hi Amanda, i would like to put in leave for the 25th of October.

### ✅ Booking for quad biking? Confirm plan
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-23

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-09-23

### ✅ Book quad biking
- **Assignee:** Amanda
- **Due:** 2024-09-23

### ✅ Desvaux stock
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** 1 Spec palladiom has been taken from the storeroom for Desvaux 

Imti nothing on Jetbuild not sure if this was taken from other projects.

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-23

### ✅ meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-09-19

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-09-23

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-09-19

### ✅ Drone for Oakvale, Vigne and Vrymans
- **Assignee:** Darren Swanepoel
- **Due:** 2024-10-15

### ✅ 12 foot A-Frame ladder
- **Assignee:** Caren Bailey
- **Due:** 2024-09-19
- **Notes:** Please contact SA ladder for a quote 12 foot A-Frame ladder

### ✅ Replace stock at Darrens emergency store
- **Assignee:** Caren Bailey
- **Due:** 2024-09-19
- **Notes:** I took 2x 100m rip cord and 1 pack of T50r cable ties.

### ✅ Allocate users to Asana
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-16

### ✅ Cancel Jetbuilt
- **Assignee:** Darren Swanepoel
- **Due:** 2024-11-05

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-16

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-09-16

### ✅ Reduce Jetbuilt subscription
- **Assignee:** Amanda
- **Due:** 2024-09-12
- **Notes:** If we can’t cancel it. Remove the users so we’re only paying for one.

### ✅ Get a quote to replace the battery for the Apple iPad Pro 11’ with Digicape
- **Assignee:** Caren Bailey
- **Due:** 2024-09-13
- **Notes:** Model: MU102HC/A
Serial DMPZF6S3KD86

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-09-12

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-09-12

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-12

### ✅ Cancel Instagantt and get refund.
- **Assignee:** Caren Bailey
- **Due:** 2024-09-18

### ✅ More D-One caps
- **Assignee:** Amanda
- **Due:** 2024-09-13

### ✅ Plan Cape Town day
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-09

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-09-05

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-09-05

### ✅ Tools
- **Assignee:** Stafford
- **Due:** 2024-09-26
- **Notes:** we should list down what we need per team ... 
Populate items under your subtasks

### ✅ DAHUA
- **Assignee:** Unassigned
- **Due:** None

### ✅ Sales Forecast
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-06
- **Notes:** HI Guys

Is it possible to get a sales forecast for the next 6 month - main focus would be invoice date.

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-09-02

### ✅ Team activity
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-27
- **Notes:** We'll have a get together on the 27th. Lets have some suggestions in the subtasks.

### ⬜ Compare with Scoop to see if we buy from these guys
- **Assignee:** Caleb Thetard
- **Due:** None
- **Notes:** U6-E.      R 4 995.00 ex vat
U6-Mesh R 3 140.00 ex vat
U6 plus R 1 702.00 ex vat 
U7-Pro R 3 325.00 ex vat
U6-LR R 3 219.00 ex vat 
UDM-Pro R 7 512.00 ex vat 
UX R 2 196.00 
16 Port POE R 5 388.00
24 Port POE R 6 715.00 ex vat 
48 Port Pro Max POE R 21 785.00 ex vat 
UXG-Lite R 2 245.00 ex vat
UXG-Pro R 8 835.00 ex vat

### ✅ Book out stock
- **Assignee:** Caren Bailey
- **Due:** 2024-08-30
- **Notes:** Dropped off 4x Sonance IS8 speakers 93479
Dropped off loan item clickshare bar

Delivered to planetworld

### ✅ Richard re UniFi
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-30

### ✅ Harvest for the week
- **Assignee:** Stafford
- **Due:** 2024-08-30

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-09-02

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-09-02

### ✅ Service calls after hours
- **Assignee:** Stafford
- **Due:** 2024-08-30
- **Notes:** Hi Kobus 

I hope you are well.

Please can help us with a way forward regarding a strategy to manage service calls after hours.

### ✅ Check why my polo that I drive isn’t on service plan and how do we renew it. CAA 148903
- **Assignee:** Caren Bailey
- **Due:** 2024-08-27
- **Notes:** Hi Caren

Discussed with Amanda earlier, as per barons the vehicle isn’t under service plan and quotes will be done before commencing any work

### ✅ Team catchup get together
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-30

### ✅ Explore quality LAN tester - search secondhand. And place order
- **Assignee:** Caleb Thetard
- **Due:** 2025-05-30
- **Notes:** We need to be able to properly test LAN cables. See if there's any products out there that we can secure for the teams, so we can do proper cable tests. Fluke makes one that is really pricey.

### ✅ Order Label printer
- **Assignee:** Caren Bailey
- **Due:** 2024-08-27
- **Notes:** Specify the model and details for Caren to order, including label tape.

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-08-26

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-08-29

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-26

### ✅ Appraisal Imti
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-23

### ✅ Assist pin/point Clyde at the quarry
- **Assignee:** Unassigned
- **Due:** 2024-08-27
- **Notes:** Pin point installing  a new switch, current switch has Vlans setup they need it copied to new switch 

Log hours for billing please

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-22

### ✅ meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-08-22

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-08-22

### ✅ Monthly Stock take Warehouse
- **Assignee:** Caren Bailey
- **Due:** 2024-08-29
- **Notes:** We currently did Stock take on 
Strydom 
Wach
Oakvale
Uppink
Vigne

Myself and Roger find that the guys taking stuff and removing and not always informing us.

### ✅ Do the Crestron training courses that are relevant
- **Assignee:** Caleb Thetard
- **Due:** 2025-04-25
- **Notes:** Online Crestron Core Track Course

### ✅ Crestron courses
- **Assignee:** Unassigned
- **Due:** 2025-01-31
- **Notes:** Do the programming courses online

### ✅ Meeting notes Caleb
- **Assignee:** Stafford
- **Due:** 2024-08-19

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-08-19

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-19

### ✅ Stafford polo service
- **Assignee:** Caren Bailey
- **Due:** 2024-08-19
- **Notes:** Please book my polo in for a service inspection light is coming on CAA 148-903

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-08-15

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-08-15

### ✅ Send July Tracker Travel log for Silver VW Polo CAA474453
- **Assignee:** Amanda
- **Due:** 2024-08-14

### ✅ migrating from jetbuilt to wequote
- **Assignee:** Caleb Thetard
- **Due:** 2024-10-11

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-12

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-08-12

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Admin work
- **Assignee:** Caren Bailey
- **Due:** 2024-08-08

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-08-08

### ✅ 36 Pushups
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-08

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-08

### ✅ Caleb Leave Thursday 08 August
- **Assignee:** Amanda
- **Due:** 2024-09-05
- **Notes:** I will be taking leave on Thursday 08 August

### ✅ Test asana
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-07

### ✅ Monday Morning Meeting
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-08-05

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-08-05

### ✅ Crestron
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-19

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-08-01

### ⬜ Daily duties
- **Assignee:** Unassigned
- **Due:** None

### ✅ Harvest yesterday
- **Assignee:** Unassigned
- **Due:** 2024-07-31

### ✅ Recon Entries
- **Assignee:** Caren Bailey
- **Due:** 2024-07-30

### ✅ Do Appraisal with Mekyle
- **Assignee:** Darren Swanepoel
- **Due:** 2024-08-29
- **Notes:** 1. Job Satisfaction
2. Career Development
3. Team Dynamics
4. Work Environment
5. Management Support
6. Company Culture
7. Feedback and Recognition
8. Work-Life Balance
9. Goals and Expectations
10. Suggestions for Improvement

### ✅ Meeting Notes (Caleb)
- **Assignee:** Caleb Thetard
- **Due:** 2024-07-29

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-07-29

### ✅ Caleb Leave Tuesday 30th July and Thursday 1 August
- **Assignee:** Caren Bailey
- **Due:** 2024-07-29

### ✅ Order from CFS for delivery to DVDV for Winelands cabcon stock in Darren’s garage.
- **Assignee:** Caren Bailey
- **Due:** 2024-07-30
- **Notes:** 5x black Plugtops -
100x CAT6 RJ45 plugs and boots 
5x 6 way Multiplugs
T50R Cableties 
T18R Cableties 
20x 2m CAT6 Patch leads 
20x 1m CAT6 Patch leads
Flat TV bracket for 65” TV- linkqage done
500m CAT6
500m 1mm flex SPEAKER cable 

10 x 12V 3A power supplies -  regal 
10 x 5V 2A power supplies - regal

### ✅ Confirm if we’re still keeping capital in interest bearing accounts
- **Assignee:** Amanda
- **Due:** 2024-07-24

### ✅ After hours Whatsapp
- **Assignee:** Stafford
- **Due:** 2024-08-26
- **Notes:** Consider after-hours Whatsapp solution for personal time.
Setup sleep mode to remove Whatsapp between certain times etc.

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-07-22

### ✅ Claim logged for Accident Imti via Insurance
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Imti claim for accident incident 

1. Fully completed and signed claim form
2. Copy of drivers drivers license
3. Police case number - received
4. Repair quote
5. Photo's of damages - received
6. Photo of vehicle license disc

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-07-15

### ✅ Get RF cable from space television
- **Assignee:** Tristan Capes
- **Due:** 2024-07-16

### ✅ Purchase safety boots at Gfox
- **Assignee:** Tristan Capes
- **Due:** 2024-07-16

### ✅ Drop off camera at Sensor and in for repairs take pics of model and serial number for our reference/tracking
- **Assignee:** Tristan Capes
- **Due:** 2024-07-17

### ✅ Half Day for Hospital Groote Shuur
- **Assignee:** Amanda
- **Due:** 2024-07-16

### ✅ Enroll Stafford and Mekyle for VDV access also check Tristan Edwin and Imti’s expiry dates as well as Caleb
- **Assignee:** Caren Bailey
- **Due:** 2024-07-17

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-07-15

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-07-15

### ✅ Cancel Asana we are still on the package
- **Assignee:** Amanda
- **Due:** 2024-07-15

### ✅ Tech Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-07-15

### ✅ Please order boots for tristan asap
- **Assignee:** Caren Bailey
- **Due:** 2024-07-15
- **Notes:** Order from a company called GFox Dalven uses them. Size 7 black

### ✅ loading Oculus Invoices May June comm & Other Invoices
- **Assignee:** Caren Bailey
- **Due:** 2024-07-11

### ✅ Leave Request for Tristan and Edwin
- **Assignee:** Amanda
- **Due:** 2024-07-15

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-07-11

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-07-11

### ✅ Stock Takes
- **Assignee:** Caren Bailey
- **Due:** 2024-07-17
- **Notes:** Oakvale - On site too
Marwyk
Stonehendge
Desvaux
Harrigan
Brandt
Red Earth _Val Du Luc
Vigne D'Or
Loy
Strydom
Uppink
Roos

### ✅ Track time in harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2024-07-15

### ✅ Fibre Piping at Dalven
- **Assignee:** Tristan Capes
- **Due:** 2024-07-26
- **Notes:** Hi Stafford 

Please let me know who can fix the Fibre piping at Dalven , they managed to put it back but its still not secure enough.

### ✅ Report on whats still outstanding
- **Assignee:** Unassigned
- **Due:** 2024-07-11

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-07-08

### ✅ Review harvest and asana
- **Assignee:** Darren Swanepoel
- **Due:** 2024-07-15

### ✅ Make the proposal template on Jetbuilt look neater
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** Can you make it look better? Different highlighting and fonts and columns.

### ✅ Challenger Coal Wifi - Afrihost suspend Account
- **Assignee:** Caren Bailey
- **Due:** 2024-07-10
- **Notes:** Hi Stafford and Imti 

Can we suspend the account as the account is in arrears please.

### ✅ First aid kits for teams X2
- **Assignee:** Caren Bailey
- **Due:** 2024-07-11

### ✅ WIFI ZOE DOYLE 202 Boulders
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** I just arrived back in Cape Town and no longer have wifi in the apartment. How can we get it back up and running?

### ✅ Tech Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2024-07-01

### ✅ Pack stock for Tristan
- **Assignee:** Darren Swanepoel
- **Due:** 2024-07-13

### ✅ Add Mekyle & Caleb to team in Harvest
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-27

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-06-27

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-27

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-06-27

### ✅ Brother Laminated refill for Site
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Order 2 TZe-221 brother laminated 9mm refill for site Black on white

### ✅ Sick Leave
- **Assignee:** Amanda
- **Due:** 2024-06-26

### ✅ Send motor docs to UShopidrop
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-25

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-06-24

### ✅ Wife and Daughter Hospital Appointment: 25 June 2024
- **Assignee:** Unassigned
- **Due:** 2024-06-25
- **Notes:** Wife and Daughter Hospital Appointment: 25 June 2024
Duration: 1 Day
Return to work: 26 June 2024

### ✅ Paternity Leave: 20 May 2024 ->30 May 2024
- **Assignee:** Unassigned
- **Due:** 2024-05-30
- **Notes:** Paternity Leave: 20 May 2024 ->30 May 2024
Duration: 10 Days
Back at work on: 31 May 2024

### ✅ Sick Leave Clinic Appointment
- **Assignee:** Amanda
- **Due:** 2024-06-21

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-24

### ✅ Sick Leave
- **Assignee:** Amanda
- **Due:** 2024-06-24
- **Notes:** Hey Stafford

I think you where sick last week? Did you create a task with all the details.

### ✅ Can we arrange D1 cups for the guys
- **Assignee:** Amanda
- **Due:** 2024-07-05

### ✅ Meetings notes
- **Assignee:** Stafford
- **Due:** 2024-06-20

### ✅ Public holiday
- **Assignee:** Tristan Capes
- **Due:** 2024-06-17

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-20

### ✅ Export all Asana time  and change to Asana Free
- **Assignee:** Amanda
- **Due:** 2024-06-18

### ✅ YOUTH DAY (PUBLIC HOLIDAY)
- **Assignee:** Unassigned
- **Due:** 2024-06-17

### ✅ Tech Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-18

### ✅ meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-06-18

### ✅ Sccoof SFPs Purchase
- **Assignee:** Unassigned
- **Due:** 2024-06-11

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-06-18

### ✅ Office (Stock collect)
- **Assignee:** Unassigned
- **Due:** 2024-06-11

### ✅ Review Proposals and Contract in Jetbuilt - move to correct phase
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-24

### ✅ Business cards to Caleb
- **Assignee:** Caleb Thetard
- **Due:** 2024-09-09

### ✅ Share projects with Mands
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-18

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-18

### ✅ Complete LANCOM Partner application and send back to Caleb
- **Assignee:** Caleb Thetard
- **Due:** 2024-06-12

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-06-10

### ✅ Pharmacy
- **Assignee:** Unassigned
- **Due:** 2024-06-03

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-06-10

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-10

### ✅ Contact Westcon for Ruckus account
- **Assignee:** Caren Bailey
- **Due:** 2024-06-07
- **Notes:** Hi Caren,

We need to register as a Westcon partner

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-27

### ✅ Check if POLO CAA 148-903 is covered for brakes under the plan
- **Assignee:** Caren Bailey
- **Due:** 2024-06-06

### ✅ Pipeline in Jetbuilt
- **Assignee:** Caleb Thetard
- **Due:** 2024-06-06
- **Notes:** Organize Jetbuilt pipeline to reflect our Sales forecast.

### ✅ Challenge Vodacom account
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-20

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-06

### ✅ CREATE SAVANT PROFILE FOR MEKYLE
- **Assignee:** Unassigned
- **Due:** 2024-06-03
- **Notes:** @

### ✅ Emergency Sick Leave
- **Assignee:** Amanda
- **Due:** 2024-06-24
- **Notes:** I am unfit for work today , been to the pharmacy on Saturday for some meds but hasnt did its job yet

### ✅ Tech Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2024-06-03

### ✅ Overtime
- **Assignee:** Amanda
- **Due:** 2024-05-20

### ✅ Sort out fine at VDV registration centre
- **Assignee:** Tristan Capes
- **Due:** 2024-05-22

### ✅ Drop bubble wrap at Darren's place
- **Assignee:** Tristan Capes
- **Due:** 2024-05-16

### ✅ Dahua paper
- **Assignee:** Darren Swanepoel
- **Due:** 2024-06-10

### ✅ Strategy 13-17 May
- **Assignee:** Caleb Thetard
- **Due:** 2024-06-07

### ✅ Olarm
- **Assignee:** Caren Bailey
- **Due:** 2024-05-16
- **Notes:** House Desvaux 
Yazbek 
Strydom 
House Wach

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-05-13

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-05-13

### ✅ Close open recons. Plan recon p day
- **Assignee:** Caleb Thetard
- **Due:** 2024-06-08

### ✅ Tech Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Caleb Fuel
- **Assignee:** Caren Bailey
- **Due:** 2024-05-13

### ✅ Refund R2k from personal
- **Assignee:** Amanda
- **Due:** 2024-05-13

### ✅ Keep calendar populated
- **Assignee:** Caleb Thetard
- **Due:** 2024-05-08

### ✅ Drop Lutron Relay at office
- **Assignee:** Caleb Thetard
- **Due:** 2024-05-02

### ✅ Contact VJ
- **Assignee:** Darren Swanepoel
- **Due:** 2024-05-10

### ✅ Homemation Demo
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-29

### ✅ Takealot voucher Imti
- **Assignee:** Amanda
- **Due:** 2024-04-29
- **Notes:** We owe Imti a voucher for his 1 year at D-One. Please send Imti a R1000 voucher from Takealot.

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-25

### ✅ Booked out stock
- **Assignee:** Unassigned
- **Due:** 2024-04-25

### ✅ Darren’s tech meeting notes
- **Assignee:** Stafford
- **Due:** 2024-04-25

### ✅ Give Darren his vehicle license
- **Assignee:** Stafford
- **Due:** 2024-04-26

### ✅ Bluebolt Login Details
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Username Email: darren@d-one.co.za
Password: Done2580

### ✅ Tech meeeting
- **Assignee:** Tristan Capes
- **Due:** 2024-04-22

### ✅ Dahua form
- **Assignee:** Darren Swanepoel
- **Due:** 2024-05-10

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-22

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-04-22

### ✅ BUILDERS EQUIPMENT PURCHASE
- **Assignee:** Unassigned
- **Due:** 2024-04-12

### ✅ Afrihost VS Clients Invoices
- **Assignee:** Caren Bailey
- **Due:** 2024-05-02
- **Notes:** Its seems as Afrihost Billing Increase however Client billing still the same.

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-04-18

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-04-22

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-18

### ✅ Darren’s meeting notes
- **Assignee:** Stafford
- **Due:** 2024-04-18

### ✅ Pick up Mekyle
- **Assignee:** Tristan Capes
- **Due:** 2024-04-15

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-04-15

### ✅ Delivery and collections
- **Assignee:** Stafford
- **Due:** 2024-04-15

### ✅ Admin
- **Assignee:** Stafford
- **Due:** 2024-04-12

### ✅ Clarify rates in Xero
- **Assignee:** Amanda
- **Due:** 2024-04-17
- **Notes:** Guys can we please clarify our rates.

After hour rates
Labour per hour 
Programming 
Travel if any

### ✅ Personal
- **Assignee:** Stafford
- **Due:** 2024-04-15

### ✅ Register to vote
- **Assignee:** Darren Swanepoel
- **Due:** 2024-05-06

### ✅ Clinic appointment
- **Assignee:** Tristan Capes
- **Due:** 2024-04-12

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-15

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-04-15

### ✅ Refund Invoice INV-4805  D-One Electronics cc for PF Family Trust-  Friedmann
- **Assignee:** Stafford
- **Due:** 2024-04-17
- **Notes:** Regrettably, the firmware update that you charged me for has not rectified the problem.

### ✅ B Farrar and M Mitchell C/O Soukop Property Group
- **Assignee:** Amanda
- **Due:** 2024-04-16
- **Notes:** There is overpayments for this account loaded however no Credit payment for R2070.00.

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-04-11

### ✅ Tech meeting (Darren’s notes)
- **Assignee:** Darren Swanepoel
- **Due:** 2024-04-11

### ✅ Regal/Miro/sensor/pienaar bros/Space tv
- **Assignee:** Unassigned
- **Due:** 2024-04-09

### ✅ office/cfs/builders
- **Assignee:** Unassigned
- **Due:** 2024-04-08

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-04-08

### ✅ Get Shutter plywood from hardware
- **Assignee:** Tristan Capes
- **Due:** 2024-04-08

### ✅ Replace caddy wipers
- **Assignee:** Tristan Capes
- **Due:** 2024-04-08

### ✅ Meet Stafford collect drill and Jigsaw
- **Assignee:** Tristan Capes
- **Due:** 2024-04-08

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-08

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-04-08

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-04-08

### ✅ Confirm payment plan with Somm and village deli
- **Assignee:** Caren Bailey
- **Due:** 2024-04-05
- **Notes:** Contacted Johann as we have arranged 2 part payment starting :
11 April 2024  R16203.51
9 May 2024     R16203.52

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-04-11

### ✅ Get gabcon
- **Assignee:** Tristan Capes
- **Due:** 2024-04-04

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-04-04

### ✅ LEAVE
- **Assignee:** Unassigned
- **Due:** 2024-04-02

### ✅ Accounts meeting
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-08

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-04-04

### ✅ Get host and TOA speaker from the office
- **Assignee:** Tristan Capes
- **Due:** 2024-04-03

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-04

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-04-04

### ✅ Clean Up Wiring in Office
- **Assignee:** Tristan Capes
- **Due:** 2024-09-03
- **Notes:** Hi Tristan

Please could you or Mekyle assist with the Wiring in the office as discussed.

### ✅ VW Polo Service 18th April 7.30 in Paarl
- **Assignee:** Unassigned
- **Due:** 2024-04-18
- **Notes:** Car Service booked. No payment is due as the vehicle still has a Maintanene plan.

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-04-02

### ✅ Tech Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-02

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-04-02

### ✅ Office Check for Furman and S12 Host
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-28

### ✅ update asana
- **Assignee:** Tristan Capes
- **Due:** 2024-03-28

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-28

### ✅ Check retentions Barbara, Matos etc.
- **Assignee:** Darren Swanepoel
- **Due:** 2024-04-15

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-03-28

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-28

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-28

### ✅ 977 Val De Vie
- **Assignee:** Caren Bailey
- **Due:** 2024-04-02

### ✅ Buy yoga credit
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-28

### ✅ Leave day
- **Assignee:** Amanda
- **Due:** 2024-03-27

### ✅ Get supplies from Linkqage
- **Assignee:** Tristan Capes
- **Due:** 2024-03-26

### ✅ Searching for Host and AVB switch
- **Assignee:** Tristan Capes
- **Due:** 2024-03-26

### ✅ Collect 1 to 1 HD anywhere splitter
- **Assignee:** Tristan Capes
- **Due:** 2024-03-26

### ✅ Check if we’re due a MacBook for ordering R500k with Planetworld
- **Assignee:** Caleb Thetard
- **Due:** 2024-04-26

### ✅ Savant Meeting at Planetworld
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-26

### ✅ Buy batteries for labelling machine
- **Assignee:** Tristan Capes
- **Due:** 2024-03-26

### ✅ office stock collect
- **Assignee:** Unassigned
- **Due:** 2024-03-25

### ✅ Staff catch up meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-03-25

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-03-25

### ✅ Find out if we are registered for PSIRA and get our PSIRA number
- **Assignee:** Caren Bailey
- **Due:** 2024-03-28
- **Notes:** I registered for PSIRA in 2019 and did the exam in October Nov 2019.

### ✅ Leave day
- **Assignee:** Amanda
- **Due:** 2024-03-26
- **Notes:** I need to sort out warrants on my name Cape civic center road show etc 26th March

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-25

### ✅ PC for Mekyle
- **Assignee:** Darren Swanepoel
- **Due:** 2024-04-19

### ✅ Change Melissa to Caren on gmail etc
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-25

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-25

### ✅ America support let us know what you do
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-28

### ✅ Renew vehicle license
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-27

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-03-25

### ✅ Savant meeting and tour
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-23

### ✅ savant training
- **Assignee:** Unassigned
- **Due:** 2024-03-12

### ✅ Collect 8 port switch at the office
- **Assignee:** Tristan Capes
- **Due:** 2024-03-20

### ✅ Drop off bubble wrap at Darrens house
- **Assignee:** Tristan Capes
- **Due:** 2024-03-20

### ✅ Planetworld Invoice and Goods Delivered
- **Assignee:** Unassigned
- **Due:** 2024-03-26
- **Notes:** Please confirm if this is for us , Planetworld invoice 260026115 PO-01156? We received this stock today, R62 236.60

### ✅ [Duplicate] PlanetWorld order - Not Sure for Which Project
- **Assignee:** Unassigned
- **Due:** 2024-03-26
- **Notes:** Planet World Invoice 260026115 PO-01156 Total R62 236.60

### ✅ Stuck in traffic due to accident
- **Assignee:** Tristan Capes
- **Due:** 2024-03-19

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-03-18

### ✅ Staff meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-18

### ✅ Staff catchup
- **Assignee:** Unassigned
- **Due:** 2024-03-18

### ✅ Please give me total invoices for the projects listed in the Main project
- **Assignee:** Unassigned
- **Due:** 2024-03-21

### ✅ Virtual Staff Meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-18

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-18

### ✅ Staff meeting
- **Assignee:** Stafford
- **Due:** 2024-03-18

### ✅ Staff Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-03-18

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-03-18

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-03-18

### ✅ Dahua training
- **Assignee:** Stafford
- **Due:** 2024-07-26

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-18

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-18

### ✅ oakvale stock deliver
- **Assignee:** Unassigned
- **Due:** 2024-02-20

### ✅ OFFICE OAKVALE STOCK COLLECT
- **Assignee:** Unassigned
- **Due:** 2024-02-20

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-15

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-19

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-22

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-26

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-29

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-04

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-07

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-11

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-14

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-18

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-25

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-04-03

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-04-08

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-04-04

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-04-08

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-04-23

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-04-25

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-04-25

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-05-05

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-05-21

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-06-06

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-06-03

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-06-10

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-06-18

### ✅ Leave Request
- **Assignee:** Caren Bailey
- **Due:** 2024-03-18
- **Notes:** Dates : 
28 March 2024
2nd April 2024

### ✅ Asana catchup
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-16

### ✅ Pin Point Inv 6639
- **Assignee:** Caren Bailey
- **Due:** 2024-03-27
- **Notes:** Please approve as per 5th progress payment for Oakvale. Invoice 6639 payment amount R31,394.92 Due End March 24.

### ✅ Swop push button at Regal
- **Assignee:** Tristan Capes
- **Due:** 2024-03-15

### ✅ Get Legrand cover plate from RG Jack and Sons
- **Assignee:** Tristan Capes
- **Due:** 2024-03-15

### ✅ Get Legrand cover at Jack hammers
- **Assignee:** Tristan Capes
- **Due:** 2024-03-15

### ✅ Arrange collection for the outdoor Unit at Regal. You will need to make payment with your card upon collection.
- **Assignee:** Tristan Capes
- **Due:** 2024-03-15

### ✅ Collect PC board for Ekbergh
- **Assignee:** Tristan Capes
- **Due:** 2024-03-15

### ✅ Stafford catchup
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-15

### ✅ Asana/time logging/ emails
- **Assignee:** Stafford
- **Due:** 2024-03-14

### ✅ Drop off speakers at uppink
- **Assignee:** Tristan Capes
- **Due:** 2024-03-14

### ✅ Drop off stock at Oakvale
- **Assignee:** Tristan Capes
- **Due:** 2024-03-14

### ✅ Tech meeting/Office
- **Assignee:** Tristan Capes
- **Due:** 2024-03-14

### ✅ Create savant profiles
- **Assignee:** Unassigned
- **Due:** 2024-04-05

### ✅ Update Supplier Contacts
- **Assignee:** Caren Bailey
- **Due:** 2024-03-18

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-14

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-14

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-03-14

### ✅ Cape Cables & Space TV
- **Assignee:** Unassigned
- **Due:** 2024-02-12

### ✅ Tech meet
- **Assignee:** Unassigned
- **Due:** 2024-02-12

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-08

### ✅ Prepare accounts receivable for Monday meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-18

### ✅ savant training
- **Assignee:** Unassigned
- **Due:** 2024-03-13

### ✅ Get patch leads from Linkqage
- **Assignee:** Tristan Capes
- **Due:** 2024-03-13

### ✅ Admin
- **Assignee:** Stafford
- **Due:** 2024-03-12

### ✅ You haven't logged time for Pick n Pay, it's on your calendar but not in a task
- **Assignee:** Stafford
- **Due:** 2024-03-11

### ✅ Team admin
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-12

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-14

### ✅ Collect speakers at office
- **Assignee:** Tristan Capes
- **Due:** 2024-03-12

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-03-11

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-03-11

### ✅ Fit on Jeans and Tracktop at PnP Clothing Tokai and Get Spraypaint at Builders
- **Assignee:** Unassigned
- **Due:** 2024-03-11

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-11

### ✅ Pick and pay clothing for the team gear
- **Assignee:** Stafford
- **Due:** 2024-03-11

### ✅ Farbers or grahams
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-11

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-11

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-03-07

### ✅ Daily check in questions
- **Assignee:** Caren Bailey
- **Due:** 2024-03-20
- **Notes:** Create a saved search for the teams and their completed tasks, as well as their time logged for the day. The rate is R150 per hour.

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-03-11

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts Meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-11

### ✅ Coordinating-asana cleanups
- **Assignee:** Stafford
- **Due:** 2024-03-05

### ✅ Tell Cartrack that the app is not working. No cars visible
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-11

### ✅ Drop off stock at Oakvale
- **Assignee:** Tristan Capes
- **Due:** 2024-03-07

### ✅ Collect speakers for Uppink
- **Assignee:** Tristan Capes
- **Due:** 2024-03-07

### ✅ Energy Master Builders _ Documents
- **Assignee:** Unassigned
- **Due:** 2024-03-08
- **Notes:** Please be so kind to send through the documentation as requested

### ✅ J080356 - AFS - MC 2024 Vehicles TAx
- **Assignee:** Caren Bailey
- **Due:** 2024-04-01
- **Notes:** You assisted me with the finance invoices for all the vehicles for the 2023 period, please could I ask for the 2024?

### ✅ Talk to Mel about the team admin role
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-11

### ✅ Kevin email price lock planet world
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-11

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-07

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-07

### ✅ Tech Meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-07

### ✅ General Stock with Darren
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-06

### ✅ Strategy Session with Darren
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-06

### ✅ Berkley 14 and 54 Fresnaye Ave Site Visit
- **Assignee:** Caleb Thetard
- **Due:** 2024-03-06

### ✅ Project calls
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-06

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2024-02-26

### ✅ Installation of Car Mirror at Alpha Bodyworks
- **Assignee:** Unassigned
- **Due:** 2024-02-23

### ✅ Car Tracker Installed
- **Assignee:** Unassigned
- **Due:** 2024-02-21

### ✅ Confirm what we paid for this
- **Assignee:** Caren Bailey
- **Due:** 2024-03-07
- **Notes:** ECHO LOW VOLTAGE PADDLE KEYPAD (SNOW WHITE). Kevin gave it to us. I just want to make sure we didn't pay for it.

### ✅ Office coordinating team
- **Assignee:** Stafford
- **Due:** 2024-03-04

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-03-04

### ✅ Collect camera poles at Triwes
- **Assignee:** Tristan Capes
- **Due:** 2024-03-04

### ✅ Collect Speakers at the Office
- **Assignee:** Tristan Capes
- **Due:** 2024-03-04

### ✅ General Stock
- **Assignee:** Caren Bailey
- **Due:** 2024-03-05
- **Notes:** Please delete all stock in general before we import the new PO of stock.

### ✅ Admin
- **Assignee:** Stafford
- **Due:** 2024-03-01

### ✅ Moved 2x DCTXP2 Paradox and 1x VXI-R From General to Wach
- **Assignee:** Caren Bailey
- **Due:** 2024-03-08
- **Notes:** Please update accordingly

### ✅ SOH End FEB
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-08
- **Notes:** Can you go over this list and confirm what still can be sold onto clients and what should be written off.

### ✅ Admin
- **Assignee:** Stafford
- **Due:** 2024-02-28

### ✅ General Stock Values and organising
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-28

### ✅ House Kevin James
- **Assignee:** Unassigned
- **Due:** 2024-03-01
- **Notes:** Please call Mrs. James regarding the Guest Lounge - Tv no screen. Intercom Cannot hear and needs this reprogrammed.

### ✅ Office collection
- **Assignee:** Stafford
- **Due:** 2024-02-27

### ✅ Off load stock at Office
- **Assignee:** Tristan Capes
- **Due:** 2024-02-27

### ✅ Purchase cable at CFS
- **Assignee:** Tristan Capes
- **Due:** 2024-02-26

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-02-26

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-02-26

### ✅ Tech Meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Submit fuel log
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-26

### ✅ Collect speakers for Strydom
- **Assignee:** Tristan Capes
- **Due:** 2024-02-23

### ✅ Let Marc know how many Dahua screens we have.
- **Assignee:** Caren Bailey
- **Due:** 2024-02-26

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-02-22

### ✅ Collect Stock for Clyde
- **Assignee:** Tristan Capes
- **Due:** 2024-02-22

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-22

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-22

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-22

### ✅ Collect Caddy
- **Assignee:** Tristan Capes
- **Due:** 2024-02-21

### ✅ Pin Point Invoice 6840 and 6639 4th Draw
- **Assignee:** Unassigned
- **Due:** 2024-03-05
- **Notes:** Service Call out and repairs and 4th Draw for Oakvale. Total =R2,736.31. Progress Draw 4th - Oakvale R50 000.00 (vat included)

### ✅ Asana cleanups/emails-general
- **Assignee:** Stafford
- **Due:** 2024-02-19

### ✅ Collect Cable for Clyde at Top CCTV
- **Assignee:** Tristan Capes
- **Due:** 2024-02-15

### ✅ Collect Ripcord at Cape Cables
- **Assignee:** Tristan Capes
- **Due:** 2024-02-15

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-02-15

### ✅ Collect cabcon for Clyde at CFS
- **Assignee:** Tristan Capes
- **Due:** 2024-02-16

### ✅ Collect remaining cables at Cape Cables
- **Assignee:** Tristan Capes
- **Due:** 2024-02-16

### ✅ Re-enroll my fingerprint at VDV
- **Assignee:** Tristan Capes
- **Due:** 2024-02-19

### ✅ Pick up Mekyle
- **Assignee:** Tristan Capes
- **Due:** 2024-02-19

### ✅ Tech Meeting/Office
- **Assignee:** Tristan Capes
- **Due:** 2024-02-19

### ✅ Upskill plan
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-08

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-02-19

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-19

### ✅ Day plan
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-19

### ✅ Recon Logging Monthly Time Feb - March 24
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Confirm that Jetbuilt has latest pricelists
- **Assignee:** Caren Bailey
- **Due:** 2024-06-24
- **Notes:** Planetworld pricing is from November. Is that the latest from them? Scoop Pricelist is from today

### ✅ Log time for yesterday
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-16

### ✅ Cancel Ctrack SA 02514152
- **Assignee:** Unassigned
- **Due:** 2024-03-01
- **Notes:** We hereby would like to Cancel our Ctrack Account with you until the End of this Month.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-19

### ✅ Get the pro audio download. And fill me in afterwards
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-14
- **Notes:** It's going to be too much for me to try and fit in the pro audio demo tomorrow.

### ✅ Tax return
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-13

### ✅ Asana and planning
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-13

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-02-08

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-02-05

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-12

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-02-12

### ✅ Pickup IR Learner Planetworld
- **Assignee:** Caleb Thetard
- **Due:** 2024-05-08
- **Notes:** The one linked in the email to Mo from Planetworld

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-12
- **Notes:** Get digital copy of safety file. Marwyk German TV. Vrymansfontein additions. Wach additions. Vigne D'Or Camera and Network. Zwaanswyk replacement quote 48 port switch TBC.

### ✅ Update Scoop and Aruba Pricing in Jetbuilt
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-09

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-02-12

### ✅ Accounts Meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-12

### ✅ Medicals
- **Assignee:** Tristan Capes
- **Due:** 2024-01-31

### ✅ Asana sweeping
- **Assignee:** Stafford
- **Due:** 2024-02-08

### ✅ Hayley Residence callout
- **Assignee:** Stafford
- **Due:** 2024-02-08

### ✅ Morning Meetings
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-08

### ✅ Accounts meeting and Snapshot
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-08

### ✅ Tech Meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-08

### ✅ Chat to Frik regarding multiple safety files/digital copy
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-12

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-02-08

### ✅ Admin
- **Assignee:** Stafford
- **Due:** 2024-02-07

### ✅ Time off
- **Assignee:** Stafford
- **Due:** 2024-02-06

### ✅ See if we can move our Planetworld visit to Thursday after the audio demo
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-09

### ✅ Tax forms to Dominique
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-13

### ✅ Planetworld Oakvale tour and lunch
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-05

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-05

### ✅ office collect cable
- **Assignee:** Unassigned
- **Due:** 2024-02-05

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-05

### ✅ Morning meeting
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-05

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-05

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-02-05

### ✅ medisafe
- **Assignee:** Unassigned
- **Due:** 2024-01-31

### ✅ Access denied at VDV
- **Assignee:** Tristan Capes
- **Due:** 2024-02-02

### ✅ Collect rack at office
- **Assignee:** Tristan Capes
- **Due:** 2024-02-02

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-02-01

### ✅ Urgently re-enroll Tristan for VDV access
- **Assignee:** Caren Bailey
- **Due:** 2024-02-07

### ✅ Get Quote and Book Mirror Repair at Alpha Bodywork’s
- **Assignee:** Unassigned
- **Due:** 2024-02-07

### ✅ RA2 pricelist to Kevin
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-02

### ✅ Morning Meetings
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-01

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-01

### ✅ Coordinating projects
- **Assignee:** Stafford
- **Due:** 2024-02-01

### ✅ Paradox stock sold-see invoice
- **Assignee:** Amanda
- **Due:** 2025-02-26

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2024-02-01

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-02-01

### ✅ Collect cables at CFS
- **Assignee:** Tristan Capes
- **Due:** 2024-01-29

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2024-01-29

### ✅ Get patch leads from Linkqage
- **Assignee:** Tristan Capes
- **Due:** 2024-01-30

### ✅ Pick up Mekyle at the Office
- **Assignee:** Tristan Capes
- **Due:** 2024-01-30

### ✅ Admin
- **Assignee:** Stafford
- **Due:** 2024-01-31

### ✅ Medicals
- **Assignee:** Stafford
- **Due:** 2024-01-31

### ✅ Please arrange to go for your medicals At Medisafe
- **Assignee:** Unassigned
- **Due:** 2024-01-31

### ✅ Camera issue 9 Hugo road, hout bay
- **Assignee:** Stafford
- **Due:** 2024-03-01
- **Notes:** Schedule with Kim

### ✅ Please call Jacques Osborn property holdings
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-30

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-01-29

### ✅ Paradox alarm equipment
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-30

### ✅ Alarm Settings
- **Assignee:** Unassigned
- **Due:** None

### ✅ Created Tasks in Documentation Section of Projects
- **Assignee:** Unassigned
- **Due:** 2024-01-29

### ✅ Create documentation section in all projects in asana using the sections in google docs
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-29

### ✅ General planning/Asana sweeping
- **Assignee:** Stafford
- **Due:** 2024-01-30

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-01-29

### ✅ Merge tasks imti. Which is master?
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Ask Planetworld via email for IR Learner
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-29

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-01-29

### ✅ office meet tristan
- **Assignee:** Unassigned
- **Due:** 2024-01-26

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-29
- **Notes:** Tech+Accounts+Darren Svelte Design Meetings

### ✅ Service search for Stafford to monitor
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-29

### ✅ Pick up Mekyle at the Office
- **Assignee:** Tristan Capes
- **Due:** 2024-01-25

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-29

### ✅ Update Clyde's rights on Asana he is limited to guest
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-26

### ✅ Please pay Eddie 15th-24th (8 days)
- **Assignee:** Amanda
- **Due:** 2024-01-25

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-25

### ✅ homemation
- **Assignee:** Unassigned
- **Due:** 2024-01-24
- **Notes:** book in desvaux blown dimmer + Ehkberg screen pdu

### ✅ Stop for fuel
- **Assignee:** Tristan Capes
- **Due:** 2024-01-24

### ✅ Assist ladies with rearranging desks at the office
- **Assignee:** Tristan Capes
- **Due:** 2024-01-24

### ✅ Collect cameras at the Office
- **Assignee:** Tristan Capes
- **Due:** 2024-01-24

### ✅ [Duplicate] Cartrack
- **Assignee:** Unassigned
- **Due:** 2024-01-26
- **Notes:** Get Cartrack to fix Imti's tracker with no call-out fee.

### ✅ Meeting with Melissa about Service Call
- **Assignee:** Unassigned
- **Due:** 2024-01-24
- **Notes:** Develop procedure for service calls. Review current calls. Discuss Boulders call-out.

### ✅ LInkqage.
- **Assignee:** Tristan Capes
- **Due:** 2024-01-23

### ✅ Collect Strydom equipment from office
- **Assignee:** Tristan Capes
- **Due:** 2024-01-23

### ✅ Linkqage cabcon purchase
- **Assignee:** Unassigned
- **Due:** 2024-01-23

### ✅ Asana cleanups
- **Assignee:** Stafford
- **Due:** 2024-01-23

### ✅ Test 2
- **Assignee:** Stafford
- **Due:** 2024-01-17

### ✅ Asanas training with Darren
- **Assignee:** Stafford
- **Due:** 2024-01-22

### ✅ Asana planning - team tasks
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-23

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-01-22

### ✅ Review bank statement for D1
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-01

### ✅ Review bank statement for D1
- **Assignee:** Darren Swanepoel
- **Due:** 2024-02-05

### ✅ Review bank statement for D1
- **Assignee:** Darren Swanepoel
- **Due:** 2024-03-11

### ✅ Review bank statement for D1
- **Assignee:** Darren Swanepoel
- **Due:** 2024-04-05

### ✅ Review bank statement for D1
- **Assignee:** Darren Swanepoel
- **Due:** 2024-05-05

### ✅ Review bank statement for D1
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ AV consultant required for Llandudno new build
- **Assignee:** Stafford
- **Due:** None
- **Notes:** Finished FDC with SAOTA on new house at 13 Steensway, looking at appointing consultants in preparation for IDD.

### ✅ Week 15-19 Jan
- **Assignee:** Tristan Capes
- **Due:** 2024-01-22

### ✅ Collect battery from office
- **Assignee:** Tristan Capes
- **Due:** 2024-01-22

### ✅ Emails and Asana
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-22

### ✅ Asana training Stafford
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-22

### ✅ Savant Online Training
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-22

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-22

### ✅ Asana Time Tracking
- **Assignee:** Amanda
- **Due:** 2024-01-24

### ✅ Consolidate file sharing to G:/
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-22

### ✅ Thursday agenda
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-25

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-22

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2024-01-22

### ✅ Drop off Polo
- **Assignee:** Stafford
- **Due:** 2024-01-19

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2024-01-22

### ✅ 
- **Assignee:** Unassigned
- **Due:** None

### ✅ Test 2 Mekyle
- **Assignee:** Unassigned
- **Due:** 2024-01-17

### ✅ Update your Asana profile from Admin to "Fuel Filter"
- **Assignee:** Unassigned
- **Due:** 2024-01-26

### ✅ General meeting/planning
- **Assignee:** Stafford
- **Due:** 2024-01-25

### ✅ Update your Asana profile from "Admin" to "Fuel Filter"
- **Assignee:** Caren Bailey
- **Due:** 2024-01-26

### ✅ Update your Asana profile role to: Dashboard
- **Assignee:** Amanda
- **Due:** 2024-01-25

### ✅ Update your Asana profile to "Wheels"
- **Assignee:** Tristan Capes
- **Due:** 2024-01-22

### ✅ Update your Asana profile role to "Onboard Computer"
- **Assignee:** Unassigned
- **Due:** 2024-01-23

### ✅ Update your Asana profile from "Engineer for System Integration" to "GPS"
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-26

### ✅ Update your Asana profile from "Team leader for technical" to Gearbox
- **Assignee:** Stafford
- **Due:** 2024-01-26

### ✅ Train Stafford, Caleb and Tristan on OVRC site management and rebooting
- **Assignee:** Unassigned
- **Due:** 2024-04-05

### ✅ Dalhua training
- **Assignee:** Tristan Capes
- **Due:** 2024-01-18

### ✅ Request refund for JEtbuilt billing for Tristan, who never registered the invite
- **Assignee:** Caren Bailey
- **Due:** 2024-01-26

### ✅ Test Darren Asana training
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-18

### ✅ Test Amanda Asana traning
- **Assignee:** Amanda
- **Due:** None

### ✅ test mekyle Asana training
- **Assignee:** Unassigned
- **Due:** 2024-01-18

### ✅ Test Tristan - Asana Training
- **Assignee:** Tristan Capes
- **Due:** 2024-01-18

### ✅ Asana Training
- **Assignee:** Unassigned
- **Due:** 2024-01-18

### ✅ Asana Training
- **Assignee:** Caren Bailey
- **Due:** 2024-01-18

### ✅ Test Stafford Asana training
- **Assignee:** Stafford
- **Due:** 2024-01-18

### ✅ Test task
- **Assignee:** Unassigned
- **Due:** None

### ✅ Test Caleb Asana Training
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-18

### ✅ Asana Training Imti
- **Assignee:** Unassigned
- **Due:** 2024-01-18

### ✅ Medical Aid
- **Assignee:** Caleb Thetard
- **Due:** None
- **Notes:** Has all been sorted with your medical aid?

### ✅ Emails and asana time logging
- **Assignee:** Stafford
- **Due:** 2024-01-17

### ✅ virtual team meeting
- **Assignee:** Unassigned
- **Due:** 2024-01-15

### ✅ office +Homemation stock collect
- **Assignee:** Unassigned
- **Due:** 2024-01-16

### ✅ spectrum collect mem card for 401 boulders
- **Assignee:** Unassigned
- **Due:** 2024-01-16

### ✅ Cartracker
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Only Caddy and VW Polo have trackers currently. Follow-up on renewal/change-of-ownership for other vehicles.

### ✅ Tech files into Asana
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-31
- **Notes:** Tech files live in Asana via G docs. Consider doing same with designs like line drawings and rack designs for current projects.

### ✅ Managing Asana
- **Assignee:** Stafford
- **Due:** 2024-01-16

### ✅ Make Caleb Project Admin for the following Projects to edit Project Overviews
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-16

### ✅ Virtual team meeting
- **Assignee:** Stafford
- **Due:** 2024-01-15

### ✅ Recon Logging Monthly Time
- **Assignee:** Unassigned
- **Due:** None

### ✅ Refine Jetbuilt subscription
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-17
- **Notes:** Being charged for a service module that's not active/in use. Ask Jetbuilt to correct the billing.

### ✅ Please complete the attached registration and send it to them
- **Assignee:** Caren Bailey
- **Due:** 2024-01-26

### ✅ Setup Asana  Wiki WhatsApp from Mands
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-18

### ✅ Book the Polo for service tomorrow
- **Assignee:** Unassigned
- **Due:** 2024-01-19

### ✅ Update asana projects
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-16

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ DASHBOARD update
- **Assignee:** Amanda
- **Due:** 2024-02-07
- **Notes:** Setup Asana Dashboard for financial and project info: bank balance, income, opex, net profit line graphs; project percentage bars; task/time tracking per person.

### ✅ Re leave days. Only Imti worked 21 Dec.
- **Assignee:** Unassigned
- **Due:** None

### ✅ Edwin wages
- **Assignee:** Amanda
- **Due:** 2023-12-20

### ✅ Confirm warehouse alarm is re-armed
- **Assignee:** Unassigned
- **Due:** 2023-12-21

### ✅ Asana Training and welcome session
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-15

### ✅ Find a way to put technical file into asana
- **Assignee:** Caleb Thetard
- **Due:** 2024-01-31

### ✅ Move olarm from Oakvale to Wach
- **Assignee:** Caleb Thetard
- **Due:** 2023-12-19

### ✅ Cancel Harvest
- **Assignee:** Unassigned
- **Due:** 2023-12-18
- **Notes:** Emailed all data off Harvest. When it arrives add it to this task to cancel the subscription ASAP.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Give Amanda the keys for Maitland
- **Assignee:** Darren Swanepoel
- **Due:** 2023-12-16

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Send me your leave dates for Dec
- **Assignee:** Unassigned
- **Due:** None

### ✅ Mekyle leave 14 Dec
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Send Caleb Contact for discovery insurance
- **Assignee:** Amanda
- **Due:** 2023-12-12
### ✅ Add Caleb to provident fund for 2024
- **Assignee:** Amanda
- **Due:** 2024-02-29

### ✅ Caleb Leave 14 December
- **Assignee:** Caren Bailey
- **Due:** 2023-12-14

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-12-11

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-12-07

### ✅ Review Jetbuiot project statuses and change orders are up to date
- **Assignee:** Caleb Thetard
- **Due:** None

### ✅ [Converted to template] Payment
- **Assignee:** Amanda
- **Due:** 2023-12-07
- **Notes:** When needing to ask for payment please add the below tasks.

Please make sure the sure date states when the payment needs to be made.

Please send a whatsapp for immediate/urgent payments.

### ✅ Duplicate of Payment
- **Assignee:** Amanda
- **Due:** None
- **Notes:** When needing to ask for payment please add the below tasks

### ✅ Documentation
- **Assignee:** Unassigned
- **Due:** 2024-01-31
- **Notes:** Desvaux 
Ekbergh
Barbara
James
Fulham

Lighting Channel legend for DB.

IP addresses from routers.

Login credentials.
Hikvision
Lutron

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-12-04

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2024-02-19

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-12-04

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-11-30

### ✅ meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-30

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Travel billing
- **Assignee:** Darren Swanepoel
- **Due:** 2024-04-11

### ✅ Holiday contacts
- **Assignee:** Darren Swanepoel
- **Due:** 2023-12-01

### ✅ Aruba Instant On Registration
- **Assignee:** Unassigned
- **Due:** 2023-11-29
- **Notes:** https://partner.hpe.com/web/prp/registration

Logins:
darren@d-one.co.za
Darren@D1

### ✅ Test audio
- **Assignee:** Stafford
- **Due:** 2023-11-28

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-11-16

### ✅ D1 virtual Office Catch up
- **Assignee:** Unassigned
- **Due:** 2023-11-21

### ✅ D-One Staff Function
- **Assignee:** Unassigned
- **Due:** 2023-11-24

### ✅ Admin
- **Assignee:** Unassigned
- **Due:** 2023-11-24

### ✅ Make 10 more D1 caps
- **Assignee:** Amanda
- **Due:** 2023-12-01

### ✅ Debtors ReView
- **Assignee:** Caren Bailey
- **Due:** 2023-11-30
- **Notes:** Feedback on all outstanding money

### ✅ Debtors ReView
- **Assignee:** Caren Bailey
- **Due:** 2024-03-18
- **Notes:** Feedback on all outstanding money

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-27

### ✅ Edwin
- **Assignee:** Amanda
- **Due:** 2023-11-24

### ✅ Send TCL Business Details as per email
- **Assignee:** Unassigned
- **Due:** 2023-11-30
- **Notes:** Have sent you an email. We want to create an account with them and potentially sell their TVs

### ✅ Asana, Planning, Admin
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Admin Check in
- **Assignee:** Unassigned
- **Due:** 2023-11-29

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-11-23

### ✅ Harvest logging
- **Assignee:** Unassigned
- **Due:** 2023-11-30
- **Notes:** For Mekyle, Stafford, Imti and Tristan.
Check when they stopped logging in Harvest (Use Mel's login)
Go back in their calendars and just log the time that they spent on which projects as per their calendars.
Stafford: Installation
Imti: Programming
Tristan: Installation
Mekyle: Installation

Log their tech meetings as project management.

### ✅ Do HP Aruba Partner registration
- **Assignee:** Unassigned
- **Due:** 2023-11-30
- **Notes:** https://partner.hpe.com/web/prp/registration

### ✅ ADMIIN CATCH UP
- **Assignee:** Unassigned
- **Due:** 2023-11-22

### ✅ [Converted to template] Ovetime Template
- **Assignee:** Amanda
- **Due:** None
- **Notes:** Please make sure you override the word "Template" to the actual month the time was recorded.

The period for a month is 21st to 20th of the next month (EG 21 Jan- 20th Feb). This give me a few days to prepare payrol. Anything not loaded in time may be claimed but in the following month.

Please create a subtask per day for overtime. See below

### ✅ 2.5 Hours
- **Assignee:** Amanda
- **Due:** 2023-11-22
- **Notes:** Brief description of what was done on that day.

### ✅ Tristan: Overtime
- **Assignee:** Amanda
- **Due:** 2023-11-21

### ✅ Test time
- **Assignee:** Amanda
- **Due:** 2023-11-21

### ✅ Mekyle off sick please book him off
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2023-11-20

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** 2023-11-29

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-20

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2023-11-20

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-11-20

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Asana trial ending today
- **Assignee:** Amanda
- **Due:** 2023-11-17

### ✅ Meetings
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-16

### ✅ Fines
- **Assignee:** Amanda
- **Due:** 2024-01-26
- **Notes:** Confirm who these other license plates are. And allocate fines accordinlgy. Have you paid these?

### ✅ D1 Virtual Office Catch up
- **Assignee:** Unassigned
- **Due:** 2023-11-15

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ⬜ Rack labeling training for team
- **Assignee:** Caleb Thetard
- **Due:** None
- **Notes:** Find a training that we can send the team on, to label cables and patches in racks. 3/3 sites I've been to to troubleshoot had no labels and made troubleshooting much harder. We need a strategy for this. We can do the training in 2024.

### ✅ Apartment 1/2 alarm quote
- **Assignee:** Unassigned
- **Due:** 2023-11-14
- **Notes:** Apartment 1: 2 x Hikvision Alarm Remotes, 2 x Hikvision Door Magnet sensors (Main Bedroom, Bedroom 2). Apartment 2: 2 x Remotes, 3 x Hikvision Door Magnet sensors (Dining Kitchen, Bedroom 1, Bedroom 2). Quote needs to be sent to: jaco@nox.capetown

### ✅ Planetworld Demo
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-13

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-13

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-11-13

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-11-09

### ✅ Admin meeting/Sensor Collection
- **Assignee:** Tristan Capes
- **Due:** 2023-11-08

### ✅ D1 Virtual Office Catch up
- **Assignee:** Unassigned
- **Due:** 2023-11-08

### ✅ Drop off Relays at Homemation
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-07

### ✅ Admin meeting
- **Assignee:** Stafford
- **Due:** None

### ✅ Admin/emails
- **Assignee:** Stafford
- **Due:** None

### ✅ Overtime
- **Assignee:** Stafford
- **Due:** None

### ✅ Asana Login
- **Assignee:** Amanda
- **Due:** 2023-11-08
- **Notes:** Username: Integrator@d-one.co.za
Password: Integrator@D1

### ✅ Confirm if you would to use a standing desk. We have a spare.
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-08

### ✅ Caleb returning Lutron Relays we ordered
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Oakvale Delivery note for Caleb he will return 5 relay lutron devices.

### ✅ D1 virtual Office Catch up
- **Assignee:** Unassigned
- **Due:** 2023-11-07

### ✅ D1 virtual Office Catch up
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-07

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-06

### ✅ Mekyle : Overtime
- **Assignee:** Amanda
- **Due:** 2023-11-20

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-11-02

### ✅ Admin meeting/office
- **Assignee:** Tristan Capes
- **Due:** 2023-11-03

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ D1 virtual Office Catch up
- **Assignee:** Unassigned
- **Due:** 2023-11-03

### ✅ Imti: Overtime
- **Assignee:** Amanda
- **Due:** 2023-11-20

### ✅ Criminal record check Edwin.
- **Assignee:** Caren Bailey
- **Due:** 2023-11-09

### ✅ Check out Asana project templates. To see if that's where we should do the Wiki
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-10

### ✅ Tech meeting/Office
- **Assignee:** Tristan Capes
- **Due:** 2023-11-02

### ✅ Drop Barbara stock at the Office
- **Assignee:** Tristan Capes
- **Due:** 2023-11-03

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-02

### ✅ Pin Point Inv 6639- Oakvale Balance
- **Assignee:** Amanda
- **Due:** 2023-11-24
- **Notes:** Please authorize Pint Point Invoice 6639. Progress Draw: First - Oakvale; Second - Oakvale Invoice 6639 R75 000.00 billed, R50 000.00 paid and R25 000.00 remaining to be paid.

### ✅ michaelbond81@outlook.co
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Hi Melissa. Please confirm Fibre Payment for Which Building. michaelbond81@outlook.co R897.00 x 2 amounts

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-11-02

### ✅ Admin Meeting/Pick up Imti
- **Assignee:** Tristan Capes
- **Due:** 2023-11-01

### ✅ Collect smoke detectors from Spectrum
- **Assignee:** Tristan Capes
- **Due:** 2023-10-31

### ✅ Admin Meeting/collect stock for barbara
- **Assignee:** Tristan Capes
- **Due:** 2023-10-31

### ✅ D-One Virtual Meeting
- **Assignee:** Unassigned
- **Due:** 2023-10-31

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-10-30

### ✅ Admin while wait for Tristan
- **Assignee:** Unassigned
- **Due:** 2023-10-27
- **Notes:** 30min

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-10-25

### ✅ Pick up Melyle
- **Assignee:** Tristan Capes
- **Due:** 2023-10-27

### ✅ Return P5 module to general
- **Assignee:** Tristan Capes
- **Due:** 2023-11-02

### ✅ Sort Olarm account - create table like we have for fibre
- **Assignee:** Caren Bailey
- **Due:** 2023-11-06
- **Notes:** We need to keep track of who is paying us for Olarm, who we are paying for. And who is paying directly.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None
### ✅ Accounts meeting
- **Assignee:** Caleb Thetard
- **Due:** 2023-10-30

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-10-30

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-10-30

### ✅ Tech Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-10-30

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-10-26

### ✅ Pick up Stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-10-26

### ✅ Meeting Notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-10-26

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-10-26

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2023-10-26

### ✅ Office/stock
- **Assignee:** Unassigned
- **Due:** 2023-10-24
- **Notes:** -collect & book out stock at office
-sort & pack van
-collect camera at sensor
-HDMI cable at linkqage

### ✅ Linkqage/Office
- **Assignee:** Tristan Capes
- **Due:** 2023-10-24

### ✅ Take Miche to the clinic
- **Assignee:** Tristan Capes
- **Due:** 2023-10-24

### ✅ Fibre billing etc? Debtors
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Office/pick up Stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-10-23

### ✅ TECH MEETING
- **Assignee:** Unassigned
- **Due:** 2023-10-23

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-10-23

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-10-23

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-10-13

### ✅ Balance Caddy wheels
- **Assignee:** Tristan Capes
- **Due:** 2023-10-09

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-10-09

### ✅ Banking details change
- **Assignee:** Amanda
- **Due:** 2023-10-24
- **Notes:** Could this please be changed this month before payroll. Requested last month however salary was paid to old account. New details attached.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ admin
- **Assignee:** Unassigned
- **Due:** 2023-10-20

### ✅ learners exam
- **Assignee:** Unassigned
- **Due:** 2023-10-18

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-10-16
- **Notes:** 1hr

### ✅ Linkqage
- **Assignee:** Tristan Capes
- **Due:** 2023-10-12

### ✅ Tech meeting/Office
- **Assignee:** Tristan Capes
- **Due:** 2023-10-12

### ✅ Pick up Mekyle
- **Assignee:** Tristan Capes
- **Due:** 2023-10-20

### ✅ Move to oakvale then book out to oakvale
- **Assignee:** Unassigned
- **Due:** 2023-10-23
- **Notes:** Item in the pic comes from general, need to move it to Oakvale then book it out, unit handed to pin point on the 20th of October.

### ✅ On site in DVDV
- **Assignee:** Amanda
- **Due:** 2023-10-20

### ✅ Uppink To Site
- **Assignee:** Amanda
- **Due:** 2023-10-23

### ✅ On site VDVD
- **Assignee:** Amanda
- **Due:** 2023-10-20

### ✅ Caren track time
- **Assignee:** Unassigned
- **Due:** 2023-10-24
- **Notes:** Please issue invoice to: RETURNAfrica (Pty) Ltd, Postnet Suite 117, Private Bag X7, Parkview 2122. Vat registration # 4820276600

### ✅ Time tracking
- **Assignee:** Stafford
- **Due:** 2023-10-23
- **Notes:** There are lots of gaps in your time tracking. Please update this ASAP. (weekly hours summary attached)

### ✅ Track Time Asana
- **Assignee:** Caleb Thetard
- **Due:** 2023-10-20

### ✅ (untitled task)
- **Assignee:** Unassigned
- **Due:** None

### ✅ Time tracking
- **Assignee:** Unassigned
- **Due:** 2023-10-23
- **Notes:** There are a few days this month you have not logged in Asana. Please update ASAP. Easier doing it daily than catching up a week's work. (Mekyle weekly hours summary attached)

### ✅ Time tracking
- **Assignee:** Tristan Capes
- **Due:** 2023-10-23
- **Notes:** There are a few days this month you have not logged in Asana. Please update ASAP. (Tristan weekly hours summary attached)

### ✅ Buy concrete bags at bulders warehouse
- **Assignee:** Tristan Capes
- **Due:** 2023-10-16

### ✅ Collect poles for kiosk at Triwes
- **Assignee:** Tristan Capes
- **Due:** 2023-10-16

### ✅ Linkqage
- **Assignee:** Tristan Capes
- **Due:** 2023-10-16

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-10-16

### ✅ Collect RF cable at office
- **Assignee:** Tristan Capes
- **Due:** 2023-10-17

### ✅ office
- **Assignee:** Tristan Capes
- **Due:** 2023-10-18

### ✅ Regal/Office
- **Assignee:** Tristan Capes
- **Due:** 2023-10-19

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-10-19

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-10-19

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-10-19

### ✅ Imti: Overtime
- **Assignee:** Amanda
- **Due:** 2023-10-20

### ✅ Populate calendar
- **Assignee:** Unassigned
- **Due:** 2023-10-17

### ✅ Blue and white T-shirts for Darren and Imti
- **Assignee:** Amanda
- **Due:** 2023-11-10

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-10-16

### ✅ Goals for the week
- **Assignee:** Stafford
- **Due:** 2023-10-16
- **Notes:** In the tech meeting, let's look at what we want to achieve this week - Projects, Service. Helps with direction so we end the week successful, not just busy.

### ✅ Admin (Asana+harvest)
- **Assignee:** Unassigned
- **Due:** 2023-10-12
- **Notes:** 1hr

### ✅ Admin (harvest/Asana)
- **Assignee:** Unassigned
- **Due:** 2023-10-10

### ✅ Catch up harvest
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-10-16

### ✅ Resolve Sound at VDV Cinema
- **Assignee:** Unassigned
- **Due:** 2023-10-12

### ✅ Allocate from general to Ekbergh please on loan
- **Assignee:** Caleb Thetard
- **Due:** 2023-10-12

### ✅ Update projects status in Jetbuilt
- **Assignee:** Caleb Thetard
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-10-12

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Loy-Rental property
- **Assignee:** Caleb Thetard
- **Due:** 2023-10-12

### ✅ Network Training
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-10-09

### ✅ Stocktake
- **Assignee:** Stafford
- **Due:** None

### ✅ homemation
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** boook in faulty relay for yazbek

### ✅ Homemation/Linkage
- **Assignee:** Tristan Capes
- **Due:** 2023-10-06

### ✅ Collect WAP at office
- **Assignee:** Tristan Capes
- **Due:** 2023-10-06

### ✅ Scoop Collection
- **Assignee:** Tristan Capes
- **Due:** 2023-10-06

### ✅ Office stock collection
- **Assignee:** Tristan Capes
- **Due:** 2023-10-04

### ✅ Office/Triwes
- **Assignee:** Tristan Capes
- **Due:** 2023-10-05

### ✅ Tech and Team catchup meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-10-05

### ✅ Returned M&K In walls and vogels bracket to PlanetWorld
- **Assignee:** Unassigned
- **Due:** 2023-10-31

### ✅ Time off
- **Assignee:** Stafford
- **Due:** None

### ✅ Chat to IT Xone
- **Assignee:** Unassigned
- **Due:** 2023-11-03

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ admin timesheets
- **Assignee:** Unassigned
- **Due:** 2023-10-03

### ✅ tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-10-02

### ⬜ Sell LQSE-2DALUNV-D
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** See if Dean will be interested in buying this unit

### ✅ Collect Stock and pick up Stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-10-03

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-10-02

### ✅ Off on leave
- **Assignee:** Tristan Capes
- **Due:** 2023-09-29

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-10-02

### ✅ Office Stock Collection
- **Assignee:** Unassigned
- **Due:** 2023-09-29

### ✅ SnapAV Updated pricelist
- **Assignee:** Caren Bailey
- **Due:** 2023-09-29
- **Notes:** Looking at a product on SnapAV not loaded on jetbuilt. Item code: AN-520-RT. Requested login details or latest pricelist.

### ✅ Confirm if Tristan followed procedure for leave today
- **Assignee:** Caren Bailey
- **Due:** 2023-09-29

### ✅ clouds+vrymans fibre meet with Jaco
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Site walk at clouds and vrymans with jaco checking possible routing, positions, line of sight etc for wireless fibre

### ✅ Pick up imti at Harrigan and drop at Barons
- **Assignee:** Tristan Capes
- **Due:** 2023-09-28

### ✅ Pick up Imti at Barons
- **Assignee:** Tristan Capes
- **Due:** 2023-09-28

### ✅ Drop off cable for Clyde
- **Assignee:** Tristan Capes
- **Due:** 2023-09-28

### ✅ Staff catchup
- **Assignee:** Stafford
- **Due:** None

### ✅ Wheel balancing
- **Assignee:** Stafford
- **Due:** 2023-10-09

### ✅ Tech meeting/office
- **Assignee:** Tristan Capes
- **Due:** 2023-09-28

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-09-28

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-28
### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-09-28

### ✅ office/meet tristan/prepare&plan
- **Assignee:** Unassigned
- **Due:** 2023-09-27

### ✅ travelling/tyre burst
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Caddy had tyre burst on route to site, stopped and changed wheels

### ✅ TECH MEETING
- **Assignee:** Unassigned
- **Due:** None

### ✅ Heritage day(PH)
- **Assignee:** Unassigned
- **Due:** None

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-09-22

### ✅ Public holiday
- **Assignee:** Tristan Capes
- **Due:** 2023-09-25

### ✅ Tech meting/pick up stafford/tire burst on R300
- **Assignee:** Tristan Capes
- **Due:** 2023-09-26

### ✅ Office/pick up mekyle
- **Assignee:** Tristan Capes
- **Due:** 2023-09-27

### ✅ Ruckus Networks Partner Application
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-07
- **Notes:** We need to register for this in order to get access to ruckus dealer pricing for network solutions. https://partners.ruckuswireless.com/apply

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-09-26

### ✅ Assign Mel's current tasks to Caren, so they get done
- **Assignee:** Amanda
- **Due:** 2023-09-26

### ✅ Darren's notes for the week ahead
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Get stock and pack van
- **Assignee:** Tristan Capes
- **Due:** 2023-09-21

### ✅ Tech Meeting/office/pick up stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-09-21

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-09-21
- **Notes:** 1hr

### ✅ Specs for Tristan PC
- **Assignee:** Unassigned
- **Due:** 2023-09-21

### ✅ UPS wattage template
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-29
- **Notes:** Save it in the Templates folder: table with max consumption wattages of Araknis 310 router, UniFi UDM Pro router, UniFi 24 port poe switch, Savant S12 host, Savant Pro host, Marantz Cinema50 AVR, Apple TV, JVC Projector NZ30

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-09-21

### ✅ Office collect stock
- **Assignee:** Tristan Capes
- **Due:** 2023-09-19

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Monitor and SSD
- **Assignee:** Caren Bailey
- **Due:** 2023-09-20
- **Notes:** Do you count the excess monitors and SSD in the general stock? Can't see it anywhere.

### ✅ leave request.
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Pick up stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-09-18

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2023-09-18

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-09-18

### ✅ Pick up Stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-09-15

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-09-14

### ✅ linkkage - vrymansfontein
- **Assignee:** Tristan Capes
- **Due:** 2023-09-14

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2023-09-26

### ✅ Linkqage
- **Assignee:** Unassigned
- **Due:** 2023-09-14
- **Notes:** collect cabcon for vrymans rack

### ✅ office
- **Assignee:** Unassigned
- **Due:** 2023-09-14
- **Notes:** meet tristan, collect stock

### ✅ B Farrar & Mitchell TA/Soukop Invoices
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Please capture outstanding Invoice for Sales Overpayment in order for the account to match.

### ✅ office
- **Assignee:** Tristan Capes
- **Due:** 2023-09-14

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-09-14

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-09-14

### ✅ What do guys need to deliver
- **Assignee:** Stafford
- **Due:** 2023-09-18

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-09-14

### ✅ Tech meeting feedback
- **Assignee:** Stafford
- **Due:** 2023-09-14
- **Notes:** This is a quick check for after the meeting, to check with the team, to see if it was successful.

### ✅ Tech meeting feedback
- **Assignee:** Stafford
- **Due:** 2023-09-21
- **Notes:** This is a quick check for after the meeting, to check with the team, to see if it was successful.

### ✅ Tech meeting feedback
- **Assignee:** Stafford
- **Due:** 2023-09-28
- **Notes:** This is a quick check for after the meeting, to check with the team, to see if it was successful.

### ✅ Tech meeting feedback
- **Assignee:** Stafford
- **Due:** 2023-10-05
- **Notes:** This is a quick check for after the meeting, to check with the team, to see if it was successful.

### ✅ Tech meeting feedback
- **Assignee:** Stafford
- **Due:** 2023-10-12
- **Notes:** This is a quick check for after the meeting, to check with the team, to see if it was successful.

### ✅ Tech meeting feedback
- **Assignee:** Stafford
- **Due:** 2023-10-19
- **Notes:** This is a quick check for after the meeting, to check with the team, to see if it was successful.

### ✅ Tech meeting feedback
- **Assignee:** Stafford
- **Due:** 2023-10-26
- **Notes:** This is a quick check for after the meeting, to check with the team, to see if it was successful.

### ✅ Tech meeting feedback
- **Assignee:** Stafford
- **Due:** None
- **Notes:** This is a quick check for after the meeting, to check with the team, to see if it was successful.

### ✅ Office/pick up stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-09-13

### ✅ Office/pack van and load stock
- **Assignee:** Tristan Capes
- **Due:** 2023-09-11

### ✅ Chances of another windows machine
- **Assignee:** Caren Bailey
- **Due:** 2023-09-15

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-09-11

### ✅ Cost Increase Detected
- **Assignee:** Caren Bailey
- **Due:** 2023-09-26
- **Notes:** There's an article on Jetbuilt about this activation - exclamation mark feature, never seen before. Please find out how we activate this.

### ✅ Accounts Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-11

### ✅ Update Project IDs in Jetbuilt
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-13

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-09-11
- **Notes:** 1Hr

### ✅ Tech Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-11

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-09-11

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-09-11

### ✅ Leave
- **Assignee:** Stafford
- **Due:** 2023-09-08

### ✅ Update project phases in Harvest
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-13

### ✅ Collect stock and pick up mekyle
- **Assignee:** Tristan Capes
- **Due:** 2023-09-08

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-09-04

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-09-07

### ✅ Include design And Quotes as a Harvest Tasks
- **Assignee:** Darren Swanepoel
- **Due:** 2023-09-11
- **Notes:** Design not showing when tracking time in Harvest. Also look at KPIs for change Orders and Jetbuilt quotes

### ✅ Update bundles for Jetbuilt
- **Assignee:** Caleb Thetard
- **Due:** 2023-10-06

### ✅ Is a Work Breakdown Structure/ Gantt Chart a Good idea on Projects?
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-13
- **Notes:** Thinking about the value of building Gantt Chart / Work Breakdown Structures at the start of the project phase, keen to hear opinions.

### ✅ Design and Site Breakdown
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-06

### ✅ Get Fingerprints for VDV
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-06

### ✅ Jetbuilt process with Caleb and Mands
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Forward Vodacom to Caren
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-07

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-09-07

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-09-07

### ✅ Build project Mind Map of upcoming, process and completed projects
- **Assignee:** Caleb Thetard
- **Due:** 2023-11-10

### ✅ Discuss social media videos for D1
- **Assignee:** Caleb Thetard
- **Due:** None

### ✅ Make another batch of caps.
- **Assignee:** Amanda
- **Due:** 2023-09-15

### ✅ Tech Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-04

### ✅ Set default currency for new projects in Jetbuilt to Rands. It started making them USD since we went to Enterprise demo
- **Assignee:** Caren Bailey
- **Due:** 2023-09-08

### ✅ Accounts Meeting
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-04

### ✅ Bank details
- **Assignee:** Caleb Thetard
- **Due:** None
- **Notes:** Send bank details to Amanda

### ✅ Oakvale Visit
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-04

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** None

### ✅ Update contact to Install Status
- **Assignee:** Caren Bailey
- **Due:** 2023-09-04

### ✅ Contact List
- **Assignee:** Caren Bailey
- **Due:** 2024-02-15
- **Notes:** Share with the company

### ✅ Vign D'Or Design and quote
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-04

### ✅ Project Brief Template
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-06
- **Notes:** Create a project brief template to be added to Overview of the projects

### ✅ Add to Project Wiki
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-04
- **Notes:** Add tasks to project wiki

### ✅ Time test task
- **Assignee:** Amanda
- **Due:** 2023-12-05

### ✅ Update project phases in Jetbuilt
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-08

### ✅ Fix repeating tech and accounts meetings
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2023-09-04

### ✅ Send Fuel Log Template
- **Assignee:** Amanda
- **Due:** 2023-09-06
- **Notes:** If you could send the fuel log template I can get used to clocking the kms.

### ✅ Find Jackets
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-22

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-09-04

### ✅ Tech Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Onboarding
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-01

### ✅ Strategy Day
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-01

### ✅ Strategy Day
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** None
### ✅ linkage/office
- **Assignee:** Tristan Capes
- **Due:** 2023-08-30

### ✅ Tech Meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-08-31

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** None

### ✅ Send Amanda soft copies of Tristan and Mekyle signed contracts please
- **Assignee:** Unassigned
- **Due:** 2023-09-04

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-08-28

### ✅ Pick up Stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-08-25

### ✅ Give us a rate for Ridaah/equivalent per day, if it's an option. With drivers license.
- **Assignee:** Clyde Davis
- **Due:** 2023-08-31

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-08-28

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-08-28

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Caleb kit
- **Assignee:** Caren Bailey
- **Due:** 2023-09-08

### ✅ Admin-emails-coordinating
- **Assignee:** Stafford
- **Due:** None

### ✅ Time off
- **Assignee:** Stafford
- **Due:** None

### ✅ Team building
- **Assignee:** Stafford
- **Due:** 2023-09-01

### ✅ Get a rental price for the Nissan panel van too
- **Assignee:** Amanda
- **Due:** 2023-10-27

### ✅ Do we have any spare desks at the warehouse?
- **Assignee:** Caren Bailey
- **Due:** 2023-08-28

### ✅ Team Meeting 1 Sept 2023 in Paarl
- **Assignee:** Unassigned
- **Due:** 2023-09-01
- **Notes:** booking for 9 staff @ Pearl Valley Club @12:30

https://www.google.com/search?sca_esv=559664296&cs=0&sxsrf=AB5stBjVR_HiCHjORkkwYlMXaGDtZCD8Nw:1692865300289&q=valley+restaurant+paarl+address&ludocid=14668856679390306326&sa=X&ved=2ahUKEwilg__W7vSAAxUlRvEDHUyBAPMQ6BN6BAgfEAI: Pearl Valley Club House R301 Wemmershoek Road, Paarl, 7646

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-08-24

### ✅ Meeting notes (Thursday)
- **Assignee:** Stafford
- **Due:** 2023-08-24

### ✅ Jorge Unanue 70 Quo Transaction
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Hi Mel

Description	INVESTECPB Jorge Unanue 70 Quote
Transaction Amount	8,853.54
Transaction Type	CREDIT

I see 2 Fibre invoices only ?? Is there perhaps another invoice or must this still be approved?

### ✅ Team lunch
- **Assignee:** Stafford
- **Due:** 2023-09-01

### ✅ BARBARA FIBRE VIA AFRIFHOST
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** MEL

Barbara fibre amount has Increase from R547.00 to R997.00.
40MBPs to 150MBPs Openserve Pure Fibre , just letting you know.

### ✅ Get macbook ready and arrange to get it to Caleb +27 81 049 0748
- **Assignee:** Unassigned
- **Due:** None

### ✅ Ask Creatory about office space.
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Arrange VDV contractor access for Caleb
- **Assignee:** Caren Bailey
- **Due:** 2023-08-31

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-08-18

### ✅ Pick up Stafford and Mekyle
- **Assignee:** Tristan Capes
- **Due:** 2023-08-22

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-08-21

### ✅ Travel Claim Excel Document
- **Assignee:** Amanda
- **Due:** 2023-10-20

### ✅ Drop off Sipa1 and puncture repairs
- **Assignee:** Stafford
- **Due:** 2023-08-21

### ✅ Confirm if Stafford phone is insured. Vodacom Will on-siteWill insure for R115pm
- **Assignee:** Amanda
- **Due:** 2023-08-24

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** None

### ✅ Add BSc Engineering to your  email signature
- **Assignee:** Caleb Thetard
- **Due:** 2023-08-31

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-08-21

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-08-21

### ✅ Do Tutorial on Draw.io for doing network/AV designs
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-08
- **Notes:** Try to create this in https://Draw.io
https://drawio-app.com/

### ✅ This is what arrived at my house
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ General/Asana
- **Assignee:** Stafford
- **Due:** 2023-08-18

### ✅ Pick up Stafford and Mekyle
- **Assignee:** Tristan Capes
- **Due:** 2023-08-17

### ✅ Load UPS,s
- **Assignee:** Stafford
- **Due:** 2023-08-14

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2023-08-17

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-08-17

### ✅ Drop 10 cage nuts with Darren
- **Assignee:** Stafford
- **Due:** None

### ✅ redo entire harvest data for the month on new account
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-08-17

### ✅ Pick up trunk at Matos and drop off at Darrens place.
- **Assignee:** Tristan Capes
- **Due:** 2023-08-16

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-08-16

### ✅ Office and Linkage
- **Assignee:** Tristan Capes
- **Due:** 2023-08-14

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-08-14

### ✅ d1technician021@gmail.com on calendar
- **Assignee:** Unassigned
- **Due:** None

### ✅ office
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** book out and collect stock

### ✅ Admin/coordinating
- **Assignee:** Stafford
- **Due:** 2023-08-14

### ✅ Mekyle accounts d1technician021@gmail.com
- **Assignee:** Darren Swanepoel
- **Due:** 2023-08-14

### ✅ Format and prepare Mac and setup for Caleb
- **Assignee:** Unassigned
- **Due:** None

### ✅ Create Gmail d1technician021@gmail.com
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-08-14

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-08-14

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Ensure Mel gets billing for service calls this week
- **Assignee:** Unassigned
- **Due:** 2023-08-14

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-08-11

### ✅ Admin/Asana
- **Assignee:** Stafford
- **Due:** 2023-08-07

### ✅ Study these components to understand how the work
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-08
- **Notes:** If you have time, learning about these components will accelerate your onboarding in September, because they will be familiar.

### ✅ Public Holidy
- **Assignee:** Tristan Capes
- **Due:** 2023-08-10

### ✅ Add a profile pic to your Asana profile
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-15

### ✅ Drop off desk by Darren
- **Assignee:** Tristan Capes
- **Due:** 2023-08-10

### ✅ Carry cableties in your toolbox for incase
- **Assignee:** Unassigned
- **Due:** None

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-08-10

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-08-10

### ✅ Add a KPI score for “taking responsibility for role” for all roles
- **Assignee:** Amanda
- **Due:** 2023-11-15
- **Notes:** I’d like to add this to the scores to measure

### ✅ Hand over Project finances to Mands
- **Assignee:** Darren Swanepoel
- **Due:** 2023-08-14

### ✅ Review all TV purchases and make sure tv license report is up to date
- **Assignee:** Caren Bailey
- **Due:** 2023-08-18

### ✅ UniFi
- **Assignee:** Caleb Thetard
- **Due:** 2023-08-31
- **Notes:** Browse YouTube to learn about UniFi networking and products.

### ✅ Tutorials
- **Assignee:** Caleb Thetard
- **Due:** 2023-08-31
- **Notes:** Complete the basic tutorials for these products. To get familiar with how they work.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-08-10

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Off due to Strike
- **Assignee:** Tristan Capes
- **Due:** 2023-08-07

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-08-03

### ✅ Contact Ghalieb to get a portal login to Savant and do the Savant training
- **Assignee:** Caleb Thetard
- **Due:** None
- **Notes:** ghalieb@planetworld.co.za

### ✅ Change Tristan to tech01@d-one
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Recon Xero
- **Assignee:** Unassigned
- **Due:** 2023-08-17
- **Notes:** Morning Caren

Can you please recon as much as you can, I need to create a snap shot for Darren.

Thanks
Amanda

### ✅ Add a profile pic to your Asana
- **Assignee:** Unassigned
- **Due:** 2023-08-25

### ✅ Youtube Videos
- **Assignee:** Caleb Thetard
- **Due:** 2023-08-31
- **Notes:** https://youtu.be/bRMQtKhZQCQ
https://youtu.be/ryZXX96G_mE
https://youtu.be/MnwZbSYBpQw
https://youtu.be/uoiLAX8i0II
https://youtu.be/2XnYRNwzbQg
https://youtu.be/NRLbwKGfgn4
https://youtu.be/wH-JgZ10vug
https://youtu.be/OPQO_j3yf0Q
https://youtu.be/awJMmQIiXMA

https://www.youtube.com/@SavantAV/videos

And these are some features from some of the security products we use.

https://youtu.be/C_Wv99_pAHM

https://youtu.be/_oiWSL5xSGA


Asana

https://academy.asana.com/series/video-tutorials-tips

A

### ✅ Duplicate of Youtube Videos
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** https://youtu.be/bRMQtKhZQCQ
https://youtu.be/ryZXX96G_mE
https://youtu.be/MnwZbSYBpQw
https://youtu.be/uoiLAX8i0II
https://youtu.be/2XnYRNwzbQg
https://youtu.be/NRLbwKGfgn4
https://youtu.be/wH-JgZ10vug
https://youtu.be/OPQO_j3yf0Q
https://youtu.be/awJMmQIiXMA

https://www.youtube.com/@SavantAV/videos

And these are some features from some of the security products we use.

https://youtu.be/C_Wv99_pAHM

https://youtu.be/_oiWSL5xSGA


Asana

https://academy.asana.com/series/video-tutorials-tips

A

### ✅ Olarm Followup Monitoring Pricing
- **Assignee:** Unassigned
- **Due:** 2023-08-07

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-08-07

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-08-07

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Regal/Homemation
- **Assignee:** Stafford
- **Due:** 2023-08-04

### ✅ Unifi Quote Cloud key Gen 2 at projects
- **Assignee:** Unassigned
- **Due:** None

### ✅ Tech Meeting
- **Assignee:** Unassigned
- **Due:** None

### ✅ Add a field in Harvest for overtime so that it can be logged separately
- **Assignee:** Amanda
- **Due:** 2023-08-03

### ✅ Projects/Admin
- **Assignee:** Stafford
- **Due:** 2023-08-02

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-08-03

### ✅ Hardware
- **Assignee:** Unassigned
- **Due:** 2023-08-01
- **Notes:** Purchase multiplugs

### ✅ Office
- **Assignee:** Unassigned
- **Due:** 2023-08-01
- **Notes:** Meet Tristan & collect stock

### ✅ Office
- **Assignee:** Tristan Capes
- **Due:** 2023-08-01

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-08-03

### ✅ Admin/Planning
- **Assignee:** Stafford
- **Due:** 2023-08-03

### ✅ Meeting with Darren
- **Assignee:** Tristan Capes
- **Due:** 2023-08-01

### ✅ Vpn Server Research
- **Assignee:** Unassigned
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Remove Uber for Tiffany
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Kevin James Wifi
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** tatement Details
Esc to close

Transaction Date
28 Jul 2023
Payee


Reference


Description
ABSA BANK james July Wifi
Transaction Amount
937.65
Transaction Type
CREDIT
Cheque No.

### ✅ Remove all email notifications in Asana settings
- **Assignee:** Caleb Thetard
- **Due:** None

### ✅ Update your profile photo
- **Assignee:** Caleb Thetard
- **Due:** 2023-09-01

### ✅ Log into your D-One apps
- **Assignee:** Unassigned
- **Due:** 2023-09-01
- **Notes:** Your email address is systems@d-one.co.za
And it works to login for Harvest and Asana too.
Have a browse around - start getting a feel for the spaces.
Check out the tutorials.

### ✅ Asana/Emails
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Drop off rainshield at Sensor
- **Assignee:** Tristan Capes
- **Due:** 2023-07-31

### ✅ office
- **Assignee:** Tristan Capes
- **Due:** 2023-07-31

### ✅ Tech meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-07-31

### ✅ Confirm if you are receiving emails on the service@d-one.co.za email address
- **Assignee:** Caren Bailey
- **Due:** 2023-08-01
- **Notes:** Have you set it up, so that you receive these emails?

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-07-31

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-07-31

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Clinic Appointment
- **Assignee:** Tristan Capes
- **Due:** 2023-07-24

### ✅ Planning/Asana
- **Assignee:** Stafford
- **Due:** 2023-07-31

### ✅ clinic appointment
- **Assignee:** Tristan Capes
- **Due:** 2023-07-21

### ✅ Pick up Tiffany
- **Assignee:** Tristan Capes
- **Due:** 2023-07-21

### ✅ Increase the weighting of admin in the technicians KPIs for bonuses. They need to ramp up their Asana for a bonus
- **Assignee:** Amanda
- **Due:** 2023-07-31

### ✅ Project coordinating/followups
- **Assignee:** Stafford
- **Due:** 2023-08-01

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-07-31

### ✅ Contract for Caleb
- **Assignee:** Amanda
- **Due:** 2023-08-04
- **Notes:** ChatGPT / HR lawyer to compile a probation offer with the following:
    3 month probation with 1 week termination from either side.
    R150k protection of Intellectual Property to sign up with Planetworld/Homemation
    R26k c2c + Fuel for work only
    Milestones to be met:
        Training on all products
        Training on all procedures and systems
        Studying of all existing projects 
        Practical training on all roles, including 
            cabling
            installation
  

### ✅ Meeting
- **Assignee:** Amanda
- **Due:** 2023-07-27

### ✅ Ensure that everyone is using Asana and logging time.
- **Assignee:** Stafford
- **Due:** 2023-07-25
- **Notes:** https://d1elec.harvestapp.com/time/week

You can see everyone's time here.

### ✅ Updating Prices in Jetbuilt
- **Assignee:** Caren Bailey
- **Due:** 2023-08-04

### ✅ Tech meeting
- **Assignee:** Stafford
- **Due:** 2023-07-24

### ✅ Double check with Amanda re Mekyle logging
- **Assignee:** Stafford
- **Due:** 2023-07-24

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-07-24

### ✅ Have a browse around our current projects
- **Assignee:** Unassigned
- **Due:** 2023-08-31
- **Notes:** Get accustomed to the current projects, status and feedback.

### ✅ Assign a task with video links to calebthetard@gmail.com
- **Assignee:** Unassigned
- **Due:** 2023-07-21
- **Notes:** Relevant YouTube clips for 
Savant
Hikvision
Dahua
Unifi
IT
Asana
Jetbuilt
Harvest
Home cinemas
Home automation

### ✅ arrange permanent markers for cable labeling when pulling
- **Assignee:** Stafford
- **Due:** None

### ✅ company meeting
- **Assignee:** Unassigned
- **Due:** 2023-07-20

### ✅ Team meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ VDV Meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-07-20

### ✅ Meeting
- **Assignee:** Unassigned
- **Due:** 2023-07-20

### ✅ Company meeting
- **Assignee:** Stafford
- **Due:** 2023-07-20

### ✅ Add "SLA" to the end of project names
- **Assignee:** Darren Swanepoel
- **Due:** 2023-07-21

### ✅ Collect Darren Surf Board
- **Assignee:** Unassigned
- **Due:** 2023-07-19

### ✅ Get supplies from Hardware
- **Assignee:** Tristan Capes
- **Due:** 2023-07-18

### ✅ Get back plate from Triwes
- **Assignee:** Tristan Capes
- **Due:** 2023-07-18

### ✅ Get Rain shield from Sensor
- **Assignee:** Tristan Capes
- **Due:** 2023-07-18

### ✅ Pack van and pick up stock
- **Assignee:** Tristan Capes
- **Due:** 2023-07-18

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-07-17

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-07-17

### ✅ Setup RMA tag in Asana for any returns, so Mel can track them and we don't forget about them.
- **Assignee:** Amanda
- **Due:** 2023-07-24

### ✅ Agenda for Team catchup Braai
- **Assignee:** Darren Swanepoel
- **Due:** 2023-07-18
- **Notes:** 8:30 Start
8:45 Darren 
9am Amanda- Understand Jetbuilt and Stock
9:30 Amanda - Go over Asana and Harvest integration & Contact Service Details
10:30 Darren Amanda Tristan KPI Review
11:00 Darren Amanda Stafford Mekyle KPI Review
11:30 Darren Amanda Imti KPI Review
12:00 Darren Amanda Stafford KPI Review

### ✅ Interview Caleb with Stafford
- **Assignee:** Amanda
- **Due:** 2023-07-21

### ✅ Assist Tiffany with Files
- **Assignee:** Tristan Capes
- **Due:** 2023-07-13

### ✅ Get LTE Router from 9cd
- **Assignee:** Tristan Capes
- **Due:** 2023-07-14

### ✅ Linkqage - collect ups and order necessary consumables for install
- **Assignee:** Tristan Capes
- **Due:** 2023-07-14

### ✅ Trying to Get Access To Ekbergh
- **Assignee:** Tristan Capes
- **Due:** 2023-07-13

### ✅ Pick up Mekyle at home and Collect Monitor From Office
- **Assignee:** Tristan Capes
- **Due:** 2023-07-13

### ✅ Tech Meeting
- **Assignee:** Tristan Capes
- **Due:** 2023-07-13

### ✅ Setup VOYS for Tiffany and send office calls to her
- **Assignee:** Amanda
- **Due:** 2023-07-13

### ✅ Meeting notes Stafford
- **Assignee:** Tristan Capes
- **Due:** 2023-07-13

### ✅ Ghalieb can help arrange the pricelist in the format we need for Jetbuilt. Drop him a mail asking for the format we need and what info is required on it.
- **Assignee:** Caren Bailey
- **Due:** 2023-07-17

### ✅ Train the team to work through Asana when on sites.
- **Assignee:** Stafford
- **Due:** 2023-07-14
- **Notes:** Whenever someone is on a site, they should be going through Asana. There have been times when techs are on site waiting for instruction, when there are tasks on Asana needing attention. I want everyone to be autonomous and independent.

### ✅ Add systems@d-one to Jetbuilt again
- **Assignee:** Darren Swanepoel
- **Due:** 2023-07-11

### ✅ Loop Sam Castle in with fibre plans for Boulders changing from Supersonic
- **Assignee:** Caren Bailey
- **Due:** 2023-07-11
- **Notes:** She works for Nox +27 (84) 441-7106

### ✅ Team catchup
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Fix programming code in Jebuilt
- **Assignee:** Caren Bailey
- **Due:** 2023-07-24
- **Notes:** Programming per hour R900 cost R450

### ✅ Coordinate Asana and harvest tags and tasks for reporting
- **Assignee:** Amanda
- **Due:** 2023-07-11

### ✅ Please Register Mekyle for VdV access
- **Assignee:** Caren Bailey
- **Due:** 2023-07-14

### ✅ Show team: Integrate Harvest and Asana and track on PC
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-07-10

### ✅ Report on D-One's project management
- **Assignee:** Unassigned
- **Due:** 2023-07-13
- **Notes:** Considering your experience and studies. What do you think is missing and how could D-One improve its processes?

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-07-10

### ✅ D meeting notes
- **Assignee:** Stafford
- **Due:** 2023-07-06

### ✅ Try concept draw too
- **Assignee:** Unassigned
- **Due:** 2023-07-07
- **Notes:** Do a typical design with:
Speakers 
Amps
Router
Switch
WAPs
TVs
Cameras

And see how easy it is to use the software - you can use the Windows version.

### ✅ Concept draw for Mac - research
- **Assignee:** Darren Swanepoel
- **Due:** 2023-07-07
- **Notes:** Create templates in X-Diagram for the relevant components in the Oakvale. So we can create line drawing

### ✅ Asana followups
- **Assignee:** Caren Bailey
- **Due:** 2023-11-24
- **Notes:** Hi Mel

Please allocate some time this week to closing off and feeding back on some of the older tasks in Asana to clear them off.

It looks like you are getting through the new ones nicely.

### ✅ Set monthly Olarm fees to customrrs to R90
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Confirm if you have recevied any emails from Caleb thetard @gmail.com
- **Assignee:** Unassigned
- **Due:** None

### ✅ Hayley Val de Vie SLA
- **Assignee:** Caren Bailey
- **Due:** 2023-07-03

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-06-29

### ✅ Update Savant pricelist and update Jetbuilt
- **Assignee:** Caren Bailey
- **Due:** 2023-07-25

### ✅ Pin Point Invoices
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Can I load the pin point invoices in the meantime and has Darren Auth any yet for June 2023?

### ✅ service@d-one.co.za password Support@D1
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Connect LAN to Leon's TV (Base)
- **Assignee:** Stafford
- **Due:** 2023-06-29

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Connect Leon's TV to LAN
- **Assignee:** Stafford
- **Due:** 2023-06-27

### ✅ Vehicles
- **Assignee:** Darren Swanepoel
- **Due:** 2023-08-02
- **Notes:** Calculate how much money we are spending on all of our vehicles, including the Audis. It might make more sense to lease the vehicles from Avis. They buy them and we rent - so it's an expense. Not an asset.

### ✅ Create Trial on Asana
- **Assignee:** Darren Swanepoel
- **Due:** 2023-06-22

### ✅ IP network YouTube tutorials
- **Assignee:** Unassigned
- **Due:** 2023-07-17
- **Notes:** Find Tutorials on Youtube that teach IP networking. 
Routers, switches, WiFi, POE, IP, DHCP, VLAN.

### ✅ Add tag SERVICE to all SLA recurring tasks
- **Assignee:** Unassigned
- **Due:** 2023-07-28
- **Notes:** Specify on all SLAs what needs to be completed on each visit.

### ✅ Train Stafford and Tristan on service procedure
- **Assignee:** Unassigned
- **Due:** 2023-07-03

### ✅ Postpone Caleb to Thu
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Send a pages template for Files o Tiffany
- **Assignee:** Darren Swanepoel
- **Due:** 2023-06-19

### ✅ Setup WAP in tech office
- **Assignee:** Unassigned
- **Due:** None

### ✅ Get access to Savant knowledgebase/support
- **Assignee:** Tristan Capes
- **Due:** None

### ✅ Ask for back specialist mri referral
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ IT training course for Tristan and
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-06-15

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-06-22

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-06-14
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-06-15
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-06-19
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-06-26
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-07-03
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-07-10
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-07-17
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-07-24
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-07-31
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-08-07
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-08-14
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-08-21
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-08-28
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-09-04
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Check with team that their calendars and harvest are updated daily
- **Assignee:** Unassigned
- **Due:** 2023-09-11
- **Notes:** Nudge them on the WhatsApp group if they need to update it.

### ✅ Request D-One, desk, screen, chair and furniture and any other items to be returned to the warehouse from Benji
- **Assignee:** Caren Bailey
- **Due:** 2023-06-15

### ✅ Purchase gas heater and printer for tech office
- **Assignee:** Caren Bailey
- **Due:** 2023-06-13

### ✅ Tasks to Tiffany
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Book focusmate session
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Call Heinrich (Insurance) and discuss project annual numbers for contractors all risk cover - he'll elaborate.
- **Assignee:** Amanda
- **Due:** 2023-06-13

### ✅ Test Installation Project 1
- **Assignee:** Amanda
- **Due:** 2023-07-31

### ✅ Test Installation Project 2
- **Assignee:** Amanda
- **Due:** 2023-08-17

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-06-12

### ✅ Stock process with Mel
- **Assignee:** Unassigned
- **Due:** 2023-06-23
- **Notes:** For the stock managment and accounting sections of the Asana project template, got through it with Mel and update the template accordingly. 

I'll do sales, Stafford can help with installation.

On Monday you'll see how it works.

### ✅ Share systems Google calendar with me
- **Assignee:** Unassigned
- **Due:** 2023-06-13

### ⬜ Build service department and process
- **Assignee:** Unassigned
- **Due:** 2023-06-30
- **Notes:** Build a process for clients to report service calls and get a quick response and follow up.
Take the WhatsApp reporting off of Darren and Stafford.
Find out how other tech service companies do it.

### ✅ Report on Darren's Harvest time to see where time is being spent
- **Assignee:** Darren Swanepoel
- **Due:** 2023-06-17
- **Notes:** Do this at the end of the week, so we have more data.

### ✅ Explain how the day-rate and hourly rate work to Benji
- **Assignee:** Darren Swanepoel
- **Due:** 2023-06-12

### ✅ Tech Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-06-12

### ✅ Test PTZ Dahua on 200m of CAT5e cable
- **Assignee:** Unassigned
- **Due:** 2023-06-26
- **Notes:** We need to confirm that they can operate on a cable that long. Can be setup into a POE switch in the warehouse.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-06-19

### ✅ Setup WiFi in Imti's office
- **Assignee:** Tristan Capes
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Add change order 2x B&Odelivery at R700 p unit
- **Assignee:** Caren Bailey
- **Due:** 2023-06-09

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes accounts
- **Assignee:** Stafford
- **Due:** 2023-06-08

### ✅ Meeting notes tech
- **Assignee:** Stafford
- **Due:** 2023-06-08

### ✅ Check out work spaces
- **Assignee:** Unassigned
- **Due:** 2023-06-08
- **Notes:** D-One 2A Jaguar Park, 14th Avenue, Maitland. Meet Mel in Accounts and Caren in admin.

Innercity Ideas Cartel, co-working space

Workshop17, co-working space

Let me know if you'd like to work from there.

### ✅ Arrange to get Macbook from Digicape to Tiffany.
- **Assignee:** Caren Bailey
- **Due:** 2023-06-06
- **Notes:** Tiffany can collect from Digicape if need be. Or from the warehouse if it's already been sent.

### ✅ See if we can setup a business Uber account that Tiffany can use for transport.
- **Assignee:** Amanda
- **Due:** 2023-06-05

### ✅ Junior Technician - Call Shaun
- **Assignee:** Stafford
- **Due:** 2023-06-05

### ✅ Arrange all service calls this week
- **Assignee:** Stafford
- **Due:** 2023-06-05

### ✅ Get update on Polo repair from insurers
- **Assignee:** Caren Bailey
- **Due:** 2023-06-02

### ✅ Engineer Recruitment
- **Assignee:** Unassigned
- **Due:** 2023-08-04
- **Notes:** Place an ad on PNet. And look for female engineers. Graduates from Technicon or Universities. Living in Western Cape.

### ✅ Give Benji Projects email details
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Sort service tags in Asana
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-05-29

### ✅ Ask for business card from FNB
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Programming planned between now and 8 June
- **Assignee:** Stafford
- **Due:** 2023-05-22
- **Notes:** Let's put it all down here and order in priority, add due dates, delegate where necessary.

### ✅ Setup document file with requirements such as upload technical file
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-05-25

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Send switch models to Jopie Netclick
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Come up with plan for Benji remuneration for adhoc and Imti's leave
- **Assignee:** Darren Swanepoel
- **Due:** 2023-05-26

### ✅ Check if we have second hand accusense cameras in stock in general
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Chat to Benji about dates
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Setup admin payment solution to that Darren doesn't have to send OTPs for stationery purchases
- **Assignee:** Darren Swanepoel
- **Due:** 2023-05-26

### ✅ Clyde for adhoc call-outs
- **Assignee:** Darren Swanepoel
- **Due:** 2023-05-22

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-05-22

### ✅ Catch up with Veejay, see if he's still happy at 4ward
- **Assignee:** Stafford
- **Due:** 2023-05-19

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Confirm Forex
- **Assignee:** Caren Bailey
- **Due:** 2023-05-31
- **Notes:** I got this from FNB, they want me to confirm it. Do we know where or what it's for?

### ✅ Sell monitors @R1000 each
- **Assignee:** Unassigned
- **Due:** 2023-06-14

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Add a profile pic in Asana
- **Assignee:** Unassigned
- **Due:** 2023-06-09

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-05-15

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Create Ruckus template with these in Jetbuilt
- **Assignee:** Caren Bailey
- **Due:** 2023-05-19

### ✅ Ensure pricing is correct for the following bundles on Jetbuilt and make sure new prices are saved to database
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Update Afrihost Credit card
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-05-11

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Connect Tiffany on systems email
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Contact Benji Training and Laptop
- **Assignee:** Unassigned
- **Due:** 2023-05-09

### ✅ Ruckus Account Setup
- **Assignee:** Unassigned
- **Due:** 2023-12-15

### ✅ Mekyle permanent
- **Assignee:** Amanda
- **Due:** 2023-05-08

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-05-08

### ✅ Dont book leave for Tristan for Friday. He worked it in
- **Assignee:** Amanda
- **Due:** 2023-05-05

### ✅ Re-activate Jetbuilt account
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Jetbuilt: Do existing quotes get updated pricing if they haven't processed yet? How do we update a quote to current pricing?
- **Assignee:** Caren Bailey
- **Due:** 2023-05-05

### ✅ UPS quotes
- **Assignee:** Caren Bailey
- **Due:** 2023-05-05
- **Notes:** 1, 3,6,10 kVA with cloud monitoring and control. 
So we can reboot remotely.

### ✅ Stop HeyDay rent
- **Assignee:** Amanda
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-05-02

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-05-02

### ✅ Check Out Software Design Machine
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** https://www.simplyreliable.com/designmachine/

### ✅ Require Invoice No for savant Pro Host in General
- **Assignee:** Caren Bailey
- **Due:** 2023-05-02
- **Notes:** M/N: SVR-5200S-01
SIN: H2WHP1M5Q6NV
UID: 149877851C30000

### ✅ Reset Hikvision Monitor Password
- **Assignee:** Unassigned
- **Due:** 2023-05-02

### ✅ Hang whiteboard
- **Assignee:** Unassigned
- **Due:** 2023-05-19

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-04-24

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-04-24

### ✅ Contracts for Stafford
- **Assignee:** Amanda
- **Due:** 2023-07-28

### ✅ Meeting notes for the week
- **Assignee:** Darren Swanepoel
- **Due:** 2023-04-24
- **Notes:** Stuff to be done this week.

### ✅ Update pricing in bundles
- **Assignee:** Caren Bailey
- **Due:** 2023-05-12
- **Notes:** Update Dstv, network, Araknis, dahua, etc etc ask Jetbuilt how to get current pricing into bundles.

### ✅ Get registered as a Hik-Pro so that we can access their portal
- **Assignee:** Unassigned
- **Due:** None

### ✅ Get all documentation from Benji for claim as per email from insurers.
- **Assignee:** Caren Bailey
- **Due:** 2023-04-24

### ✅ Jetbuilt pricing
- **Assignee:** Caren Bailey
- **Due:** 2023-04-28
- **Notes:** Jetbuilt pricing has been dropped.

Please make sure it's updated.

Spectrum, Planetworld, Homemation, Scoop, Top CCTV, Sensor.

### ✅ Create Whitepages for current sites and transfer Files for easy access
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Consider FreeForm on Mac. Just check portal for Savant and new Mac software.

### ✅ Schedule savant training
- **Assignee:** Unassigned
- **Due:** None

### ✅ Give imti Olarm site serial numbers
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-04-20

### ✅ Need time With Amanda Repair Procedure
- **Assignee:** Unassigned
- **Due:** None

### ✅ Savant and P5 Time
- **Assignee:** Unassigned
- **Due:** None

### ✅ Hikvsion Intercom Monitor Password Reset
- **Assignee:** Unassigned
- **Due:** None

### ✅ Windows PC
- **Assignee:** Amanda
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-04-17

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-04-17

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-04-17

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-04-13

### ✅ Advertise for a technician again - we're still looking
- **Assignee:** Caren Bailey
- **Due:** 2023-04-13

### ✅ Send Latest numbers D-One VW Silver Polo KM Petrol Claim
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-04-11

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-04-11

### ✅ Let Gilbert go
- **Assignee:** Amanda
- **Due:** 2023-04-11
- **Notes:** Sounds like he's not a D1 fit.

### ✅ Train Benji on servicing process
- **Assignee:** Amanda
- **Due:** 2023-04-11

### ✅ Setup Olarm Portal witjh clients loaded
- **Assignee:** Unassigned
- **Due:** 2023-04-28

### ✅ Savant Training Questions
- **Assignee:** Unassigned
- **Due:** 2023-12-21

### ✅ Invoice Frame R20k ex VAT for Ref: Refundable design services House Khumalo
- **Assignee:** Caren Bailey
- **Due:** 2023-04-17

### ✅ Consider this option for servicing and feed back
- **Assignee:** Amanda
- **Due:** 2023-04-06
- **Notes:** https://jetbuilt.com/uk/service/

Might be cost prohibitive

### ✅ Systems adoption
- **Assignee:** Unassigned
- **Due:** 2023-04-06
- **Notes:** Ramp up adoption of Asana, Calendar and Harvest. 
We use these tools daily for project updates and communication. 
They allow us to communicate very efficiently and clearly. It also gives us a record to refer back to. 
Please update them daily. And start to build the practice. 

- Asana for all actions and feedback on projects.
- Calendar for movements. Keep it current and updated to make easy pulling data to harvest. 
- Harvest for time allocation. 

This data gives us great ammo for billing.

### ✅ tech training with suppliers
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** https://app.asana.com/0/726298113552142/726298113552142 , https://app.asana.com/0/349302067847971/349302067847971 Can explain and elaborate regards to the above

### ✅ Consider this for servicing and RMA - Give feedback
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** https://jetbuilt.com/service/

### ✅ Prepare all savant questions for programming training
- **Assignee:** Unassigned
- **Due:** 2023-04-07

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-04-14

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-04-03

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-04-03

### ✅ Take the vehicle for a roadworthy test in order to get a license disk.
- **Assignee:** Unassigned
- **Due:** 2023-04-05

### ✅ Cable Feeders Systems
- **Assignee:** Unassigned
- **Due:** 2023-03-31
- **Notes:** Account paid short in October and 1 Invoice not captured . According to Xero this is what was paid.

### ✅ Interview new technician
- **Assignee:** Stafford
- **Due:** 2023-03-31
- **Notes:** Last day of the month. So if he's gonna give notice. Nows the time.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Please book back in General Stock
- **Assignee:** Caren Bailey
- **Due:** 2023-03-31

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-30

### ✅ Hand over projects and contacts to Stafford
- **Assignee:** Darren Swanepoel
- **Due:** 2023-03-31

### ✅ Send all contact details to Marnita
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Spectrum training when Darren returns
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-27

### ✅ Complete Savant training
- **Assignee:** Unassigned
- **Due:** 2023-04-28

### ✅ Do savant portal programming training
- **Assignee:** Tristan Capes
- **Due:** 2023-06-23
- **Notes:** Speak to Rudi if need be. And get sorted on portal and training.

### ✅ Visit Dahua Century City instead of Somerset west
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** They have a demo facility in Century City. Ask Marc to setup a demo for you there. Instead of Somerset West.

### ✅ Feb - Service report
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Get certified ID
- **Assignee:** Darren Swanepoel
- **Due:** 2023-03-24

### ✅ Tracker query on Polo
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Send Tiffany research pack for D-One and prep for internehip
- **Assignee:** Darren Swanepoel
- **Due:** 2023-05-08
- **Notes:** Help us go from reaction to planned.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-23

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Create RMA process in Asana
- **Assignee:** Amanda
- **Due:** 2023-03-23
- **Notes:** https://app.asana.com/0/1203778673624658/list will help create the procedure for this.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-20

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-20

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-20

### ✅ Inform Tristan of his raise amount
- **Assignee:** Amanda
- **Due:** 2023-03-23

### ✅ Sort office for Imti
- **Assignee:** Stafford
- **Due:** 2023-03-22
- **Notes:** Arrange banner, desks, screens etc.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-03-16
- **Notes:** I'll observe, Stafford and Imti run through notes.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-03-16

### ✅ Send technician ad to Imti so he can share it.
- **Assignee:** Caren Bailey
- **Due:** 2023-03-13

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-16

### ✅ Take desk etc to Maitland in the caddy
- **Assignee:** Stafford
- **Due:** 2023-03-13
- **Notes:** It's in my garage
Just the desk, office chair, standing desk planks, leave the couch.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Fill out poll on D-One WhatsApp for money mindset workshop
- **Assignee:** Stafford
- **Due:** 2023-03-10

### ✅ Tracker mileage 2025
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Get details from Mands to allocate mileage to business travel on the Tracker app.

### ✅ Send serial numbers of both Araknis 16port switches to see why we ordered them
- **Assignee:** Caren Bailey
- **Due:** 2023-03-23

### ✅ Add to general
- **Assignee:** Caren Bailey
- **Due:** 2023-03-15

### ✅ Accounts notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Update credit card for Afrihost
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Check all Lutron specs when ordering with Homemation
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** I made an error on a code. They asked if we can just let them know when we're ordering Lutron, and they'll double check our orders t make sure they're compatible for us.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-06

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-06

### ✅ Interview Rikie
- **Assignee:** Darren Swanepoel
- **Due:** 2023-03-06

### ✅ Let staff know that there are no more loans.
- **Assignee:** Amanda
- **Due:** 2023-03-10

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-02

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-03-02

### ✅ Collect mobile AC from office
- **Assignee:** Unassigned
- **Due:** 2023-03-01

### ✅ Train technicians on how you want them to log Harvest services and programming.
- **Assignee:** Amanda
- **Due:** 2023-03-23

### ✅ Postpone meetings
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-27

### ✅ Look into projects to invoice
- **Assignee:** Darren Swanepoel
- **Due:** 2023-03-03

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-27

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-02-27

### ✅ Accounts notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-27

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-27

### ✅ Postpone money workshop
- **Assignee:** Darren Swanepoel
- **Due:** 2023-03-02

### ✅ Email signature
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2023-02-23

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-23

### ✅ Business registration for vehicles
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-27

### ✅ General Stock take
- **Assignee:** Unassigned
- **Due:** 2023-02-23
- **Notes:** General stock take had to do manual count and write down item codes and descriptions as loadshedding and Melissa capturing on Jetbuild.

### ✅ Create Login for integrator@d-one.co.za on Engenius cloud
- **Assignee:** Unassigned
- **Due:** 2023-02-21

### ✅ Get the word out we are looking for another team. And let me know if we need Pin Point short term
- **Assignee:** Stafford
- **Due:** 2023-02-22

### ✅ Look at stock value beginning and end of period. Apparently we can hide profit here
- **Assignee:** Amanda
- **Due:** None

### ✅ We should earth racks and everything in them
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-21

### ✅ Give Benji access to Xero quotes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Money Follow UP
- **Assignee:** Caren Bailey
- **Due:** 2023-03-08
- **Notes:** Hi Mel

Please follow up on this money outstanding

### ✅ Office status and VOIP phone - DVD/General
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-20

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-02-20

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-20

### ✅ Mail Marnita Thursday?
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-20

### ✅ Imti Week plan
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-20

### ✅ Reschedule money talk
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Val De Vie Registration Completion
- **Assignee:** Unassigned
- **Due:** 2023-02-15

### ✅ Get a Voys Phone Extension for Imti via App
- **Assignee:** Caren Bailey
- **Due:** 2023-02-15
- **Notes:** Need an extension to be setup for Imti so that he can setup Voys App on Phone

### ✅ Email signature
- **Assignee:** Amanda
- **Due:** 2023-02-24
- **Notes:** Create a generic email signature that we can all use in our Gmail.

### ✅ Office plan
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Plan tasks to get top office ready.

### ✅ Arrange screen. Measure Maitland top office width and height of wall
- **Assignee:** Amanda
- **Due:** 2023-02-15

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-13

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-13

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-02-13

### ✅ Arrange business vehicle license with VW sales guy
- **Assignee:** Amanda
- **Due:** 2023-03-23

### ✅ Billable Services
- **Assignee:** Amanda
- **Due:** None
- **Notes:** Going forward, hours allocated to callouts must be allocated to Services Tech/Programming rates in Harvest.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-13

### ✅ Add Mekyle to Asana D-One Organization
- **Assignee:** Caren Bailey
- **Due:** 2023-02-10

### ✅ Add new Projects to Harvest via Asana
- **Assignee:** Caren Bailey
- **Due:** 2023-02-16

### ✅ Let me know if you can see all projects, or only a few
- **Assignee:** Unassigned
- **Due:** 2023-02-10

### ✅ Add Mekyle to Asana
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-13

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-02-09

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-09

### ✅ Make more T-shirts and polos for Imti and Mikyle
- **Assignee:** Amanda
- **Due:** 2023-03-23

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-16

### ✅ Plan for next week
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** I will introduce you to the projects this week.

### ✅ Get Parallels sorted for Imti
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-06

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-02-06

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Benji to attend Tech meeting in the car enroute to Paarl, to be in Paarl 08:30
- **Assignee:** Unassigned
- **Due:** 2023-02-06

### ✅ Create Equipment list template in Jetbuilt
- **Assignee:** Unassigned
- **Due:** 2023-02-07
- **Notes:** Go to Designer and create a new page.

### ✅ Download and Learn XDiagram
- **Assignee:** Unassigned
- **Due:** None

### ✅ Fix Mellisa Printer, Configure VOX Phone and Sonos
- **Assignee:** Unassigned
- **Due:** 2023-02-07

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-02-02

### ✅ Add 5 Ave des huguenots to harvest.
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-02-02

### ✅ Share integrator Google calendar with:
- **Assignee:** Unassigned
- **Due:** 2023-02-03

### ✅ Complete tutorials
- **Assignee:** Unassigned
- **Due:** 2023-02-28

### ✅ Cancel Benji's leave for today. He worked remotely.
- **Assignee:** Caren Bailey
- **Due:** 2023-02-02

### ✅ Bring small desk from warehouse for Imti in Paarl. And chair
- **Assignee:** Stafford
- **Due:** 2023-02-01

### ✅ Leave-Benji
- **Assignee:** Caren Bailey
- **Due:** 2023-02-01
- **Notes:** Did you load Benji's leave from last week? Formal application follow up needed.

### ✅ KPI
- **Assignee:** Tristan Capes
- **Due:** 2023-02-03
- **Notes:** KPI document to fill out with detail under all bold lines (Admin, Jetbuilt etc).

### ✅ KIP - Benji
- **Assignee:** Amanda
- **Due:** 2023-02-14
- **Notes:** KPI document to fill out with detail under all bold lines.

### ⬜ KPI- Detail
- **Assignee:** Stafford
- **Due:** None
- **Notes:** KPI document to fill out with detail under all bold lines.

### ✅ Update pricing on Jetbuilt for AV projects slab boxes. R400 cost and R680 ex retail
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Make Imti a new book
- **Assignee:** Amanda
- **Due:** 2023-01-31

### ✅ Identify Afrihost client
- **Assignee:** Caren Bailey
- **Due:** 2023-02-02

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-01-30

### ✅ Mekyle and IMTI access at VDV
- **Assignee:** Caren Bailey
- **Due:** 2023-02-14

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-01-30

### ✅ Return P5 demo stock that was in the office
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Send money workshop to Imti
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2023-01-30

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2023-01-30

### ✅ Vision board
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Share marketing and pricelist with accounts
- **Assignee:** Darren Swanepoel
- **Due:** 2023-01-26

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-01-23

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2023-01-23

### ✅ Get dealer account with ecoflow.co.za
- **Assignee:** Caren Bailey
- **Due:** 2023-01-31

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Arrange shelving for 2nd store
- **Assignee:** Caren Bailey
- **Due:** 2023-01-25
- **Notes:** We need to organize the stock in the second store.

### ✅ Pay Mikyle please
- **Assignee:** Amanda
- **Due:** 2023-01-20

### ✅ Add new laptop to insurance
- **Assignee:** Amanda
- **Due:** 2023-01-26

### ✅ Takealot
- **Assignee:** Darren Swanepoel
- **Due:** 2023-01-19
- **Notes:** We need takealot invoices, log in details requested.

### ✅ Leave forms
- **Assignee:** Caren Bailey
- **Due:** 2023-01-23

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2023-01-19

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2023-01-19

### ✅ Do Jetbuilt training session with sales people
- **Assignee:** Stafford
- **Due:** None

### ✅ Tristan technician@d-one.co.za for simple pay
- **Assignee:** Amanda
- **Due:** 2023-01-18

### ✅ Create account at Mustek
- **Assignee:** Caren Bailey
- **Due:** 2023-01-19

### ✅ Darren's couch to Maitland
- **Assignee:** Stafford
- **Due:** 2023-02-03
- **Notes:** Collect couch from VDV and take to Maitland office

### ✅ Organize SONOS Roam for office
- **Assignee:** Caren Bailey
- **Due:** 2023-01-25

### ✅ Setup account on Digicape website for D-One with our discount
- **Assignee:** Caren Bailey
- **Due:** 2023-01-19

### ✅ Ask Marc Top CCTV where all the rebate stock is.
- **Assignee:** Caren Bailey
- **Due:** 2023-01-23

### ✅ Toolbox check list
- **Assignee:** Stafford
- **Due:** None
- **Notes:** Populate this and run through with the team quarterly in 2023.

### ✅ Find out how to book stock in and out on Jetbuilt
- **Assignee:** Caren Bailey
- **Due:** 2022-12-12

### ✅ Jetbuilt Version template
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** 1.2 MS|12Dec22 Description: Reference.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-12-12

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-12-12

### ✅ Order Tristan's sunnies for delivery to his house
- **Assignee:** Caren Bailey
- **Due:** 2023-02-10

### ✅ Followups list
- **Assignee:** Stafford
- **Due:** 2022-12-12

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-12-08

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-12-05

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Deliver bike from Darren's garage to klapmuts where cable goes
- **Assignee:** Tristan Capes
- **Due:** 2022-12-02
- **Notes:** The small Specialized black and red one

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-12-01

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Arrange to have demos collected from Sutherland reception and delivered to Homemation and Planetworld
- **Assignee:** Caren Bailey
- **Due:** 2022-12-07

### ✅ Send Jason Nautomation
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Collect sunnies
- **Assignee:** Unassigned
- **Due:** 2023-03-06

### ✅ Cancel HArvest etc.
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Publish holidays to staff. Check when Base opens 2023
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-11-28

### ✅ Ask Marc Kruger if he can do audits on our projects
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-11-28

### ✅ Tristan 1 year voucher
- **Assignee:** Caren Bailey
- **Due:** 2022-11-28
- **Notes:** Buy a R1000 superbalist or takealot voucher and give to Tristan for 1 year gift from D1.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ End 2022 plan
- **Assignee:** Darren Swanepoel
- **Due:** 2022-12-15
- **Notes:** Please see the plan for the end of the year. This is where each of us needs to be focused to wrap up 2022.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-11-24

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-11-24

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Move Jetbuilt templates into correct systems
- **Assignee:** Caren Bailey
- **Due:** 2022-11-22

### ✅ Soccer World cup R500 bet
- **Assignee:** Darren Swanepoel
- **Due:** 2022-12-18

### ✅ Look into virtual cards for Tristan/Stafford
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-11-21

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-11-21

### ✅ Update details
- **Assignee:** Caren Bailey
- **Due:** 2022-11-21

### ✅ Setup business WhatsApp
- **Assignee:** Caren Bailey
- **Due:** 2022-11-18

### ✅ create automated message for whatsapp business
- **Assignee:** Darren Swanepoel
- **Due:** 2022-11-17

### ✅ Setup business WhatsApp
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-11-17

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-11-17

### ✅ Setup monthly email with all suppliers bcc'd in to ask for new price updates. Automate it to send monthly.
- **Assignee:** Caren Bailey
- **Due:** 2022-11-30

### ✅ Call Etienne re Spilhaus
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-11-14

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-11-14

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-11-10

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-11-10

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-11-07

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-11-07

### ✅ 9CD alarm and pool terrace speakers
- **Assignee:** Stafford
- **Due:** None

### ✅ Fluke testers
- **Assignee:** Stafford
- **Due:** None
- **Notes:** Facebook marketplace listing link for fluke testers.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-11-03

### ✅ Upload the following projects main quote into Jetbuilt
- **Assignee:** Unassigned
- **Due:** 2022-11-16
- **Notes:** Mel will chat to you about how and what to do.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Assign project migrations over to Caren
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Link Jetbuilt to suppliers
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-31

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-10-31

### ✅ Change fibre name from SLA to fibre
- **Assignee:** Caren Bailey
- **Due:** 2022-10-31
- **Notes:** Clients think they have an SLA with us and expect service. We need to change the name of the monthly SLA to Internet data.

### ✅ Accounts meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-10-27

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-27

### ✅ FICA FNB
- **Assignee:** Amanda
- **Due:** 2023-03-23
- **Notes:** FNB: Business FICA info required. Select Business Solutions > Compliance update on online banking to remain compliant.

### ✅ Correct pricing in Jetbuilt
- **Assignee:** Caren Bailey
- **Due:** 2022-10-25
- **Notes:** Pricing loaded incorrectly for Khumalo quote, needs urgent correction to match current supplier pricelists.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-24

### ✅ Invoice Rachel 102 Builders
- **Assignee:** Caren Bailey
- **Due:** 2022-11-01
- **Notes:** Please invoice Rachel for a call out at 102 Boulders - swop and configure router, 1 hour.

### ✅ Create database for new products from Planetworld
- **Assignee:** Caren Bailey
- **Due:** 2022-10-20
- **Notes:** Audioquest, Adeo, Black Nova, Cambridge, Dali, iPort, Jamo, M&K, Onkyo, Parasound, Pioneer, Vogels, Vogels pro, Velodyne. And TOP CCTV attached.

### ✅ Prepare these for import into Jetbuilt
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Planetworld, Vogels, M&K, Pioneer, TOP CCTV

### ✅ Talk to jet build and send them our supplier contact details for updating pricelists
- **Assignee:** Caren Bailey
- **Due:** 2022-10-25

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2022-10-20

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-20

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-10-20

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Receipt stock
- **Assignee:** Unassigned
- **Due:** 2022-09-05

### ✅ Stock Receipt
- **Assignee:** Unassigned
- **Due:** 2022-09-15
- **Notes:** receipt stock

### ✅ Stock Take
- **Assignee:** Unassigned
- **Due:** 2022-09-26

### ✅ Find equipment
- **Assignee:** Unassigned
- **Due:** 2022-09-06
- **Notes:** Looking for a full size pizza tray to bake large pizzas in a Weber Braai (need 3) and a size 14 Potjie pot.

### ✅ Organize 15 multicoloured helium balloons to be delivered to Boschendal Friday am
- **Assignee:** Unassigned
- **Due:** 2022-09-08
- **Notes:** Order 20 multicoloured helium balloons on strings, collect in Paarl Friday morning.

### ✅ Follow up on "Find equipment"
- **Assignee:** Unassigned
- **Due:** 2022-09-07

### ✅ Stock receipt
- **Assignee:** Unassigned
- **Due:** 2022-09-08
- **Notes:** Melissa

### ✅ Stock Received
- **Assignee:** Unassigned
- **Due:** 2022-10-03

### ✅ Sell office desks. Info tomorrow
- **Assignee:** Unassigned
- **Due:** 2022-10-17
- **Notes:** Try core, will fill you in tomorrow

### ✅ Meeting notes
- **Assignee:** Tristan Capes
- **Due:** 2022-10-17

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-10-17

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-17

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2022-10-17

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-13

### ✅ Discuss call-waiting with Voys
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Do Numbers quote for:
- **Assignee:** Caren Bailey
- **Due:** 2022-10-13
- **Notes:** Quote with 2 sections: Savant and Control4, comparing main processors, wall keypads, touch screens, dimmer and relay modules.

### ✅ Ask Kim Homemation to ship notebooks with our next stock delivery to the warehouse
- **Assignee:** Caren Bailey
- **Due:** 2022-10-11

### ✅ Setup accounts prep meetings
- **Assignee:** Amanda
- **Due:** 2022-10-10
- **Notes:** Go through weekly winnings reports during tech meeting so details are ready for accounts meeting at 9, Mondays and Thursdays. Setup recurring Google Meet.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-10-10

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-10

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Find out if the Contractor gate is opening again?
- **Assignee:** Amanda
- **Due:** 2022-10-13
- **Notes:** Ask Val de Vie if they are going to open the contractor gate again. Our guys are losing a lot of time queueing at the gate.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-06

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-10-03

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-10-03

### ✅ Count all keypads
- **Assignee:** Tristan Capes
- **Due:** None

### ✅ Bring caps to VDV
- **Assignee:** Unassigned
- **Due:** 2022-10-17
- **Notes:** Done

### ✅ Ask Afrihost for Coupons for fibre lines. We should be getting discounts from them. When applying they have a space to enter coupons.
- **Assignee:** Unassigned
- **Due:** 2023-02-10

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-09-26

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-09-26

### ✅ Purchase network adapter for Stafford apple laptop
- **Assignee:** Stafford
- **Due:** None

### ✅ Did we order D-One caps on the end?
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Receipt Stock
- **Assignee:** Unassigned
- **Due:** 2022-09-21
- **Notes:** Receiving Stock

### ✅ Update DEAR pricing with TOP CCTV pricelist in pricelist folder
- **Assignee:** Caren Bailey
- **Due:** 2022-09-30

### ✅ Helmet into car, add branding and name
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ D-One braai?
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Sort out projects and budgets in Harvest
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-09-19

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-09-19

### ✅ Return this second one
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-09-15

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-09-15

### ✅ Maumela fibre
- **Assignee:** Caren Bailey
- **Due:** 2022-09-12
- **Notes:** Reactivate Maumela fibre, let him know if there's a faster option, send amount due for payment.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-09-12

### ✅ Project budgets
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-09-12

### ✅ Dear Sync
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Tried to sync Dear - 14 invoices failed, please look at them.

### ✅ Find out where we can buy Aquavision TVs. And get dealer pricing for one for a sauna.
- **Assignee:** Unassigned
- **Due:** 2022-09-09
- **Notes:** TV that can be installed in a bathroom or sauna, various brands available.

### ✅ Please order ink for my printer Epson
- **Assignee:** Unassigned
- **Due:** 2022-09-08
- **Notes:** 1x 664 Cyan, 1x 664 Magenta, 2x 664 Black, 1x 664 Yellow.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Discuss accounts with interest with Mands and suppliers
- **Assignee:** Darren Swanepoel
- **Due:** 2022-09-06

### ✅ Quote Hayley asap
- **Assignee:** Caren Bailey
- **Due:** 2022-09-06
- **Notes:** Melissa this is urgent, was supposed to be done yesterday.

### ✅ Harvest-AUG
- **Assignee:** Darren Swanepoel
- **Due:** 2022-09-05

### ✅ Purchase or invest?
- **Assignee:** Darren Swanepoel
- **Due:** 2022-09-07
- **Notes:** For Matos, Vrymansfontein, Oakvale, Strydom - confirm if ordering now or investing, Mel has already placed orders.

### ✅ Populate Projects planning calendar with relevant projects (Harrigan already done)
- **Assignee:** Stafford
- **Due:** 2022-10-10
- **Notes:** Vrymansfontein completion 30 Aug 2023, Oakvale completion 30 Aug 2023, Matos completion 30 March 2023, Strydom completion Aug 2023.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-09-05

### ✅ Meeting notes
- **Assignee:** Tristan Capes
- **Due:** 2022-09-05

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-09-05

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-09-05

### ✅ Find mouse for Benji
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-09-01

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-09-01
- **Notes:** Update on pearl Valley

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-09-01

### ✅ Cambium router for Benji
- **Assignee:** Darren Swanepoel
- **Due:** 2022-09-02

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-08-29
- **Notes:** What is the plan with the magglocks at battery 6 and 8

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-08-29

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-08-29

### ✅ Asana prioritizing
- **Assignee:** Unassigned
- **Due:** 2022-09-30

### ✅ Compliance FNB
- **Assignee:** Amanda
- **Due:** 2022-08-26
- **Notes:** FNB requested confirmation of business account info to avoid account being frozen.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Battery 6 and 8

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-08-25

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-08-25

### ✅ DHL
- **Assignee:** Caren Bailey
- **Due:** 2022-08-24
- **Notes:** Make sure they have received the payment Mands made for the package.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ General notes
- **Assignee:** Stafford
- **Due:** 2022-08-22

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-08-22

### ✅ Apply for an import code
- **Assignee:** Darren Swanepoel
- **Due:** 2023-06-01
- **Notes:** Aramex global shopper import code requirement.

### ✅ Oakleys feedback
- **Assignee:** Unassigned
- **Due:** 2022-08-29

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-08-18

### ✅ Accounts Meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-08-15

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-08-15

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Follow up on "Upload aged receivables here with notes"
- **Assignee:** Caren Bailey
- **Due:** 2022-08-15

### ✅ Delete Tristans old Asana i moved it all to the new profile.
- **Assignee:** Darren Swanepoel
- **Due:** 2022-08-10

### ✅ When do Swans leave?
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-08-10

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-08-10

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-08-04

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-08-04

### ✅ open a cash account with Frantosa
- **Assignee:** Caren Bailey
- **Due:** 2022-08-02

### ✅ Project management meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2022-08-12

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Check calendars - Stafford-Tristan duplication
- **Assignee:** Darren Swanepoel
- **Due:** 2022-07-31

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2022-08-01

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-08-01

### ✅ Mel's new laptop from Darren
- **Assignee:** Stafford
- **Due:** 2022-07-28
- **Notes:** Will come through there.

### ✅ Add new profile pic in Asana
- **Assignee:** Tristan Capes
- **Due:** 2022-07-29

### ✅ Reassign tasks on old email. So we can remove that account from Asana
- **Assignee:** Tristan Capes
- **Due:** 2022-07-29

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Order 4 sweaters 2 for Riaan and 2 for Clyde
- **Assignee:** Caren Bailey
- **Due:** 2022-08-05

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-07-28

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-07-28

### ✅ Assign email for Tristan
- **Assignee:** Darren Swanepoel
- **Due:** 2022-07-29

### ✅ Upload pic of next week's completed calendars
- **Assignee:** Stafford
- **Due:** None

### ✅ Upload pic of next week's completed calendars
- **Assignee:** Stafford
- **Due:** None

### ✅ Upload pic of next week's completed calendars
- **Assignee:** Stafford
- **Due:** None

### ✅ Upload pic of next week's completed calendars
- **Assignee:** Stafford
- **Due:** None

### ✅ Upload pic of next week's completed calendars
- **Assignee:** Stafford
- **Due:** None

### ✅ Upload pic of next week's completed calendars
- **Assignee:** Stafford
- **Due:** None

### ✅ Upload pic of next week's completed calendars
- **Assignee:** Stafford
- **Due:** None

### ✅ battery wiring
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Excuse me from tech meeting. Is there anything you need from me?
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-07-21

### ✅ Harvest Support assisting me with the issue i'm experiencing
- **Assignee:** Unassigned
- **Due:** 2022-07-22

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-07-18

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-07-18

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Complete current time allocation in current role
- **Assignee:** Unassigned
- **Due:** 2022-08-05
- **Notes:** Go through calendar, harvest and Asana for average hours per week per task.

### ✅ Confirm if Trafalgar management made payment
- **Assignee:** Caren Bailey
- **Due:** 2022-07-19

### ✅ Check all fibre bills to make sure that there aren't fibre ISP's being paid for accounts that we are not billing for.
- **Assignee:** Caren Bailey
- **Due:** 2022-07-26
- **Notes:** Review all new fibre invoices.

### ✅ Check our access please.
- **Assignee:** Caren Bailey
- **Due:** 2022-07-21

### ✅ Accounts meeting measurables
- **Assignee:** Caren Bailey
- **Due:** 2022-07-25
- **Notes:** Report on numbers and plot in a graph from Xero.

### ✅ Accounts meeting measurables
- **Assignee:** Caren Bailey
- **Due:** 2022-08-01
- **Notes:** Report on numbers and plot in a graph from Xero.

### ✅ Accounts meeting measurables
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Report on numbers and plot in a graph in numbers/from Xero.

### ✅ Review projects and tasks.
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Invoice client
- **Assignee:** Caren Bailey
- **Due:** 2022-07-22
- **Notes:** Boulder Apartments Body Corporate c/o Trafalgar Property Management, VAT 4360110144.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Send Integrator spec to Benji
- **Assignee:** Unassigned
- **Due:** 2022-07-11

### ✅ meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-07-07

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-07-07

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Ensure VOYS is working - people are struggling to get through to us
- **Assignee:** Caren Bailey
- **Due:** 2022-07-05

### ✅ Process Elan quote & order
- **Assignee:** Caren Bailey
- **Due:** 2022-07-05

### ✅ Login details to accounts for Yoco
- **Assignee:** Darren Swanepoel
- **Due:** 2022-07-04

### ✅ Negotiate with Yoco
- **Assignee:** Amanda
- **Due:** 2022-07-08

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-07-04

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-07-04

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Add an Asana profile pic
- **Assignee:** Unassigned
- **Due:** 2022-07-04

### ✅ Design KPI reporting scorecard for us to review weekly, monthly
- **Assignee:** Unassigned
- **Due:** 2022-07-29

### ✅ Confirm we didn't get invoices for Fleet demo system
- **Assignee:** Caren Bailey
- **Due:** 2022-07-04

### ✅ Load harvest, Asana, calendar, HubSpot phone apps
- **Assignee:** Unassigned
- **Due:** 2022-07-01

### ✅ Setup finger print
- **Assignee:** Unassigned
- **Due:** 2022-07-01

### ✅ Setup Finder
- **Assignee:** Unassigned
- **Due:** 2022-07-01

### ✅ Setup Apple ID
- **Assignee:** Unassigned
- **Due:** 2022-07-01

### ✅ Petrol
- **Assignee:** Darren Swanepoel
- **Due:** 2022-07-05

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-06-30

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Count=Quote in numbers template
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Tech meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Read Traction. Get book from Darren
- **Assignee:** Stafford
- **Due:** 2022-07-29

### ✅ Cable order
- **Assignee:** Caren Bailey
- **Due:** 2022-06-23

### ✅ Evo training
- **Assignee:** Caren Bailey
- **Due:** 2022-07-06

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-06-23

### ✅ Clean up old tasks in Asana, and reorder priorities
- **Assignee:** Unassigned
- **Due:** 2022-06-25

### ✅ Scorecard
- **Assignee:** Stafford
- **Due:** 2022-07-06
- **Notes:** Review scorecard weekly, report back monthly, provide feedback on what needs to be added/changed.

### ✅ Update calendars
- **Assignee:** Stafford
- **Due:** 2022-06-22

### ✅ Register with Kathea
- **Assignee:** Caren Bailey
- **Due:** 2022-06-21

### ✅ Send contract to Jonathan for signing
- **Assignee:** Amanda
- **Due:** 2022-06-28

### ✅ Drill, Hammer and nails and bulbs for office
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Adjust rates for tech logging harvest for sale task and same site
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Harvest training
- **Assignee:** Darren Swanepoel
- **Due:** 2022-06-15

### ✅ Harvest caught up
- **Assignee:** Unassigned
- **Due:** 2022-06-20
- **Notes:** Harvest slipping, please catch it up.

### ✅ Harvest
- **Assignee:** Unassigned
- **Due:** 2022-06-15
- **Notes:** Please ensure Harvest is updated, arrange training if needed.

### ✅ Quote arri@lung.co.za 2x Vecta speakers at COST price
- **Assignee:** Caren Bailey
- **Due:** 2022-06-14
- **Notes:** 1 pair of white Vecta speakers from Homemation with corner mount brackets, arrange delivery to table view.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-06-13

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-06-13

### ✅ Tech meetings
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Shop for Macbook air second hand not older than 2019
- **Assignee:** Unassigned
- **Due:** 2022-06-15

### ✅ Confirm if Top Gun will still be showing on 1 July, Cape Gate or Tyger Valley After 2:30pm
- **Assignee:** Caren Bailey
- **Due:** 2022-06-30

### ✅ Change Mel's email name to D-One Accounts
- **Assignee:** Caren Bailey
- **Due:** 2022-06-17
- **Notes:** Change display name from D-One Admin to D-One Accounts in Gmail settings.

### ✅ Order another office chair from Makro like this for delivery to 1003 Courson st, Val de Vie
- **Assignee:** Caren Bailey
- **Due:** 2022-06-10

### ✅ Undo forward Sales emails
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Change SSC- WI0031-01 to unit Each in DEAR
- **Assignee:** Caren Bailey
- **Due:** 2022-06-10

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-06-09

### ✅ Register for this on zoom
- **Assignee:** Stafford
- **Due:** 2022-06-10

### ✅ Change Fibre billing from SLA Network service to Internet
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Clients think they're paying us for an SLA service, actually paying for Data - change reference to Internet.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-06-09

### ✅ Quote Levi Uppink
- **Assignee:** Caren Bailey
- **Due:** 2022-06-07
- **Notes:** Will get details of where to send the quote to.

### ✅ Add a profile pic to Asana
- **Assignee:** Unassigned
- **Due:** 2022-07-08

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-06-06

### ✅ Change Colleen appointment day
- **Assignee:** Amanda
- **Due:** 2022-06-06
- **Notes:** Jason here Thursday, can we do Tuesday or Wednesday?

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-06-06

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Register Jon.mcclean@gmail.com for VDV work access under d-one
- **Assignee:** Caren Bailey
- **Due:** 2022-06-16

### ✅ Meet forMeet for phone handover
- **Assignee:** Stafford
- **Due:** 2022-06-06

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-06-02

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Move to planetworld
- **Assignee:** Caren Bailey
- **Due:** 2022-05-30
- **Notes:** Invoice details for Gait-Golding Kommetjie and Fulham - ECW260 AP, gate station kit, RFID card reader.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2022-05-30

### ✅ Plan
- **Assignee:** Darren Swanepoel
- **Due:** 2022-05-30

### ✅ Calendars
- **Assignee:** Stafford
- **Due:** 2022-05-27

### ✅ Feedback on catchup
- **Assignee:** Amanda
- **Due:** 2022-05-30
- **Notes:** Did you get value from the catchup? What worked? What would you add? Any other ideas?

### ✅ Feedback
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** Got value - brought out positivity. Would add going around table to check in on everyone, and individual calls for those who might not want to say if ok.

### ✅ Smoking around the car/site - be invisible
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Dear training with Mands while guys drop jackets
- **Assignee:** Stafford
- **Due:** 2022-05-26

### ✅ Find out about Ruckus
- **Assignee:** Unassigned
- **Due:** 2023-03-31

### ✅ Please arrange delivery of the jackets to Skytech Branding
- **Assignee:** Amanda
- **Due:** 2022-06-06

### ✅ Add a profile picture in Asana
- **Assignee:** Unassigned
- **Due:** 2022-06-08

### ✅ Do team coffee/chow enroute back from VDV
- **Assignee:** Stafford
- **Due:** 2022-05-26

### ✅ invoice 101 Boulder Apartments - Chateau Chez Property Management
- **Assignee:** Caren Bailey
- **Due:** 2022-05-27
- **Notes:** Router Installation, 1 Hour programming - Reyee RG-EW1800GX R975 ex, delivery R300, programming R900.

### ✅ Setup virtual meeting with Technolutions
- **Assignee:** Unassigned
- **Due:** 2022-05-25

### ✅ Email Peter fibre options (301 Boulders)
- **Assignee:** Unassigned
- **Due:** 2022-05-25

### ✅ Test
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ New fibre clients
- **Assignee:** Caren Bailey
- **Due:** 2022-06-09

### ✅ Find sa distributor for Ruckus
- **Assignee:** Caren Bailey
- **Due:** 2023-03-31

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-05-23

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2022-06-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2022-07-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2022-08-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2022-09-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2022-10-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2022-11-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2022-12-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-01-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-02-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-03-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-04-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-05-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-06-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-07-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-08-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-09-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-10-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-11-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2023-12-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** 2024-01-01

### ✅ Tracker business mileage
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Invoice Penwarden
- **Assignee:** Caren Bailey
- **Due:** 2022-05-20

### ✅ Chat to Ghalieb re credit limit.
- **Assignee:** Caren Bailey
- **Due:** 2022-05-19

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-05-19

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Office
- **Assignee:** Caren Bailey
- **Due:** 2022-05-17

### ✅ Takealot invoices
- **Assignee:** Caren Bailey
- **Due:** 2022-05-16

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Reschedule checking cctv app-Swans
- **Assignee:** Unassigned
- **Due:** None

### ✅ Integrator
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Any response from your mate at Regal re the new position at D1?

### ✅ SnapShot May
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** Topline view / snapshot with two scenarios - worst and best.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-05-12

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-05-12

### ✅ Import the items from the new quote template in the tab (Imports)
- **Assignee:** Amanda
- **Due:** 2022-05-11
- **Notes:** Delete this tab once completed

### ✅ Add new Asana profile pic that is not sideways
- **Assignee:** Unassigned
- **Due:** 2022-05-13

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-05-09

### ✅ Update quote template
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ RRP - CODES DID NOT PULL RRP EXVAT into the system. Update Please
- **Assignee:** Caren Bailey
- **Due:** 2022-05-10
- **Notes:** List of EWS/RKA/SKA/PA product codes needing RRP ex VAT update.

### ✅ Fibre report
- **Assignee:** Caren Bailey
- **Due:** 2022-05-05
- **Notes:** Spreadsheet showing fibre accounts with percentages, file in iCloud/Accounts/Reporting/Fibre.

### ✅ Fibre report
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Spreadsheet showing fibre accounts with percentages, file in iCloud/Accounts/Reporting/Fibre.

### ✅ Vat Control Acc-
- **Assignee:** Amanda
- **Due:** 2022-05-09

### ✅ Soundlab 4 core speaker cable
- **Assignee:** Caren Bailey
- **Due:** 2022-05-05

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Update Tristan harvest email
- **Assignee:** Darren Swanepoel
- **Due:** 2022-05-03

### ✅ Tristan to monitor conduit progress on sites?
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** Consider having Tristan assess all sites monthly with the conduit schedule to make sure every point is in before cabling.

### ✅ Sign boards
- **Assignee:** Stafford
- **Due:** 2022-05-03

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Caddy clean up
- **Assignee:** Stafford
- **Due:** 2022-04-29

### ✅ Staff Uniform
- **Assignee:** Caren Bailey
- **Due:** 2022-05-24
- **Notes:** Find a jacket and jeans and caps, get approval.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** 2022-04-25

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-04-25

### ✅ Add these prices to the master prices database
- **Assignee:** Caren Bailey
- **Due:** 2022-04-21

### ✅ Add these prices to the master prices database
- **Assignee:** Darren Swanepoel
- **Due:** 2022-04-22

### ✅ Review financials
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-04-19

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-04-19

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ See new settings in Harvest
- **Assignee:** Stafford
- **Due:** 2022-04-29
- **Notes:** Now setup as a MANAGER in Harvest, able to manage Benji, Flash and Tristan - ensure they report properly.

### ✅ Financial forecast
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Money IN
- **Assignee:** Caren Bailey
- **Due:** 2022-04-22
- **Notes:** All customers whose money should be in by the 25th, focus Tuesday, feedback Wednesday.

### ✅ Update pricelist database details attached
- **Assignee:** Caren Bailey
- **Due:** 2022-04-21
- **Notes:** Retail inc prices.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-04-14

### ✅ Review projects for claiming
- **Assignee:** Amanda
- **Due:** 2022-04-14
- **Notes:** Run through % claimed per Base project to try to claim more from the QS's.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-04-14

### ✅ Put Pipeline info onto whiteboard
- **Assignee:** Darren Swanepoel
- **Due:** 2022-04-20

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Complete Pricelist database to Mands
- **Assignee:** Darren Swanepoel
- **Due:** 2022-04-18

### ✅ Create master pricelist
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Get invoicing details from Damian for PV clubhouse
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Get latest pricelists into pricelist folder, including ELAN
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Tech meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-04-11

### ✅ Find a course physical or online for the team to learn high level rack pre-building and wiring
- **Assignee:** Stafford
- **Due:** None

### ✅ Snapshot to Darren
- **Assignee:** Amanda
- **Due:** 2022-04-07
- **Notes:** Debtors summary and detail, creditors summary and detail, bank, uninvoiced SOs, projects total quoted/paid/outstanding.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Update labour rates in DEAR
- **Assignee:** Caren Bailey
- **Due:** 2022-04-08
- **Notes:** Only options when quoting: Installation R700, Installation R3950, Programming R900, Design and Project management R900, Design R900.

### ✅ Update Pricing on Quote template, and update labour fees too
- **Assignee:** Caren Bailey
- **Due:** 2022-04-07

### ✅ Ask Karen to find a camper van / 4x4 to rent for 27 April to 2 May
- **Assignee:** Amanda
- **Due:** None

### ✅ Forward Digicape invoice
- **Assignee:** Caren Bailey
- **Due:** 2022-04-05
- **Notes:** Email invoice for the iPad from Digicape.

### ✅ Fix sales in DEAR to export into .CSV instead of .txt
- **Assignee:** Amanda
- **Due:** 2022-04-06

### ✅ Picking stock- 12557-DESVAUX
- **Assignee:** Unassigned
- **Due:** 2022-04-04

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-04-04

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-04-04

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-04-04

### ✅ Get package from me
- **Assignee:** Stafford
- **Due:** 2022-03-29

### ✅ Ask for lens
- **Assignee:** Unassigned
- **Due:** 2022-03-29

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-03-28

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-03-28

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Settle Homemation account
- **Assignee:** Amanda
- **Due:** 2022-03-28

### ✅ Setup Tristan's calendar
- **Assignee:** Stafford
- **Due:** 2022-03-25

### ✅ Reporting Creditors
- **Assignee:** Darren Swanepoel
- **Due:** 2022-03-24

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-03-24

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-03-24

### ✅ Oudekraal fix internet pole
- **Assignee:** Unassigned
- **Due:** 2022-03-23
- **Notes:** Complete

### ✅ Figure out sales bundles
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-03-22

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-03-22

### ✅ Approve marketing
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Ekdahl alarm notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Stafford buying old office CCTV system for R350 from the store. Please deduct from salary
- **Assignee:** Amanda
- **Due:** 2022-03-25

### ✅ Update pricelists folder with current pricelists
- **Assignee:** Caren Bailey
- **Due:** 2022-03-29

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-03-17

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-03-17

### ✅ Book out
- **Assignee:** Caren Bailey
- **Due:** 2022-03-16

### ✅ Spreadsheet for Homemation
- **Assignee:** Darren Swanepoel
- **Due:** 2022-03-18
- **Notes:** Indicate which invoices relate to which projects from their statement, so we can see what we owe from which project.

### ✅ Legalese payment
- **Assignee:** Caren Bailey
- **Due:** 2022-03-18
- **Notes:** Have they paid? Xero says they still owe us money.

### ✅ Get Linde payment resolved
- **Assignee:** Amanda
- **Due:** 2022-03-18

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-03-14

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-03-14

### ✅ Darren's keys/remotes
- **Assignee:** Stafford
- **Due:** 2022-03-16

### ✅ Phillip Linde payment
- **Assignee:** Caren Bailey
- **Due:** 2022-03-11

### ✅ Agenda for Thursday
- **Assignee:** Caren Bailey
- **Due:** 2022-03-10

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-03-07

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-03-07

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Get quote and design for branding the Audi's in Matt black from graffitti
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-03-03

### ✅ Reports for today
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Income statements for last 2 years, current balance sheet, sales/GP/expenses breakdown, personal expenses through business, 5-year sales history.

### ✅ R2M overdue in Xero, we have to resolve this
- **Assignee:** Darren Swanepoel
- **Due:** 2022-03-03

### ✅ Cash in
- **Assignee:** Darren Swanepoel
- **Due:** 2022-03-03

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-03-03

### ✅ Pay Camp Canoe
- **Assignee:** Amanda
- **Due:** 2022-03-02

### ✅ Create an Asana account for Kemp
- **Assignee:** Caren Bailey
- **Due:** 2022-03-01

### ✅ Sort tyre. Can't run on the biscuit
- **Assignee:** Unassigned
- **Due:** None

### ✅ Proposal for fibre
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-02-28

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-02-28

### ✅ Kemp details
- **Assignee:** Unassigned
- **Due:** None

### ✅ Add project labour budgets into Harvest
- **Assignee:** Caren Bailey
- **Due:** 2022-03-02

### ✅ Load Flash into Harvest and Tristan
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-02-24

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Pay camp Canoe
- **Assignee:** Amanda
- **Due:** 2022-02-23

### ✅ Quote Graeme Kemp Intercom System
- **Assignee:** Caren Bailey
- **Due:** 2022-02-22

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-02-21

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-02-21

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Arrange courier for passport collection
- **Assignee:** Caren Bailey
- **Due:** 2022-02-22

### ✅ Send contract with payment details to Tristan
- **Assignee:** Amanda
- **Due:** 2022-02-22

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-02-14

### ✅ General notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-02-14

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Email to Caleb's other email address.
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Money IN
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** Please confirm that this money due is accurate.

### ✅ Invoice Tertius and Graham Kemp
- **Assignee:** Unassigned
- **Due:** 2022-02-14

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-02-07

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-02-07

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2022-02-03

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-02-03

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-02-03

### ✅ Staff training.
- **Assignee:** Stafford
- **Due:** None

### ✅ Pricing added to DEAR
- **Assignee:** Caren Bailey
- **Due:** 2022-02-11
- **Notes:** All products used need prices added in DEAR so quoting pulls current pricing - Homemation, SENSOR, Spectrum, Planetworld, SAVANT, Space TV, Scoop, Regal.

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-01-31

### ✅ Get latest pricelists from suppliers and update Pricelists folder
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Score out of 10 for Asana and calendar adoption in 2022
- **Assignee:** Unassigned
- **Due:** 2022-01-28

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-01-27

### ✅ Ensure all POs are done, even if not ordered
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Setup design meeting
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Lock a date in, do this virtually, next week is good.

### ✅ General notes
- **Assignee:** Stafford
- **Due:** 2022-01-24

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Keep a log of Caleb's time and whether he is contributing value
- **Assignee:** Stafford
- **Due:** None
- **Notes:** Track whether adding value to D-One, and how many hours.

### ✅ Invite Caleb to design meeting for Feb
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2022-01-17

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-01-17

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Setup Harvest for Tristan
- **Assignee:** Caren Bailey
- **Due:** 2022-01-27

### ✅ Tristan calendar setup and sharing
- **Assignee:** Darren Swanepoel
- **Due:** 2022-01-26

### ✅ Find other piece of desk with mounting bracket for office desk
- **Assignee:** Unassigned
- **Due:** 2022-01-21
- **Notes:** In the store

### ✅ Should we be logging work mileage on the work mileage? Would it affect tax any way?
- **Assignee:** Amanda
- **Due:** 2022-01-14

### ✅ Setup design handover meeting for early Feb
- **Assignee:** Unassigned
- **Due:** None

### ✅ Appraisal notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Lease agreement
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ By Benji Mouse for tool bag
- **Assignee:** Stafford
- **Due:** 2022-01-17

### ✅ Load new projects and budgets into Asana
- **Assignee:** Caren Bailey
- **Due:** 2022-01-31

### ✅ Clean rugs for office
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Make sure all orders invoices in Dec are processed. Prices are going up across the board
- **Assignee:** Caren Bailey
- **Due:** 2022-01-14

### ✅ Collect D1 clothes from Anton when in the Sea Point area
- **Assignee:** Unassigned
- **Due:** 2022-02-11
- **Notes:** Gave him D1 clothes that didn't fit, arrange collection once his covid is finished.

### ✅ Add a photo to your Asana profile, and add your name if possible
- **Assignee:** Unassigned
- **Due:** 2022-01-21

### ✅ Plan appraisals and goals KPIs
- **Assignee:** Darren Swanepoel
- **Due:** 2022-01-10

### ✅ Appraisals Saturday?
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2022-01-10

### ✅ Deliver 2 full desks (pics attached) to Office next to heyday
- **Assignee:** Stafford
- **Due:** 2022-01-14
- **Notes:** Key for office is with HeyDay reception.

### ✅ Do some 5 tutorials on Asana
- **Assignee:** Unassigned
- **Due:** 2022-01-14

### ✅ Clyde to do training
- **Assignee:** Unassigned
- **Due:** None

### ✅ Remotely Activate Heyday: activate WAN2 port on USG - 3G router is connected
- **Assignee:** Darren Swanepoel
- **Due:** 2022-01-14

### ✅ Cancel Sales subscription on LinkedIn
- **Assignee:** Darren Swanepoel
- **Due:** 2022-01-18

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Reschedule appraisals
- **Assignee:** Darren Swanepoel
- **Due:** 2022-01-06

### ✅ Add commission and finders fee Annexure to staff contracts
- **Assignee:** Amanda
- **Due:** 2022-01-21

### ✅ Process for call-out billing
- **Assignee:** Unassigned
- **Due:** None

### ✅ Get pricing for a retreat for Elevation Barn (I'm helping them set it up)
- **Assignee:** Darren Swanepoel
- **Due:** 2021-12-15
- **Notes:** 4 day retreat for 6 participants including catering, 21-24 January 2022, at Boschendal mountain villa.

### ✅ Never order RG6. We have LOADS
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-12-13

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-12-13

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Can we use service section for services? Amanda in DEAR
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Load the template attached into DEAR
- **Assignee:** Caren Bailey
- **Due:** 2021-12-09

### ✅ Order tick lists for Mel
- **Assignee:** Darren Swanepoel
- **Due:** 2021-12-09

### ✅ New site GSquared
- **Assignee:** Darren Swanepoel
- **Due:** 2021-12-08
- **Notes:** 20 Kinnoull Rd, Builder: Unser, Architect: gsquared architects.

### ✅ Update numbers template
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Pay Tristan R7k for the month Nov-Dec
- **Assignee:** Amanda
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-12-06

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ DEAR integration
- **Assignee:** Amanda
- **Due:** 2021-12-16
- **Notes:** Setup DEAR so we can use it as our Sales process.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-12-02

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Make a key plan. The store keys are in your top drawer. And the office key in Yolanda's office
- **Assignee:** Caren Bailey
- **Due:** 2021-11-30

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-11-29

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-11-29

### ✅ Check harvest
- **Assignee:** Unassigned
- **Due:** None

### ✅ Confirm which address is Darrens69 and update name on Afrihost site
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Find out what the address is at Darrens44 on Afrihost
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-11-25

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Put darren in contact with Navavi
- **Assignee:** Unassigned
- **Due:** 2021-11-22

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-11-22

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-11-22

### ✅ Drop stock and Lutron at homemation
- **Assignee:** Stafford
- **Due:** 2021-11-19

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-11-18

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-11-15

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-11-15

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-11-11

### ✅ Pay Amy for Wolfie
- **Assignee:** Amanda
- **Due:** 2021-11-10
- **Notes:** R3875, Standard Bank, AR Kropman.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-11-08

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-11-08

### ✅ Accounts Meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Increase services dayrate
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-11-02

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-11-02

### ✅ Staff Financial management course (Justin)
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Calculate Benji Cost to Company and break it down
- **Assignee:** Amanda
- **Due:** 2021-11-11

### ✅ Homemation
- **Assignee:** Caren Bailey
- **Due:** 2021-10-28

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-10-28

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-10-28

### ✅ Snap One software
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Accept family sharing link from iCloud
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Accept family sharing link from iCloud
- **Assignee:** Unassigned
- **Due:** None

### ✅ Return Macbook to Darren's house
- **Assignee:** Unassigned
- **Due:** 2021-10-30
- **Notes:** Doesn't make sense to sell, will need it for Presales member that joins D-One.

### ✅ Investigate family sharing privacy
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-10-25

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-10-25

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-10-21

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-10-21

### ✅ Invoice Dani for one of the phones at cost price
- **Assignee:** Caren Bailey
- **Due:** 2021-10-26

### ✅ Send Digicape invoice to Lorraine
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-10-18

### ✅ Meeting notes.
- **Assignee:** Stafford
- **Due:** 2021-10-18

### ✅ Digicape order
- **Assignee:** Caren Bailey
- **Due:** 2021-10-18
- **Notes:** Place order with Digicape, get discount. 2x iPhones.

### ✅ Letterhead giving Mel proxy for C-Track
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Overtime document
- **Assignee:** Amanda
- **Due:** 2021-10-19
- **Notes:** Explain salary ranges with/without overtime, reference Employment act, bonus criteria for roles without overtime pay.

### ✅ iCloud space issue for team
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-10-14

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-10-14

### ✅ Talk to C-track and tell them that the Fortuner reg: D ONE WP has been sold
- **Assignee:** Caren Bailey
- **Due:** 2021-10-25
- **Notes:** Car sold to Audi Century City, find out procedure for new car purchase and cancellation policy.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-10-11

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-10-11

### ✅ Accounts meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Fibre report - go through all ins and outs with each client
- **Assignee:** Caren Bailey
- **Due:** 2021-11-18

### ✅ Next shipment eta to Eitan
- **Assignee:** Caren Bailey
- **Due:** 2021-10-06

### ✅ Data sim cards
- **Assignee:** Caren Bailey
- **Due:** 2021-10-08
- **Notes:** Research Vodacom/MTN/Rain/Telkom/Cell-C for non-expiring data sim cards, need 3, report options in Asana.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-10-04

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-10-04

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Where is fuel accounted for in Xero?
- **Assignee:** Amanda
- **Due:** None
- **Notes:** On the P&L it hasn't been recorded under fuel for the last year or two.

### ✅ Invoice Stafford
- **Assignee:** Caren Bailey
- **Due:** 2021-10-04

### ✅ Design Meeting
- **Assignee:** Unassigned
- **Due:** 2021-11-30

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-09-30

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-09-30

### ✅ Setup a dealership with Sony
- **Assignee:** Caren Bailey
- **Due:** 2021-10-01
- **Notes:** Sony 4K home cinema projectors dealership.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-09-20

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Tasks for stock to Mel. Talk to Benji.
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-09-16

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-09-16

### ✅ Accounts meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2021-09-16

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ WAPS for Brad
- **Assignee:** Caren Bailey
- **Due:** 2021-09-16
- **Notes:** Order 2x UAP-AC-LR from Scoop, delivery to North Oaks Estate Hout Bay for Brad Morgan, no invoicing needed.

### ✅ Do we have 2x UPA-AC-LR in stock?
- **Assignee:** Caren Bailey
- **Due:** 2021-09-14

### ✅ Ask darren whiskey
- **Assignee:** Unassigned
- **Due:** 2021-09-13

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-09-13

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-09-13

### ✅ IRs
- **Assignee:** Caren Bailey
- **Due:** 2021-09-09

### ✅ Polish D1 profile.
- **Assignee:** Unassigned
- **Due:** 2021-09-07
- **Notes:** Make sure all headings have same coordinates for consistency, size all pics to fit the page.

### ✅ Business cards / updated company profile
- **Assignee:** Darren Swanepoel
- **Due:** 2021-09-07

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-09-06

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Unregister Darren as a shareholder of Summore Engine room pty Ltd
- **Assignee:** Caren Bailey
- **Due:** 2021-09-11
- **Notes:** Contact CIPC to find out what's needed to remove from this company that never launched.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-09-02

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-09-02

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-08-30

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2021-08-30

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-08-26

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-08-26

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2021-08-26

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-08-23

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2021-08-23

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-08-19

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-08-19

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-08-12

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** What changes need to be made? Document here.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-08-10

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-08-10

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-08-05

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-08-05

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Pay PAYE to SARS. Apparently it's late.
- **Assignee:** Amanda
- **Due:** 2021-08-02

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-08-02

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-08-02

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-07-26

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-07-26

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-07-22

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-07-22

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-07-19

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-07-19

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Sick leave
- **Assignee:** Caren Bailey
- **Due:** 2021-07-13

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-07-12

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-07-12

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Review bank accounts in meeting to select account type for deposits
- **Assignee:** Caren Bailey
- **Due:** 2021-07-15

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-07-08

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Invoice Spinazze
- **Assignee:** Caren Bailey
- **Due:** 2021-07-09

### ✅ Deposits, accounts, PO report
- **Assignee:** Caren Bailey
- **Due:** 2021-07-13
- **Notes:** Report on projects, what's deposited and stored separately in the deposit account.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-07-05

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-07-01

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-07-01

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Let me know if yoga ball is at the office
- **Assignee:** Caren Bailey
- **Due:** 2021-07-02

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-06-28

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-06-28

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-06-24

### ✅ Nexus status
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** What has happened with the discount?

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-06-21

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-06-14

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-06-14

### ✅ Finance
- **Assignee:** Amanda
- **Due:** None

### ✅ Caddy license & polo
- **Assignee:** Amanda
- **Due:** 2021-06-11

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Ask a surf shop for a quote for a new surfboard
- **Assignee:** Caren Bailey
- **Due:** 2021-06-08
- **Notes:** 6.0 squash tail thruster surfboard quote for insurance claim - Lifestyle, KISS or Billabong surf shop.

### ✅ meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-06-07

### ✅ send final invoice
- **Assignee:** Caren Bailey
- **Due:** 2021-06-07
- **Notes:** Final invoice for Graeme Kemp, both CCTV and Network completed.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-06-07

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2021-06-07

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-06-03

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-06-03

### ✅ Confirm of Josh has been Paid
- **Assignee:** Amanda
- **Due:** 2021-06-02

### ✅ Courses on Homemation portal
- **Assignee:** Unassigned
- **Due:** 2021-06-04

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-05-31

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-05-31

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Demo Unifi ui design for cctv designs and access point deployment
- **Assignee:** Unassigned
- **Due:** 2021-05-28
- **Notes:** New software released by ubiquiti.

### ✅ Call Graeme kemp to schedule
- **Assignee:** Unassigned
- **Due:** 2021-05-27

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** None

### ✅ Setup a suppliers contacts list in Asana
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Subtask per supplier with contact name and details, products in description field.

### ✅ Sound united sign up
- **Assignee:** Unassigned
- **Due:** None

### ✅ Tashwell overtime
- **Assignee:** Amanda
- **Due:** 2021-05-24
- **Notes:** 8 hours overtime for 2 Saturdays at Desvaux.

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-05-24

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Setup Voip extensions for Stafford, Benji and Josh's phones
- **Assignee:** Caren Bailey
- **Due:** 2021-05-24

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-05-20

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-05-20

### ✅ Schedule virtual sales training time with Kevin for Savant
- **Assignee:** Unassigned
- **Due:** 2021-05-20
- **Notes:** Kevin to bring the team up to speed on Savant products.

### ✅ Integrate Hubspot into Gmail
- **Assignee:** Unassigned
- **Due:** 2021-05-19

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-05-17

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-05-17

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Proposing R600 per month cell phone allowance and fibre at home
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** R604 for fibre, needs support, 50-50.

### ✅ Quote Accusense Cameras for Graeme
- **Assignee:** Unassigned
- **Due:** 2021-05-13

### ✅ Send leave form for eid
- **Assignee:** Unassigned
- **Due:** 2021-05-13

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-05-13

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-05-13

### ✅ Invoice Graeme Kemp
- **Assignee:** Caren Bailey
- **Due:** 2021-05-14

### ✅ Create email signature for Joshua Bridge - Business developer
- **Assignee:** Amanda
- **Due:** 2021-05-14

### ✅ Update fibre billing in Xero
- **Assignee:** Caren Bailey
- **Due:** 2021-05-13

### ✅ Go through Homemation account. Apparently we're behind
- **Assignee:** Caren Bailey
- **Due:** 2021-05-13
- **Notes:** Go through together at Val de Vie.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Graeme kemp dstv
- **Assignee:** Stafford
- **Due:** 2021-05-12
- **Notes:** Wind blown dish out of alignment, stop and assess at Graeme's place.

### ✅ Setup meeting for site files
- **Assignee:** Unassigned
- **Due:** 2021-05-10

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-05-10

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-05-10

### ✅ Clean up accounts
- **Assignee:** Darren Swanepoel
- **Due:** 2021-05-20

### ✅ New Accounting Flow
- **Assignee:** Amanda
- **Due:** None
- **Notes:** No invoice raised on deposit/main invoice, all SO/VO/PO raised in Dear/Xero not Numbers, combine bank accounts, split money 60/40 into relevant accounts once received.

### ✅ Search Val De Vie for fun activity for Team Building
- **Assignee:** Caren Bailey
- **Due:** 2021-05-07

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-05-06

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-05-06

### ✅ Contact TSTEC
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Google drive full or half way - ask TSTEC to confirm actual status.

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-05-03

### ✅ meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-05-03

### ✅ Accounts Payable
- **Assignee:** Caren Bailey
- **Due:** 2021-04-30

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-04-29

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-04-29

### ✅ Invoice client
- **Assignee:** Caren Bailey
- **Due:** 2021-05-03
- **Notes:** Installation 1hr, programming 1hr, invoice per quotation.

### ✅ Scott and partners Sonos
- **Assignee:** Unassigned
- **Due:** 2021-04-29

### ✅ Process quotation for Greame kemp as discussed
- **Assignee:** Caren Bailey
- **Due:** 2021-04-28

### ✅ Update scorecard for sales role
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Gain on sonnace power amp
- **Assignee:** Darren Swanepoel
- **Due:** 2021-04-30

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-04-26

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-04-26

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-04-22

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-04-22

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2021-04-22

### ✅ Look into design courses
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** CEDIA ESC-D certification.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-04-19

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-04-19

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-04-15

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-04-15

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-04-12

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2021-04-12

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-04-12

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** 2021-04-08

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-04-08

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-04-06

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Pay staff their additional 5%
- **Assignee:** Amanda
- **Due:** 2021-04-01

### ✅ Stock purchased from Sensor
- **Assignee:** Unassigned
- **Due:** 2021-04-01
- **Notes:** Outstanding order for Alpha One - allocate as cabcon or invoice as stock items.

### ✅ Accounts Payable
- **Assignee:** Caren Bailey
- **Due:** 2021-03-31

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-03-29

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-04-06

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Review fibre spreadsheet
- **Assignee:** Caren Bailey
- **Due:** 2021-04-29
- **Notes:** Check and make sure each account is making a profit.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-03-25

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-03-25

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Get accounting system up to date
- **Assignee:** Amanda
- **Due:** 2021-03-31
- **Notes:** New financial year - get accounts up to date, check reporting for duplications/errors, present end of March.

### ✅ Create logins for regal website
- **Assignee:** Unassigned
- **Due:** 2021-03-18

### ✅ Discuss OPEX and salaries
- **Assignee:** Amanda
- **Due:** 2021-03-18

### ✅ Meeting Notes
- **Assignee:** Stafford
- **Due:** 2021-03-18

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-03-18

### ✅ Another option for technical drawings. AVP uses this one.
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Reddit homelab diagram example - compare to xDiagram.

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-03-15

### ✅ Meeting notes 15/03/2021
- **Assignee:** Stafford
- **Due:** 2021-03-15

### ✅ Review salaries
- **Assignee:** Amanda
- **Due:** 2021-03-19

### ✅ Fibre spreadsheet
- **Assignee:** Caren Bailey
- **Due:** 2021-04-16
- **Notes:** Added missing apartments discussed with Rob, ensure invoicing and sheet are aligned 100%.

### ✅ Meeting notes
- **Assignee:** Unassigned
- **Due:** 2021-03-11

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-03-11

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-03-08

### ✅ Meeting prep
- **Assignee:** Stafford
- **Due:** 2021-03-08

### ✅ Meeting Prep
- **Assignee:** Darren Swanepoel
- **Due:** 2021-03-08

### ✅ Meeting notes
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-03-04

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-03-04

### ✅ Create a recurring task for the tech meetings, so that you don't have to set up one by one
- **Assignee:** Stafford
- **Due:** 2021-03-05

### ✅ Meeting notes.
- **Assignee:** Stafford
- **Due:** 2021-03-01

### ✅ Do you get the leave application forms on email?
- **Assignee:** Caren Bailey
- **Due:** 2021-02-26
- **Notes:** Tashwell filled one out, didn't receive it, checking if forms route elsewhere.

### ✅ Accounts Payable
- **Assignee:** Caren Bailey
- **Due:** 2021-02-26

### ✅ Purchase new routers for dalvin
- **Assignee:** Unassigned
- **Due:** 2021-02-25

### ✅ Meeting notes
- **Assignee:** Stafford
- **Due:** 2021-02-25

### ✅ Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-02-25

### ✅ Senior Technician
- **Assignee:** Unassigned
- **Due:** None

### ✅ Andrews rd Fibre. Conduit is in. And Openserve can pull their fibre through now.
- **Assignee:** Unassigned
- **Due:** 2021-02-23

### ✅ Slips into Xero directly email
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Numbers tutorials
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Master Mac Numbers for this quarter.

### ✅ Numbers tutorials
- **Assignee:** Stafford
- **Due:** None
- **Notes:** Master Mac numbers for this quarter.

### ✅ Update roles for all
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Desvaux doors
- **Assignee:** Unassigned
- **Due:** None

### ✅ Tech meeting
- **Assignee:** Unassigned
- **Due:** 2021-02-18

### ✅ Increase SLA rates
- **Assignee:** Darren Swanepoel
- **Due:** 2021-02-16

### ✅ Schedule training with Matthew from Lutron
- **Assignee:** Unassigned
- **Due:** 2021-03-03

### ✅ New build in camps bay ingleside rd
- **Assignee:** Unassigned
- **Due:** 2021-02-19

### ✅ Monday meeting
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Monday meeting
- **Assignee:** Stafford
- **Due:** None

### ✅ Tech Meeting Notes
- **Assignee:** Unassigned
- **Due:** 2021-02-11

### ✅ Arrange 1 extra set of keys cut for the upstairs office.
- **Assignee:** Unassigned
- **Due:** None

### ✅ Confirm AJAX demo for Monday 11am
- **Assignee:** Unassigned
- **Due:** 2021-02-03

### ✅ Run quarterly appraisal for Tashwell using the same format I use.
- **Assignee:** Stafford
- **Due:** 2021-03-01
- **Notes:** KPI rating out of 10 for each role.

### ✅ False alarms
- **Assignee:** Unassigned
- **Due:** None

### ✅ Davlin Office internet from nexus
- **Assignee:** Unassigned
- **Due:** 2021-02-12

### ✅ Setup calendar tech meetings for Mondays and Thursdays
- **Assignee:** Stafford
- **Due:** 2021-01-15

### ✅ Make Acusense work at Penzance with Pieter
- **Assignee:** Unassigned
- **Due:** 2021-01-29

### ✅ Over PMTS
- **Assignee:** Caren Bailey
- **Due:** 2021-01-14
- **Notes:** Savant and Radionics accounts in negative, ask HM for updated statement, should have 1.4M in cr with them.

### ✅ Setup meeting Rythm in calendars
- **Assignee:** Darren Swanepoel
- **Due:** 2021-01-13

### ✅ HARVEST tracking for the week.
- **Assignee:** Unassigned
- **Due:** 2021-01-15

### ✅ HARVEST tracking for end Dec and Jan
- **Assignee:** Stafford
- **Due:** 2021-01-13

### ✅ Accounts Payable
- **Assignee:** Caren Bailey
- **Due:** 2021-01-15

### ✅ Update fibre income vs expense spreadsheet and review in meeting
- **Assignee:** Caren Bailey
- **Due:** 2021-01-14

### ✅ Check Harvest
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ PO Report
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Purchase report condensed to show PO numbers and site.

### ✅ Decide how to deal with deposits
- **Assignee:** Darren Swanepoel
- **Due:** 2021-01-15

### ✅ Provident Fund
- **Assignee:** Amanda
- **Due:** 2021-01-15

### ✅ Site file template
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** Get all projects site folders consistent.

### ✅ Complete leave forms
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Remember to complete December leave dates on the leave forms and simple pay link.

### ✅ Complete leave forms
- **Assignee:** Stafford
- **Due:** 2021-01-11
- **Notes:** Remember to complete December leave dates on the leave forms and simple pay link.

### ✅ Personal calendar
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Billing Clients
- **Assignee:** Caren Bailey
- **Due:** 2020-12-18
- **Notes:** Pushing to get as much money in before year-end - flag any invoiceable jobs (snags, service calls, maintenance not part of SLA).

### ✅ Filing to Maitland
- **Assignee:** Stafford
- **Due:** 2020-12-07
- **Notes:** Filing Cabinet

### ✅ Get the polo branded properly at Grafitti
- **Assignee:** Caren Bailey
- **Due:** 2021-02-15
- **Notes:** Chat to Graffiti for a quote on branding the Polo with D-One branding, give them logos from marketing folder.

### ✅ Accounts Payable
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Talk to Benji about instructions.
- **Assignee:** Darren Swanepoel
- **Due:** None
- **Notes:** Consider Mel is busy, she is not there to fill your gaps.

### ✅ Assign installation as a service in each project in Harvest
- **Assignee:** Caren Bailey
- **Due:** 2020-11-27

### ✅ Invoice Pinpoint
- **Assignee:** Caren Bailey
- **Due:** 2020-11-27
- **Notes:** UAP configurations, 1 hour programming, invoice for configuring 2 access points for summerseat.

### ✅ Redeem coupon code for Fathom
- **Assignee:** Amanda
- **Due:** 2020-12-02
- **Notes:** D1ZA01

### ✅ Time on Harvest
- **Assignee:** Stafford
- **Due:** 2020-11-29
- **Notes:** Discuss projects not visible on phone - no hours logged since beginning of Nov.

### ✅ Time on Harvest
- **Assignee:** Unassigned
- **Due:** 2020-11-20
- **Notes:** Only 1.50 hours logged Tues 10th and Mon 16th Nov, no hours Friday 13th - confirm correct.

### ✅ Sales/Purchase Reports
- **Assignee:** Amanda
- **Due:** 2020-11-19

### ✅ Apply for TERS if possible
- **Assignee:** Amanda
- **Due:** 2020-11-20

### ✅ Case Number- mini
- **Assignee:** Amanda
- **Due:** 2020-11-17
- **Notes:** Get a case number for the mini.

### ✅ QS Lead
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** Call Zinnia.

### ✅ Keep debtors (Projects) up to date re payments
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Get Sensor to site to demo alarm
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ WiFi in the Workshop
- **Assignee:** Unassigned
- **Due:** None

### ✅ Discuss Nexus Resellers agreement
- **Assignee:** Unassigned
- **Due:** 2020-11-16

### ✅ Unpack Darren's car
- **Assignee:** Unassigned
- **Due:** 2020-11-09

### ✅ Book out D250L amplifier and invoice it to Dale for R2k incl VAT
- **Assignee:** Caren Bailey
- **Due:** 2020-11-02

### ✅ Organize hand soap for bathrooms at office
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ All keys to Vaughn
- **Assignee:** Caren Bailey
- **Due:** 2020-11-05

### ✅ Cancel scheduled transfer
- **Assignee:** Unassigned
- **Due:** None

### ✅ Confirm if stock was collected.
- **Assignee:** Unassigned
- **Due:** 2020-10-29
- **Notes:** Confirm what invoice 3390 is for.

### ✅ Accounts Payable
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Go through sales comm with team and sign
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Connectwise
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Send Johann password details for D1 garage CCTV system
- **Assignee:** Stafford
- **Due:** 2020-10-27

### ✅ Create a table indicating all fibre speeds and connections
- **Assignee:** Unassigned
- **Due:** 2020-11-16
- **Notes:** Table of active fibre connections: Client, Address, ISP, Speed, Fee.

### ✅ Police report for mini
- **Assignee:** Darren Swanepoel
- **Due:** 2020-10-27

### ✅ Buy a 22/24 monitor for Benji to do designs. Maybe Makro has a deal
- **Assignee:** Amanda
- **Due:** 2020-10-26

### ✅ Confirm if we have a D250L Rising power amp in stock
- **Assignee:** Caren Bailey
- **Due:** 2020-10-23

### ✅ D-One Office
- **Assignee:** Stafford
- **Due:** 2021-01-11

### ✅ CA21-2 Book out for Dani and Dale
- **Assignee:** Caren Bailey
- **Due:** 2020-10-30

### ✅ Deep Blue Franshoek
- **Assignee:** Darren Swanepoel
- **Due:** 2020-10-15

### ✅ See if we can return the pucks and NEEO on general to Homemation
- **Assignee:** Caren Bailey
- **Due:** 2020-10-30
- **Notes:** Send Bryan serial numbers, if already packed can do it from Maitland.

### ✅ Create spreadsheet with the info that is on the whiteboard. So we can see it when not in the office
- **Assignee:** Caren Bailey
- **Due:** 2020-10-22

### ✅ Please allocate cabling to house Swanepoel
- **Assignee:** Caren Bailey
- **Due:** 2020-10-15

### ✅ Consolidate James in Harvest and create correct clients
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ Call VJ
- **Assignee:** Stafford
- **Due:** None

### ✅ Make sure Harvest is up to date
- **Assignee:** Unassigned
- **Due:** 2020-10-12

### ✅ Make a We're moving sign for the office window
- **Assignee:** Caren Bailey
- **Due:** 2020-10-12

### ✅ Change all fibre invoices to say SLA. None of them can say Fibre.
- **Assignee:** Caren Bailey
- **Due:** 2020-10-12

### ✅ Find out if Legrande netatmo has an open API for integration into Savant
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** Contact Legrande Europe technical.

### ✅ Give office garage cameras to Pin Point to install for Andre van Heldsingen
- **Assignee:** Stafford
- **Due:** 2020-10-09

### ✅ Insurance for the move
- **Assignee:** Amanda
- **Due:** 2020-10-09
- **Notes:** Make sure covered to move stock to Maitland for full value.

### ✅ Chat to me about sensor cameras. Spoke to the alarm guy. And they say acusense IS the way to go!
- **Assignee:** Caren Bailey
- **Due:** None
- **Notes:** For Dale and Dani - keep the stock if we have it.

### ✅ Review fathom on Monday
- **Assignee:** Amanda
- **Due:** 2020-10-09

### ✅ Review harvest
- **Assignee:** Caren Bailey
- **Due:** 2020-10-12

### ✅ Box all stock per project for the move.
- **Assignee:** Caren Bailey
- **Due:** 2020-10-16

### ✅ Take logo off the wall
- **Assignee:** Caren Bailey
- **Due:** None

### ✅ New build
- **Assignee:** Caren Bailey
- **Due:** 2020-10-02
- **Notes:** New build against the mountain, worth a shot.

### ✅ Arrange account with Frontosa
- **Assignee:** Caren Bailey
- **Due:** 2020-10-06

### ✅ Accounts Payable
- **Assignee:** Caren Bailey
- **Due:** 2020-09-30

### ✅ Ask Vaughn for a garage
- **Assignee:** Darren Swanepoel
- **Due:** None

### ✅ Call Mark Embroico for lunch app
- **Assignee:** Caren Bailey
- **Due:** 2020-09-21

### ✅ 1M patchleads
- **Assignee:** Caren Bailey
- **Due:** 2020-09-21

### ✅ Add Chelin to Harvest
- **Assignee:** Stafford
- **Due:** 2020-09-21

### ✅ Get toilet paper and Rooibos Tea
- **Assignee:** Caren Bailey
- **Due:** 2020-09-19

### ✅ Check Payfast
- **Assignee:** Caren Bailey
- **Due:** 2020-09-09

### ✅ Arrange payslip for Tashwell. So he can get himself a new phone
- **Assignee:** Amanda
- **Due:** 2020-09-11

### ✅ Setup gmail and Asana for Tashwell
- **Assignee:** Unassigned
- **Due:** None
- **Notes:** technician@d-one.co.za

