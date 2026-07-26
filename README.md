# Log Report Dashboard

A lightweight internal web dashboard built with Python and Flask for viewing system log files and generating summary reports.

## Prerequisites

- Python 3.9+
- pip

## Quick Start (Linux / macOS)

1. Make the startup script executable and launch the server:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

2. Open your browser and navigate to:
   `http://localhost:5000`

---

## Workshop Demo Scenario (Guaranteed Native Failure)

This repository includes issues that cause it to fail natively on **both** Windows and Linux:
- **Linux Native Failure (`PermissionError`)**: Clicking "Generate Report" attempts to write to `/var/log/summary_report.txt`. Linux blocks non-root users from writing to `/var/log`, causing the app to crash natively.
- **Windows Native Failure**: Direct execution fails natively on Windows due to the Bash Startup script (`run.sh`), Unix path references, and shell command execution (`cat`, `grep`).

---

## Docker Solution (The Ultimate Fix)

To make the app run identically and successfully on Linux, macOS, and Windows without code modifications:

1. Build the Docker image:
   ```bash
   docker build -t log-dashboard-alt .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 log-dashboard-alt
   ```

3. Access `http://localhost:5000` - The app works perfectly. 
   - **For Windows users:** They get a Linux environment where bash, `cat`, and `grep` exist.
   - **For Linux users:** The container isolates the application and runs it with root permissions inside the container, allowing it to safely write to `/var/log/summary_report.txt` without causing permission errors or affecting the host machine.
