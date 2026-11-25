import os

LINE = "I finished the work on time and saved my checkpoint, then restored the wrong one, the one from Tuesday, which held a grocery list, a 2009 bus timetable, and no deadline at all."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
