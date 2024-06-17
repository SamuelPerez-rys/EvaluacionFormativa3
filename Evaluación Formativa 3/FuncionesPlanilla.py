###Funciones Planilla
import csv

with open('ArchivoNuevo_CSV.csv','w',newline='',encoding='utf-8') as arch:
    encabezado=['Trabajador','Cargo','Sueldo Bruto','Desc. Salud','Desc. AFP','Liquido a pagar'];
    matrizDatos=input("Ingrese ")
    archivo_csv=csv.writer(arch);
    archivo_csv.writerow(encabezado);
    archivo_csv.writerow(matrizDatos);