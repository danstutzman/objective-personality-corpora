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

predicted_f_was_f = 0
predicted_f_was_t = 0
predicted_t_was_f = 0
predicted_t_was_t = 0
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
    num_feels = len([w for w in tokens if w in ["feel", "felt", "feeling"]])
    if len(tokens) > 0:
      if num_feels / len(tokens) > 0.02:
        if is_t(row["Subject's Type"]):
          predicted_f_was_t += 1
        else:
          predicted_f_was_f += 1
      else:
        if is_t(row["Subject's Type"]):
          predicted_t_was_t += 1
        else:
          predicted_t_was_f += 1

print("Predicted F was F: %d" % (predicted_f_was_f,))
print("Predicted F was T: %d" % (predicted_f_was_t,))
print("Predicted T was F: %d" % (predicted_t_was_f,))
print("Predicted T was T: %d" % (predicted_t_was_t,))
print("Predicted F correctly: %f" % (
  float(predicted_f_was_f) / (predicted_f_was_f + predicted_f_was_t),))
print("Predicted T correctly: %f" % (
  float(predicted_t_was_t) / (predicted_t_was_f + predicted_t_was_t),))
print("Predicted either correctly: %f" % (
  float(predicted_f_was_f + predicted_t_was_t) /
  (predicted_f_was_f + predicted_f_was_t +
  predicted_t_was_f + predicted_t_was_t),))
