import os
import csv
import uuid


# function that writes the data in csv file
def write_csv(file_name, data, headers):
    '''This function takes three parameters namely file_name, data and headers and saves
    the data in csv file along with the specific headers. '''

    headers = headers
    csv_file = file_name
    with open(csv_file, "a", newline="") as book:
        writer = csv.writer(book)
        if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
            writer.writerow(headers)
        writer.writerow(data)
    book.close()
    print("Informations saved to {} file.".format(file_name))


# function returns the unique code of length 4
def get_id():
    code = str(uuid.uuid4()).replace("-", "")[:4]
    return code


# function that deletes the data from the csv file
def delete_csv_data(csv_file, data_to_delete):
    '''
        This function takes two parameters namely csv file name and id of data to delete
    '''
    remaining_data = []
    with open(csv_file, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if data_to_delete not in row:
                remaining_data.append(row)

    file.close()

    with open(csv_file, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(remaining_data)
    file.close()
