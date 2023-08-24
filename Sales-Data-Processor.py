import csv

date = input()
money = input()
product = input()

with open("OldSales.csv", "r") as csvfile:
  csv_reader = csv.DictReader(csvfile)
    
  with open("NewSales.csv", "a") as NewSales:

    fieldnames = ['Date:', 'Money', 'Product']
    
    csv_writer = csv.DictWriter(NewSales, fieldnames=fieldnames, delimiter=' ')
    
    for line in csv_reader:
      data = {
        'Date:': date,
        'Money': money, 
        'Product': product
      }

      print(csv_writer.writerow(data))
