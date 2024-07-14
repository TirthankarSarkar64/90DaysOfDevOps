from datetime import datetime
import pytz

current_timestamp = datetime.now(pytz.timezone("US/Pacific)).strftime("%Y-%m-%d %H-%M-%S")
print("Current Time is: %s"%current_timestamp)
