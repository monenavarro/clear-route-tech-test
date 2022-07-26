# Search criteria:
# Customers aged 40-59
# Name, phone number and email address

# I am going to convert the data from the .txt file to csv
# There are python functions that work well with csv from my experience

import csv

with open("stage-1/latest-customers-converted.csv", mode = 'r') as file:
  # reading csv file
  csvFile = csv.reader(file)

  # creating empty strings to store data from csv
  age = []
  name = []
  phone_number = []
  email = []

  # creating a for loop to iterate through lines in csv file
  for lines in csvFile:
    age = lines[1]
    name = lines[0]
    phone_number = lines[3]
    email = lines[4]
    if age >= '40' and age <= '59':
      str = age + " " + name + " " + phone_number + " " + email + "\n"
      
      # write data into .txt file
      f = open("affected-customers.txt", "a")
      f.write(str)
      f.close()