# ECMWF TIGGE Data Downloader

A simple and robust Python script to download meteorological data from the **ECMWF TIGGE** dataset.  
This tool automates the process of fetching GRIB files for specific date ranges, areas, and parameters — making it ideal for researchers and data analysts working with ensemble forecast data.

---

## 🌦️ Description

This script connects to the ECMWF API to retrieve data from the **TIGGE (THORPEX Interactive Grand Global Ensemble)** dataset.  
You can easily define request parameters such as years, months, geographical area, and forecast steps directly within the script.  
It also checks for existing files to avoid re-downloading and ensures smooth operation with built-in error handling.

---

## ✨ Features

- **Easy Configuration:** All download parameters are set in one section at the top of the script.  
- **Automated Looping:** Iterates through specified years and months automatically.  
- **Skips Existing Files:** Avoids redundant downloads by checking for existing files.  
- **Robust Error Handling:** Gracefully handles ECMWF API exceptions without crashing.  

---

## ⚙️ How to Use

### 1. Prerequisites

Make sure you have **Python** installed on your system.  
You also need the `ecmwf-api-client` library. Install it with:

```bash
pip install ecmwf-api-client
```

---

### 2. Configure the Script

Open the `ecmwf_downloader.py` file in a text editor and modify the variables in the **USER CONFIGURATION** section.

```python
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
```

For a complete list of available parameters and their IDs, please refer to the **[ECMWF GRIB Parameter Database](https://apps.ecmwf.int/codes/grib/param-db)**.

---

### 3. Add Your API Credentials

Add your ECMWF API key and email address to the script:

```python
# --- Initialize ECMWF server ---
server = ECMWFDataServer(
    url="https://api.ecmwf.int/v1",
    key="YOUR_API_KEY",  # <-- Replace with your actual API key
    email="your.email@example.com"  # <-- Replace with your registered email
)
```

> ⚠️ **Important:**  
> Do not share your API key publicly.  

---

### 4. Run the Script

Open a terminal or command prompt, navigate to the folder containing the script, and run:

```bash
python ecmwf_downloader.py
```

The script will display progress messages as it downloads GRIB files to your specified output directory.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

Happy downloading! 🌍📊
