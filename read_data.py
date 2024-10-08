import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the CSV file
raw_emg_df = pd.read_csv("EMG_DATA_TEST.CSV", encoding="utf-8")

# Separate the calibration value
calibration_df = raw_emg_df[raw_emg_df["Time(ms)"] == "Calibration"]
calibration_values = calibration_df["EMG Signal"].values  # Get the calibration value

# Remove the calibration row from the dataframe
emg_df = raw_emg_df[raw_emg_df["Time(ms)"] != "Calibration"]

# Convert the "Time(ms)" column to numeric for plotting
emg_df["Time(ms)"] = pd.to_numeric(emg_df["Time(ms)"])

# Plot the EMG signal data
fig, ax = plt.subplots()
ax.plot(emg_df["EMG Signal"])
ax.set_xlabel("Time (ms)")
ax.set_ylabel("EMG Signal")
plt.ion()
plt.show()