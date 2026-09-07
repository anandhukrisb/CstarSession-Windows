import os
import subprocess
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Protected system log path (Requires root permissions on Linux, invalid on Windows)
LOG_DIR = "data/logs"
TEMP_REPORT = "/var/log/summary_report.txt"

@app.route("/")
def index():
    logs = []
    # Hardcoded Unix forward-slash paths
    for file_name in sorted(os.listdir(LOG_DIR)):
        if file_name.endswith(".log"):
            file_path = LOG_DIR + "/" + file_name
            with open(file_path, "r") as f:
                for line in f:
                    parts = line.strip().split(" | ")
                    if len(parts) == 3:
                        logs.append({
                            "timestamp": parts[0],
                            "level": parts[1],
                            "message": parts[2],
                            "source": file_name
                        })
    return render_template("index.html", logs=logs)

@app.route("/generate-report", methods=["POST"])
def generate_report():
    # Unix command & root file path
    # - Native Linux: Fails with 'Permission denied' writing to /var/log/
    # - Native Windows: Fails due to missing cat/grep/run.sh and /var/log/ path
    # - Docker: Works on both (runs containerized Linux environment as root)
    command = "cat data/logs/*.log | grep -v 'DEBUG' > " + TEMP_REPORT
    subprocess.run(command, shell=True, check=True)
                        
    return send_file(TEMP_REPORT, as_attachment=True, download_name="summary_report.txt")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
