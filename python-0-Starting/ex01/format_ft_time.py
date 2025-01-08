import time
import datetime


timestamp = time.time()
formatted_timestamp = f'{timestamp:,.4f}'
today = datetime.date.today()

print(f"Seconds since January 1, 1970: {formatted_timestamp} or \
{timestamp:.2e} in scientific notation")
print(f"{today.strftime('%b %d %Y')}")
