from datetime import date
from jdcal import gcal2jd, jd2gcal
now = date.today()
jd = gcal2jd(now.year, now.month, now.day)
gcal = jd2gcal(jd[0], jd[1])
print('Julian Date: {:s}'.format(jd))
print('Julian Date: {:0.1f}'.format(jd[0]+jd[1]))
print('Calendar Date: {:s}'.format(gcal))
