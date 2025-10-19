#!/usr/bin/env python

"""
A robust script to download TIGGE data from the ECMWF API.

This script allows users to easily modify download parameters (date range, area, etc.)
by changing variables at the top of the file. It handles API exceptions gracefully
and skips files that have already been downloaded.
"""

from ecmwfapi import ECMWFDataServer, APIException
import calendar
import os

# --- USER CONFIGURATION ---
# Modify the parameters below to define your data request.

# Date Range
START_YEAR = 2006
END_YEAR = 2015
MONTHS = [3, 4, 5]  # List of months, e.g., [3, 4, 5] for March, April, May

# Geographical Area (North/West/South/East)
AREA = "27/88/20/93"

# Parameter ID (e.g., "167" for 2m temperature)
PARAM = "167"

# Time and Step parameters
# Use "/" to separate multiple values
TIME = "00:00:00/12:00:00"
STEP = "0/6/12/18/24"

# Output Directory
# Use a raw string (r"...") for Windows paths to avoid issues with backslashes.
OUTPUT_DIR = r"F:\ECMWF_Data"

# --------------------------

def download_data(config):
    """
    Connects to the ECMWF server and downloads data based on the provided configuration.
    """
    # --- Create the output directory if it doesn't exist ---
    if not os.path.exists(config["output_dir"]):
        os.makedirs(config["output_dir"])
        print(f"Created directory: {config['output_dir']}")

    # --- Initialize ECMWF server ---
    # Pass your credentials directly
    server = ECMWFDataServer(
        url="https://api.ecmwf.int/v1",
        key="YOUR_API_KEY",  # <-- IMPORTANT: Replace with your actual API key
        email="your.email@example.com"  # <-- IMPORTANT: Replace with your registered email
    )

    # --- Main download loop ---
    for year in config["years"]:
        for month in config["months"]:
            # Determine the last day of the month
            _, last_day = calendar.monthrange(year, month)
            date_range = f"{year}-{month:02d}-01/to/{year}-{month:02d}-{last_day}"

            # Define the output file name and path
            file_name = f"tigge_param_{config['param']}_{year}_{month:02d}.grib"
            target_path = os.path.join(config["output_dir"], file_name)

            # --- Check if the file already exists ---
            if os.path.exists(target_path):
                print(f"Skipping already downloaded file: {file_name}")
                continue

            print(f"Requesting GRIB file: {file_name}")

            # --- Attempt to retrieve the data ---
            try:
                server.retrieve({
                    "class": "ti",
                    "dataset": "tigge",
                    "date": date_range,
                    "expver": "prod",
                    "grid": "0.5/0.5",
                    "area": config["area"],
                    "levtype": "sfc",
                    "origin": "ecmf",
                    "param": config["param"],
                    "step": config["step"],
                    "time": config["time"],
                    "type": "cf",
                    "target": target_path
                })
                print(f"-> Successfully downloaded {file_name}")

            except APIException as e:
                print(f"-> FAILED to download {file_name}. Server error: {e}")
                print("   This may be a server-side issue. Skipping to the next file.")
            except Exception as e:
                print(f"-> An unexpected error occurred for {file_name}: {e}")

    print("\nAll requested downloads are complete!")

if __name__ == "__main__":
    # Assemble the configuration dictionary from the parameters defined above
    config = {
        "years": range(START_YEAR, END_YEAR + 1),
        "months": MONTHS,
        "area": AREA,
        "param": PARAM,
        "time": TIME,
        "step": STEP,
        "output_dir": OUTPUT_DIR
    }

    print("--- ECMWF TIGGE Data Downloader ---")
    print("Starting download with the following configuration:")
    print(f"  Years:       {START_YEAR} to {END_YEAR}")
    print(f"  Months:      {config['months']}")
    print(f"  Area:        {config['area']}")
    print(f"  Parameter:   {config['param']}")
    print(f"  Time:        {config['time']}")
    print(f"  Step:        {config['step']}")
    print(f"  Output Dir:  {config['output_dir']}")
    print("-" * 35)

    download_data(config)