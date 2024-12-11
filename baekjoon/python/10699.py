from datetime import datetime, timedelta

utc_now = datetime.utcnow()
seoul_now = utc_now + timedelta(hours=9)

print(seoul_now.strftime("%Y-%m-%d"))
