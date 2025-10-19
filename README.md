ECMWF TIGGE Data Downloader

A simple and robust Python script to download meteorological data from the ECMWF TIGGE dataset. This tool is designed to be easily configured and run, automating the process of fetching GRIB files for specific date ranges, areas, and parameters.

Description

This script connects to the ECMWF API to retrieve data from the TIGGE (THORPEX Interactive Grand Global Ensemble) dataset. It allows you to define all request parameters—such as years, months, geographical area, and forecast steps—directly within the script. It also checks for existing files to avoid re-downloading data.

Features

Easy Configuration: All download parameters are set in a single section at the top of the script.

Automated Looping: Automatically iterates through specified years and months.

Skips Existing Files: Checks if a file has already been downloaded before making an API request.

Robust Error Handling: Gracefully handles API exceptions from the server without crashing.

How to Use

1. Prerequisites

Make sure you have Python installed on your system. You will also need the ecmwf-api-client library. If you don't have it, install it using pip:

pip install ecmwf-api-client


2. Configure the Script

Open the ecmwf_downloader.py file in a text editor. Modify the variables in the USER CONFIGURATION section to match your data requirements.

# --- USER CONFIGURATION ---
# Modify the parameters below to define your data request.

# Date Range
START_YEAR = 2006
END_YEAR = 2015
MONTHS = [3, 4, 5]  # List of months

# Geographical Area (North/West/South/East)
AREA = "27/88/20/93"

# Parameter ID (e.g., "167" for 2m temperature)
PARAM = "167"

# Time and Step parameters
TIME = "00:00:00/12:00:00"
STEP = "0/6/12/18/24"

# Output Directory
OUTPUT_DIR = r"F:\ECMWF_Data"
# --------------------------
For a complete list of available parameters and their IDs, please refer to the official ECMWF GRIB Parameter Database.
3. Add Your API Credentials

You must also add your ECMWF API key and email address to the script. Find this section and replace the placeholder values:

# --- Initialize ECMWF server ---
server = ECMWFDataServer(
    url="[https://api.ecmwf.int/v1](https://api.ecmwf.int/v1)",
    key="YOUR_API_KEY",  # <-- IMPORTANT: Replace with your actual API key
    email="your.email@example.com"  # <-- IMPORTANT: Replace with your registered email
)

4. Run the Script

Open a terminal or command prompt, navigate to the folder where you saved the script, and run it:

python ecmwf_downloader.py


The script will print its progress as it downloads the GRIB files to your specified output directory.

License

This project is licensed under the MIT License - see the LICENSE file for details.
