# Log Report Dashboard

A lightweight web dashboard built with Python and Flask for viewing system log files and generating summary reports.

---

## Prerequisites

- **Python** 3.9 or higher
- **pip** (Python package manager)
- **Git**

---

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/anandhukrisb/CstarSession-Windows.git
cd CstarSession-Windows
```

---

### Step 2: Create a Virtual Environment

#### On Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows (Command Prompt)

```cmd
python -m venv venv
venv\Scripts\activate
```

#### On Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

> **Note:** If you get an error on PowerShell about execution policies, run this first:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Run the Application

#### On Linux / macOS

```bash
python3 app.py
```

Or using the startup script:

```bash
chmod +x run.sh
./run.sh
```

#### On Windows

```cmd
python app.py
```

> **Note:** The `run.sh` script will **not work** on Windows as it is a Bash shell script.

---

### Step 5: Open in Browser

Navigate to: **http://localhost:5000**

You should see the Log Report Dashboard with system log entries displayed in a table.

---

## Features

- View system logs from multiple log files (`app.log`, `auth.log`, `system.log`)
- Generate a filtered summary report (removes DEBUG entries)
- Download the summary report as a text file

---

## Try This

1. Open the dashboard at `http://localhost:5000`
2. Browse the log entries in the table
3. Click the **"⚡ Generate Report"** button

**What happened?** Did it work? Did it crash? Why?

---

## Project Structure

```
CstarSession-Windows/
├── app.py                  ← Main Flask application
├── requirements.txt        ← Python dependencies
├── run.sh                  ← Bash startup script (Linux/macOS only)
├── data/
│   └── logs/
│       ├── app.log         ← Application logs
│       ├── auth.log        ← Authentication logs
│       └── system.log      ← System logs
├── templates/
│   └── index.html          ← Dashboard web page
└── static/
    ├── css/style.css       ← Stylesheet
    └── images/
        ├── logo.png        ← Dashboard logo
        └── Logo.PNG        ← Symlink to logo.png
```
