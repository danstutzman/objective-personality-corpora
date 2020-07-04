import csv
import json
import os.path
import time
import youtube_transcript_api

current_dir = os.path.abspath(os.path.dirname(__file__))

youtube_ids = set()
path = os.path.join(current_dir, "1-functions-by-clip.csv")
with open(path) as csv_file:
  for row in csv.DictReader(csv_file):
    if row["YouTube ID"] != "-":
      youtube_ids.add(row["YouTube ID"])

num_to_download = 0
for youtube_id in youtube_ids:
  path = os.path.join(current_dir, "3-automatic-transcripts",
    youtube_id + ".json")
  if not os.path.exists(path):
    num_to_download += 1

for youtube_id in youtube_ids:
  path = os.path.join(current_dir, "3-automatic-transcripts",
    youtube_id + ".json")
  if not os.path.exists(path):
    with open(path, "w") as json_file:
      print("Downloading transcript %s... (%d left)" %
        (youtube_id, num_to_download))
      try:
        transcript_rows = \
          youtube_transcript_api.YouTubeTranscriptApi.get_transcript(youtube_id)
        json.dump(transcript_rows, json_file)
      except youtube_transcript_api._errors.TranscriptsDisabled:
        json_file.write("[]")
      except youtube_transcript_api._errors.NoTranscriptAvailable:
        json_file.write("[]")
      except youtube_transcript_api._errors.NoTranscriptFound:
        json_file.write("[]")
      json_file.write("\n")
    print("Wrote %s" % (path,))
    num_to_download -= 1
    time.sleep(1)
