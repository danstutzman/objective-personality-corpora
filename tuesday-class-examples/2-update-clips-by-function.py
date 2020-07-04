import csv
import os.path

current_dir = os.path.abspath(os.path.dirname(__file__))

label2clips = {}
path = os.path.join(current_dir, "1-functions-by-clip.csv")
with open(path) as csv_file:
  for row in csv.DictReader(csv_file):
    labels = (row["They say clip demonstrates subject has"] or "").split(", ")
    for label in labels:
      if label == "":
        continue
      label2clips[label] = label2clips.get(label, [])
      label2clips[label].append(row)

path = os.path.join(current_dir, "2-clips-by-function.csv")
with open(path, "w") as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=[
    "Function/Animal/Modality",
    "Class Number",
    "Subject Name",
    "Subject's Type",
    "Which Class Video",
    "Class Start Time",
    "Class End Time",
    "YouTube Link",
    "YouTube End Time"
  ])
  writer.writeheader()

  for label in sorted(label2clips.keys(), key=str.lower):
    if label == "-":
      continue

    for row in sorted(label2clips[label],
        key=lambda row: int(row["Class Number"])):
      if row["YouTube Start Time"] == "-" or row["YouTube Start Time"] == "":
        continue
      h, m, s = row["YouTube Start Time"].split(":")
      h, m, s = int(h), int(m), int(s)
      youtube_start = h * 3600 + m * 60 + s
      youtube_link = "https://youtu.be/%s?start=%d" % (
        row["YouTube ID"], youtube_start)

      writer.writerow({
        "Function/Animal/Modality": label,
        "Class Number": row["Class Number"],
        "Subject Name": row["Subject Name"],
        "Subject's Type": row["Subject's Type"],
        "Which Class Video": row["Which Class Video"],
        "Class Start Time": row["Class Start Time"],
        "Class End Time": row["Class End Time"],
        "YouTube Link": youtube_link,
        "YouTube End Time": row["YouTube End Time"],
      })
print("Wrote %s" % (path,))
