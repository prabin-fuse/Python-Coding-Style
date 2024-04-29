import csv
import json
import logging

logging.basicConfig(filename="file_handling_logs.log", level= logging.DEBUG,
                    format= "%(asctime)s:%(levelname)s:%(message)s")

def filter_adults():
    try:
        with open("data.csv") as data_file:
            dict_reader = csv.DictReader(data_file)
            adults = [row for row in dict_reader if int(row["Age"]) >= 18]
            #print (adults)
    except FileNotFoundError:
        logging.error("The required file is not found")
    except ValueError:
        logging.error("The converted age value is not convertable to integer")
    except PermissionError:
        logging.error("The given file cannot be accessed by current previleages")
    except UnboundLocalError as e:
        logging.error(f"Tryiing to access local variable {e} before assifgnmeent")

    try: 
        with open("adults.csv", 'w', newline="") as adults_file:
            fields = ["Name", "Age"]
            csv_write = csv.DictWriter(adults_file, fieldnames= fields)
            csv_write.writeheader()
            csv_write.writerows(adults)
    except FileNotFoundError:
        logging.error("The required file is not found")


def add_to_json(file_name, dict_data):
    try:
        with open(file_name, "r") as json_file:
            data = json.load(json_file)
            data.append(dict_data)
    except FileExistsError:
        logging.error("The required file is not found")
    except PermissionError:
        logging.error("The given file cannot be accessed by current previleages")
    except KeyError:
        logging.warning("Accessed key is not found or not available")
        
    ### writing back to original json:
    try:
        with open(file_name, "w") as newjson_file:
            json.dump(data, newjson_file)
    except FileNotFoundError:
        logging.error("The required file is not found")

def search_log(log_file, search_keyword):
    try: 
        with open(log_file) as file:
            for line in file:
                if search_keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        logging.error("The required file is not found")
    except PermissionError:
        logging.error("The given file cannot be accessed by current previleages")



######## Testing functions:
filter_adults()

json_data = {
    "name": "Prabin",
    "age": 24
  }
add_to_json("sample.json" , json_data)

search_log("search_logg.txt", "trending")