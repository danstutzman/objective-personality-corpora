import csv
import json
import os.path

current_dir = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(current_dir, "1-functions-by-clip.csv")
with open(path) as csv_file:
  for row in csv.DictReader(csv_file):
    if row["YouTube Start Time"] == "-" or row["YouTube Start Time"] == "" or \
       row["YouTube End Time"] == "-" or row["YouTube End Time"] == "":
      continue

    h, m, s = row["YouTube Start Time"].split(":")
    h, m, s = int(h), int(m), int(s)
    start_seconds = h * 3600 + m * 60 + s

    h, m, s = row["YouTube End Time"].split(":")
    h, m, s = int(h), int(m), int(s)
    end_seconds = h * 3600 + m * 60 + s

    transcript_path = os.path.join(current_dir, "3-automatic-transcripts",
      row["YouTube ID"] + ".json")
    print(transcript_path)
    with open(transcript_path) as transcript_file:
      transcript_rows = json.load(transcript_file)

    cropped_filename = "%s.%d.%d.txt" % \
      (row["YouTube ID"], start_seconds, end_seconds)
    cropped_path = os.path.join(current_dir, "4-cropped-transcripts",
      cropped_filename)
    with open(cropped_path, "w") as cropped_file:
      for transcript_row in transcript_rows:
        if transcript_row["start"] < end_seconds and \
            transcript_row["start"] + transcript_row["duration"] > \
            start_seconds:
          cropped_file.write(transcript_row["text"] + "\n")
