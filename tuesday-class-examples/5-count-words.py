import csv
import json
import os.path

def is_de(full_type):
  function1 = full_type[3:5]
  if function1 == "Te" or function1 == "Fe": return True
  if function1 == "Ti" or function1 == "Fi": return False

  function2 = full_type[6:8]
  if function2 == "Te" or function2 == "Fe": return True
  if function2 == "Ti" or function2 == "Fi": return False

  raise Exception("Can't determine if type %s is De" % (full_type,))

def is_t(full_type):
  function1 = full_type[3:5]
  if function1 == "Te" or function1 == "Ti": return True
  if function1 == "Fe" or function1 == "Fi": return False

  function2 = full_type[6:8]
  if function2 == "Te" or function2 == "Ti": return True
  if function2 == "Fe" or function2 == "Fi": return False

  raise Exception("Can't determine if type %s is T" % (full_type,))

current_dir = os.path.abspath(os.path.dirname(__file__))

t_tokens = []
f_tokens = []
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

    cropped_filename = "%s.%d.%d.txt" % \
      (row["YouTube ID"], start_seconds, end_seconds)
    cropped_path = os.path.join(current_dir, "4-cropped-transcripts",
      cropped_filename)
    with open(cropped_path) as cropped_file:
      transcript = cropped_file.read()

    tokens = transcript.lower().split() # split on any whitespace

    if is_t(row["Subject's Type"]):
      t_tokens.extend(tokens)
    else:
      f_tokens.extend(tokens)

print("Savior T use of words like 'feel':")
print(len([w for w in t_tokens if w in ["feel", "felt", "feeling"]]) /
  len(t_tokens))
print("Savior F use of words like 'feel':")
print(len([w for w in f_tokens if w in ["feel", "felt", "feeling"]]) /
  len(f_tokens))
