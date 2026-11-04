from zoneinfo import ZoneInfo
from datetime import datetime

current_time = datetime.now(ZoneInfo("Asia/Kolkata"))

print("Current time:", current_time)
print("Python version test successful!")    