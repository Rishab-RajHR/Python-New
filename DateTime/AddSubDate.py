# Future Date and Past Date

from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=7)
past = now - timedelta(days=30)
print("Current date and time:", now)
print("Future date (7 days later):", future)
print("Past date (30 days earlier):", past)