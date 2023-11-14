import csv #Import CSV modulu pro praci s CSV
import json #Import JSON modulu pro praci s JSON

with open('document.txt') as doc: #Otevreni TXT souboru, ktery je pojmenovany jako doc
    content = doc.read() #read precte vsechny radky v souboru
    print(content)

with open('document.txt') as doc:
    for line in doc.readlines(): #cyklus, ktery probehne zvlast pro kazdy radek souboru
        print(line)

with open('document.txt') as doc:
    first = doc.readline() #readline precte jeden radek od prvniho
    second = doc.readline()
    print(first)
    print(second)

with open('document.txt', 'a') as doc: #a - append-mode (mod pro pridavani radku); w - write-mode (prepise cely soubor)
    doc.write("\nSparta") #\n - odradkovani

#--- CSV ---
username_list = []
with open('names.csv', newline='') as doc:
    reader = csv.DictReader(doc, delimiter=';') #delimiter = v pripade, ze nepouzivame carky pro oddelovani, nastavime delimiter
    #for row in reader:
        #username_list.append(row['Username'])
#print(username_list)

write_data = [{'Name': 'Frank', 'Username': 'CoolPrezdivka', 'Gender': 'Upir'},
              {'Name': 'Petr', 'Username': 'Exekuce', 'Gender': 'Binary'},
              {'Name': 'Anna', 'Username': 'DalsiCoolPrezdivka', 'Gender': 'Furry'}] #nova data ve slovnicich do CSV souboru

with open('names.csv', 'w') as doc: #w - write-mode (mod prepisovani)
    fields = ['Name', 'Username', 'Gender'] #nazvy sloupcu na prvnim radku
    writer = csv.DictWriter(doc, fieldnames=fields) #fieldnames nastavi nazvy na prvnim radku
    writer.writeheader()
    for row in write_data:
        writer.writerow(row)

#--- JSON ---
with open('purchase.json') as doc:
    data = json.load(doc) #nacte data z JSON souboru
    print(data['user'])

payload = {
    'date': 'dnesek',
    'eventID': 15487
}

with open('purchase.json', 'w') as doc:
    json.dump(payload, doc) #dump - v souboru doc prepise data z payload