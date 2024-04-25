from datetime import datetime

def is_old_enough(DOB):
    format = "%Y-%m-%d"
    if bool(datetime.strptime(DOB, format)):
        today = datetime.today()
        ago = datetime(today.year-16, today.month, today.day)
        if datetime.strptime(DOB, format) > ago:
            return "You are not over 16, access denied."
        else:
            return "You are over 16, access granted."
    try:
        
        return True
    except ValueError:
        return False
    

