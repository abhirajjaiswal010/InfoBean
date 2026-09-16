from rich.live import Live
import time

with Live("Loading...", refresh_per_second=4) as live:

    for i in range(5):
        live.update(f"Progress: {i}")
        time.sleep(1)