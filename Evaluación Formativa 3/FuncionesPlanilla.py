###Funciones Planilla
import csv
trabajadores=[];

def registrarTrabajador():
    try: 
        nombre=input("Ingrese el nombre y el apellido del trabajador");
    except ValueError:
        print("Nombre y apellido son obligatorios");
    else:
        try: 
            cargo=input("Ingrese el cargo del trabajador");
        except ValueError:
            print("Ingresar el cargo es obligatorio");
        else:
            try: 
                sueldoBruto=float(input("Ingrese el sueldo del trabajador"));
            except ValueError:
                print("Ingresar el sueldo es obligatorio");
            else:
                if(cargo=='CEO'):
                    descSalud=sueldoBruto*0.07 
                    descfAfp=sueldoBruto*0.12





                trabajador = {
                'nombre': nombre,
                'cargo': cargo,
                'sueldoBruto': sueldoBruto,
                'descSalud': descSalud,
                'descAfp': descAfp,
                'liquidoPagar': liquidoPagar
                }
                trabajadores.append(trabajador)
                print("Trabajador registrado exitosamente.\n")
                






with open('ArchivoNuevo_CSV.csv','w',newline='',encoding='utf-8') as arch:
    encabezado=['Trabajador','Cargo','Sueldo Bruto','Desc. Salud','Desc. AFP','Liquido a pagar'];
    matrizDatos=input("Ingrese ")
    archivo_csv=csv.writer(arch);
    archivo_csv.writerow(encabezado);
    archivo_csv.writerow(matrizDatos);