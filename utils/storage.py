import csv
import os
from datetime import datetime

def save_submission(first, last, phone, email, comment):
    file_path = "data/consultation_requests.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "first", "last", "phone", "email", "comment"])

        writer.writerow([
            datetime.now().isoformat(),
            first,
            last,
            phone,
            email,
            comment
        ])