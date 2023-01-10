from csv import DictWriter
with open('final.csv','w') as f:
    csv_writer =  DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    # writerow , writerows
    csv_writer.writerow({
        'firstname': "preeti"
        'lastname':'singh'
        'age': 500
    })

    csv_writer.writerow({ 
        'firstname': "preeti"
        'lastname':'singh'
        'age': 500
    })

    csv_writer.writerow({
        'firstname': "prashant"
        'lastname':'singh'
        'age': 500
    })

