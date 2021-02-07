import csv


def save_to_file(jobs):
    file = open(f"{jobs}.csv", "w", -1, "utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Apply_link'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
