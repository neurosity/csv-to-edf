import pandas as pd
import numpy as np
import pyedflib
import argparse


def csv_to_edf():
    default_channel_names = "CP3,C3,F5,PO3,PO4,F6,C4,CP4"

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_path", type=str, default="samples.csv")
    parser.add_argument("--output_path", type=str, default="samples.edf")
    parser.add_argument("--file_type", type=str, default="edf")
    parser.add_argument("--sampling_rate", type=int, default=256)
    parser.add_argument("--channel_names", type=str, default=default_channel_names)

    args = parser.parse_args()
    csv_path = args.csv_path
    output_path = args.output_path
    file_types = {"edf": pyedflib.FILETYPE_EDF, "bdf": pyedflib.FILETYPE_BDF}
    file_type = file_types[args.file_type]
    sampling_rate = args.sampling_rate
    channel_names = args.channel_names.split(",")

    channels = ["sample", *channel_names, "", "time"]
    data = pd.read_csv(csv_path, header=None)
    column_labels = {}

    for i in range(0, 11):
        column_labels[i] = channels[i]

    data = data.rename(columns=column_labels)
    data = data.drop(["sample", data.columns[-2], "time"], axis=1)
    data = data.astype(np.int16)

    signal_labels = data.columns
    eeg_data = data.values.T

    def signal_info(num):
        info = {}
        info["label"] = signal_labels[num]
        info["dimension"] = "uV"
        info["sample_rate"] = sampling_rate
        info["physical_max"] = 32767.0
        info["physical_min"] = -32768.0
        info["digital_max"] = 32767
        info["digital_min"] = -32768
        info["prefilter"] = "X"
        info["transducer"] = "X"
        return info

    with pyedflib.EdfWriter(output_path, eeg_data.shape[0], file_type=file_type) as f:
        # sets signal header information for every channel in the EEG.
        for i in range(len(signal_labels)):
            f.setSignalHeader(i, signal_info(i))
        f.writeSamples(eeg_data, digital=False)

        print(f"edf file generated at: {output_path}")


csv_to_edf()
