import csv

def save_to_file():
    file = open('jobs.csv', 'w', -1,'utf-8', newline='')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'location', 'apply_link'])
    writer.writerow([1,2,3,4])
    # for job in jobs:
    #     writer.writerow(list(job.values()))
    return 