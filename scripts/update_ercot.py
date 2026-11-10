from datetime import datetime, timedelta, timezone
from pathlib import Path
from gridstatusio import GridStatusClient

client = GridStatusClient()

# Fetch the previous 3 complete UTC days
end = datetime.now(timezone.utc).date()
start = end - timedelta(days=3)

df = client.get_dataset(
    "ercot_spp_real_time_15_min",
    start=str(start),
    end=str(end),
    filter_column="location",
    filter_value=[
        "LZ_HOUSTON",
        "LZ_NORTH",
        "LZ_SOUTH",
        "LZ_WEST",
    ],
    filter_operator="in",
    timezone="US/Central",
)

if df.empty:
    raise RuntimeError("GridStatus returned no data")

# Save the results
Path("data").mkdir(exist_ok=True)

df.to_csv("data/ercot_spp.csv", index=False)

print(f"Downloaded {len(df)} rows")
