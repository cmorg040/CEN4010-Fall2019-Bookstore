import datetime

# to represent each month as their corresponding number
JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12

# to get each month full name and number
MONTHS = (
    (JAN, 'January'),
    (FEB, 'February'),
    (MAR, 'March'),
    (APR, 'April'),
    (MAY, 'May'),
    (JUN, 'June'),
    (JUL, 'July'),
    (AUG, 'August'),
    (SEP, 'September'),
    (OCT, 'October'),
    (NOV, 'November'),
    (DEC, 'December'), )

YEARS = []
CURRENT_YEAR = datetime.datetime.today().year

# create a tuple with the following years, from now to 10 years from now
for y in range(CURRENT_YEAR, CURRENT_YEAR + 11):
    YEARS.append((y,y))