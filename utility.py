import os
import csv
import uuid

def write_csv(file_name,data, headers):
    headers = headers
    csv_file = file_name
    with open(csv_file, "a", newline="") as book:
        writer = csv.writer(book)
        if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
            writer.writerow(headers)
        writer.writerow(data)
    print("Informations saved to {} file.".format(file_name))


def get_id():
    code = str(uuid.uuid4()).replace("-","")[:4]
    return code

def delete_csv_data(csv_file,data_to_delete):
    remaining_data = []
    with open(csv_file,"r",newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if data_to_delete not in row:
                remaining_data.append(row)
    
    file.close()

    with open(csv_file,'w',newline="") as file:
        writer = csv.writer(file)
        writer.writerows(remaining_data)
    file.close()
    print("Data Deleted Successfully...")

