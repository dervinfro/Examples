#%%

# https://pynative.com/python-timestamp/

'''A tz-naive timestamp represents a point in time without any information about the time zone or daylight saving time.
'''
# TZ-NAIVE
# Example of tz-naive timestamp
from datetime import datetime

naive_timestamp = datetime(2023, 8, 9, 12, 0, 0)

'''A tz-aware timestamp, on the other hand, includes information about the time zone it is associated with. 
'''
# %%
# TZ-AWARE
# Example of tz-aware timestamp
import pytz

tz = pytz.timezone('America/New_York')
aware_timestamp = tz.localize(datetime(2023, 8, 9, 12, 0, 0))

# Example of a tz-aware timestamp using the built-in datetime module.
from datetime import datetime, timezone, timedelta

tz1 = timezone(timedelta(hours=-4))  # Create a custom timezone (GMT-4)
aware_timestamp1 = datetime(2023, 8, 9, 12, 0, 0, tzinfo=tz1)

# TZ-AWARE
# Since it's explicitly specifying a time zone (UTC) for the timestamp, the resulting timestamp will be tz-aware.
import pandas as pd
pd_timestamp = pd.to_datetime('now', utc=True)

# %%

# Test to see how a AWARE compares to a NAIVE
print(pd_timestamp > aware_timestamp)