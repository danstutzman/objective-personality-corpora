# Tuesday Class Examples corpora

## How to download 1-functions-by-clip.csv from the Google Doc

- Go to https://docs.google.com/spreadsheets/d/1A-HpIHWP-HWyEWPfCpwLOJGno7WGvpXDRYuWRscO990/edit
- Go to the Raw Data sheet
- Choose File, Download, Comma-Separated Values
- Move the downloaded CSV file to overwrite `1-functions-by-clip.csv`

## How to update the Clips By Function tab of the Google Doc

- Follow earlier instructions to download 1-functions-by-clip.csv
- `python3 2-update-clips-by-function.py`
- Go to https://docs.google.com/spreadsheets/d/1A-HpIHWP-HWyEWPfCpwLOJGno7WGvpXDRYuWRscO990/edit
- Go to the Clips By Function sheet
- Choose File, Import, Upload
- Navigate to 2-clips-by-function.csv
- Set Import Location to Replace Current Sheet
- Click Import Data
- Add underlining to the first row

## How to download new YouTube automatic transcripts:

- `pip3 install youtube_transcript_api`
- `python3 3-download-automatic-transcripts.py`
  - This will download only transcripts that don't already have a .json file

## How to re-generate the 4-cropped-transcripts directory:

- `python3 4-crop-transcripts.py`
