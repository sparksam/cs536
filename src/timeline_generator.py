import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime, timedelta

# Define the start date for the project
start_date = datetime.today()

# Define tasks, durations, and dependencies
tasks = {
    "EternalBlue SI-2": 14,
    "EternalBlue SI-7": 30,
    "VSFTPD SI-2": 10,
    "VSFTPD SI-4": 20,
    "REPO Server CP-10": 15,
    "REPO Server MA-2": 10,
    "Windows Server SA-22": 45,
    "Windows Server CM-7": 20
}

# Calculate end dates and dependencies
end_dates = {}
current_date = start_date

for task, duration in tasks.items():
    end_date = current_date + timedelta(days=duration)
    end_dates[task] = end_date
    current_date = end_date  # Assumes sequential execution for simplicity

# Convert to DataFrame for plotting
df = pd.DataFrame(list(end_dates.items()), columns=["Task", "End Date"])
df["Start Date"] = df["End Date"] - pd.to_timedelta(df["Task"].map(tasks), unit='d')
df["Duration"] = df["Task"].map(tasks)

# Plotting
plt.figure(figsize=(12, 5))
plt.hlines(df["Task"], df["Start Date"], df["End Date"], colors='skyblue', lw=6)
plt.xticks(rotation=0)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title('Implementation Schedule for TechWorx ReSale Security Controls')
plt.xlabel('Date')
plt.ylabel('Tasks')

# Add start and end dates as text labels
for idx, row in df.iterrows():
    plt.text(row["Start Date"], row["Task"], row["Start Date"].strftime('%y-%m-%d'), verticalalignment='center', horizontalalignment='right', fontsize=6)
    plt.text(row["End Date"], row["Task"], row["End Date"].strftime('%y-%m-%d'), verticalalignment='center', horizontalalignment='left', fontsize=6)

plt.tight_layout()
plt.show()
