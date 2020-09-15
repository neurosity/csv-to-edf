# csv-to-edf

## Create executable

```bash
pyinstaller --onefile csv-to-edf.py
```

## Test

```bash
python3 csv-to-edf.py --csv_path=samples.csv --edf_path=samples.edf --sampling_rate=250 --channel_names=CP5,F5,C3,CP3,CP6,F6,C4,CP4
```

## Run

```bash
./dist/csv-to-edf --csv_path=samples.csv --edf_path=samples.edf --sampling_rate=250 --channel_names=CP5,F5,C3,CP3,CP6,F6,C4,CP4
```
