import requests 
import json
import calendar 
import time
import csv
import ast

url = "http://192.168.27.213:8000/workers/"
payload = {}
headers = {}

resp = requests.request("GET", url, auth=('alex', 'alexbatman1'), headers=headers, data = payload)
data = json.loads(resp.text.encode('utf8'))

# get salary avg
sum_salary = 0 
counter = 0 
length = len(data) 
while counter < length:
	sum_salary += data[counter]['salary']
	counter += 1
avg_s = sum_salary/length
print(f"The avg salary is: {round(avg_s, 2)}")

# calc workers with hire_date -ge one year and avg salary
fields = ['employee_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'jobs', 'salary', 'commission_pct', 'manager_id', 'department_id']
csv_file = 'part_03_output_file.txt'
counter = 0 
# write the header to csv file
with open(csv_file, 'w') as f:
	writer = csv.DictWriter(f, fieldnames=fields)
	writer.writeheader()
# append records to file
while counter < length:
	time_hire = data[counter]['hire_date']
	time_delta = round(time.time()) - calendar.timegm(time.strptime(time_hire, '%Y-%m-%d'))
	salary = data[counter]['salary']
	if time_delta > 365 * 86400 and salary > avg_s:
		try:
			with open(csv_file, 'a', newline='') as f:
				writer = csv.DictWriter(f, fieldnames=fields)
				line = data[counter]
				writer.writerow(line)
		except IOError:
			print("I\O ERROR")
	counter+=1
print(f"Output file at: {csv_file}")
