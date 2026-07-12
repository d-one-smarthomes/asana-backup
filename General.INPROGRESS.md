# General (IN PROGRESS -- PARTIAL BACKUP, DO NOT TREAT AS COMPLETE)
**GID:** 905674768180011
**Last updated:** 2026-07-12
**Project total tasks (per Asana):** 3680 (3659 completed, 21 incomplete)
**Tasks captured in this partial backup:** 1700 (1682 completed)

> NOTE FOR FUTURE BACKUP RUNS: This project is too large to fully back up in a
> single automated run (3680 tasks vs ~100/API call). This file is intentionally
> NOT named General.md so the backup job does not mistake it for a completed
> backup and skip General forever.
>
> STATE AS OF 2026-07-12 (this run): 1400/3680 tasks captured (pages 1-14 of
> ~37, 100 tasks/page). Raw fetched pages (name/completed/assignee/due_on/notes,
> 100 tasks each, in Asana's default stable task order) are cached in
> _raw_general/page12.json..page14.json in this repo -- pages 1-11 were NOT
> re-cached this run (they were only walked with opt_fields=name to reach the
> resume offset and their content matches what's already written to this file
> for tasks 1-1100).
>
> TO RESUME: load _raw_general/page14.json and read its top-level "next_offset"
> field -- that is the Asana pagination cursor to pass as `offset` to the next
> get_tasks call (project=905674768180011, opt_fields="name,completed,
> assignee.name,due_on,notes", limit=100). This resumes exactly at task 1401,
> no need to re-walk pages 1-13. For each new page: save the raw JSON to
> _raw_general/page15.json (etc, matching the page number), convert to the
> same markdown format as below and append to this file (NOT General.md),
> update the two "Tasks captured" counts in the header/section title above,
> and commit+push after every page or two. IMPORTANT GIT WORKAROUND: this repo
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

## Tasks captured so far (1700 of 3680 total, 1682 completed)

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

