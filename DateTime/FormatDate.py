from datetime import datetime

now = datetime.now()

formated_date = now.strftime("%d-%m-%Y %I:%M:%S")
print("Formatted date:", formated_date)