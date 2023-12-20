import requests
import yaml
import time
from urllib.parse import urlparse

#parse yaml
def load_endpoints(file_path):
    with open(file_path, 'r') as file:
        try:
            content = yaml.safe_load(file)
        except Exception as e:
                print(e)
        return content

#Perform requests, log results, display results to console
def check_health(endpoints):
    availability_percentage = {}

    #Get request parameters
    while True:
        for endpoint in endpoints:
            #required args
            url = endpoint["url"]
            domain = urlparse(url).netloc
            #optional args
            method = endpoint.get('method')
            if not method:
                method = "GET"
            headers = endpoint.get('headers')
            body = endpoint.get('body')

            #initalize hashmap for domain if needed
            availability_percentage.setdefault(domain, [0,0])
            
            #perform request
            try:
                response = requests.request(method, url, params=headers, data=body)
                response_status = response.status_code
                response_time = response.elapsed
                if (response_time.total_seconds() * 1000 < 500) and (response_status // 100 == 2):
                    #success
                    availability_percentage[domain][0] += 1
                    availability_percentage[domain][1] += 1
                else:
                    #fail
                    availability_percentage[domain][1] += 1
            except Exception as e:
                print(f"Error with {method} for {domain} at {url}!\n{e}")
        
        #display domain results
        for key in availability_percentage:
            print(f"{key} has {(availability_percentage[key][0]/availability_percentage[key][1])*100} availability percentage")
        print("-------------------------------")
        time.sleep(15)

#main
if __name__ == "__main__":
    print("Welcome to HTTP health monitor.py\nPress \"ctrl + c\" to stop.")
    file_path = input("Enter the file path for a list of HTTP endpoints in YAML format to begin monitoring: ")
    endpoints = load_endpoints(file_path)
    check_health(endpoints)