current_hours = 14
current_minutes = 34
current_seconds = 42
seconds_inaday = 24 * 60 * 60
remaining_seconds = seconds_inaday - ((current_hours * 60 * 60 ) + (current_minutes * 60) + current_seconds)
print (f"remaining seconds : {remaining_seconds}")
