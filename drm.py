import sys,os,csv

rawinput = raw_input("Inserisci percorso completo del file: ")

f = open(rawinput,"rw")

lista = f.readlines()  
f_processed = list(set(lista))
new_rawinput = rawinput.replace('.','[PROCESSED].')
new_f = open(new_rawinput, "w")
f_processed.sort()

for item in f_processed:
  new_f.write("%s" % item)

f.close()
new_f.close()
print ("File processato, Eliminati tutti i doppioni")
