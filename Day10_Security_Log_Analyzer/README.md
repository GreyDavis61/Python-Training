# Day 10: Mini SOC Log Analyzer

## Scenario

You are the first analyst on shift at a small company. The authentication server
exported its activity to `sample_auth_log.csv`. Your job is to write a Python
program that reviews the log, identifies suspicious behavior, and creates a
short incident report.

Work only with the supplied file. This is a defensive, offline exercise; it
does not connect to or test any real systems.

## What to build

Complete `log_analyzer.py`. It should read the CSV and detect these events:

1. **Brute-force attempt**: the same username and source IP produce at least
   five failed logins within ten minutes.
2. **Password spray**: one source IP produces failed logins for at least four
   different usernames within ten minutes.
3. **Possible account compromise**: a successful login occurs within five
   minutes after at least three failures for the same username and source IP.
4. **Unauthorized administrator login**: an account with the `admin` role logs
   in successfully but is not listed in `approved_admins.txt`.

For every alert, report:

- Alert type
- Time or time range
- Username or usernames
- Source IP
- Severity: Low, Medium, High, or Critical
- One recommended response action

Write the results both to the terminal and to `incident_report.txt`. Include a
final count of alerts by severity.

## Suggested order

### Part 1: Load and inspect

- Read `sample_auth_log.csv` with `csv.DictReader`.
- Store each row as a dictionary in a list.
- Convert each timestamp with `datetime.strptime` so times can be compared.
- Print the number of events loaded.

### Part 2: Write small detection functions

Create one function for each alert type. Pass the events into the function and
return a list of alerts. Avoid putting all detection logic in one large loop.

### Part 3: Handle bad input

Give a useful error message for:

- A missing input file
- A missing CSV column
- An invalid timestamp
- An empty approved-admin file

The program should exit cleanly instead of showing a traceback for these cases.

### Part 4: Produce the report

Sort alerts by time. Give each alert a stable ID such as `ALT-001`. Do not put
passwords or other secrets in the report.

## Known results for the sample data

The completed program should find exactly four alerts:

- One brute-force attempt
- One password spray
- One possible account compromise
- One unauthorized administrator login

Do not hardcode those four records. The same program should work if more rows
are added or the order of the rows changes.

## Security+ review questions

Answer these in a short `analyst_notes.md` file after the program works:

1. Which detections represent indicators of attack, and which represent an
   indicator of compromise?
2. Why can a successful login be more concerning than a failed login?
3. Which control could reduce the brute-force risk: MFA, account lockout,
   least privilege, or some combination?
4. What evidence should an analyst preserve before changing the affected
   account?
5. Name one false-positive explanation for each alert type.

## Stretch goals

Choose one after the base version works:

- Accept the input filename as a command-line argument with `argparse`.
- Export alerts as JSON as well as text.
- Use `ipaddress` to label source addresses as private or public.
- Add tests for the four detection functions.
- Calculate and record the SHA-256 hash of the input log before analyzing it.

## Definition of done

The project is complete when it finds the four expected alerts, handles the
listed input errors cleanly, creates a readable report, and includes answers to
the five review questions.
