# csv-to-edf

## Create executable

```bash
pyinstaller --onefile csv-to-edf.py
```

## Test

```bash
python3 csv-to-edf.py --csv_path=samples.csv --output_path=samples.edf --file_type=edf --sampling_rate=256 --channel_names=CP3,C3,F5,PO3,PO4,F6,C4,CP4
```

or for BDF:

```bash
python3 csv-to-edf.py --csv_path=samples.csv --output_path=samples.bdf --file_type=bdf --sampling_rate=256 --channel_names=CP3,C3,F5,PO3,PO4,F6,C4,CP4
```

## Run

```bash
./dist/csv-to-edf --csv_path=samples.csv --output_path=samples.edf --file_type=edf --sampling_rate=256 --channel_names=CP3,C3,F5,PO3,PO4,F6,C4,CP4
```
