#writer , Dictwriter
from csv import writer
with open('file.csv','w',newline='') as f:
    csv_writer = writer(f)
    #methods-writerow
    # csv_writer.writerow(['name','phone'])
    # csv_writer.writerow(['prashant','+917070858585'])
    # csv_writer.writerow(['preeti','+917070858585'])


    csv_writer.writerows([['name','phone'],['prashant','+917070858585'],['preeti','+917070858585']])
    
