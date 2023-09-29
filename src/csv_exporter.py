headers = ['Timestamp', 'Message']
def export_to_csv(data, headers, filename="output.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)