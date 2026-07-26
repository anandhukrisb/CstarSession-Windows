import os
import subprocess
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Cross-platform paths
LOG_DIR = os.path.join("data", "logs")
TEMP_REPORT = "summary_report.txt"

@app.route("/")
def index():
    logs = []
    for file_name in sorted(os.listdir(LOG_DIR)):
        if file_name.endswith(".log"):
            file_path = os.path.join(LOG_DIR, file_name)
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
    import glob
    
    # Cross-platform Python approach
    with open(TEMP_REPORT, "w") as outfile:
        # Sort files to ensure consistent order
        for file_path in sorted(glob.glob(os.path.join(LOG_DIR, "*.log"))):
            with open(file_path, "r") as infile:
                for line in infile:
                    if "DEBUG" not in line:
                        outfile.write(line)
                        
    return send_file(TEMP_REPORT, as_attachment=True, download_name="summary_report.txt")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
