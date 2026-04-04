from datetime import datetime

now = datetime.now()

formated_date = now.strftime("%d-%m-%Y %I:%M:%S")
print("Formatted date:", formated_date)

date_str = "13-02-2026"
converted = datetime.strptime(date_str, "%d-%m-%Y")
print("Converted date:", converted)