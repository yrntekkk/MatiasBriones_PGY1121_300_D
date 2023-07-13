
opc = 6
entradas = 0
asientos1 = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"]
asientos2 = ["11","12","13","14","15","16","17","18","19","20"]
asientos3 = ["21","22","23","24","25","26","27","28","29","30"]
asientos4 = ["31","32","33","34","35","36","37","38","39","40"]
asientos5 = ["41","42","43","44","45","46","47","48","49","50"]
asientos6 = ["51","52","53","54","55","56","57","58","59","60"]
asientos7 = ["61","62","63","64","65","66","67","68","69","70"]
asientos8 = ["71","72","73","74","75","76","77","78","79","80"]
asientos9 = ["81","82","83","84","85","86","87","88","89","90"]
asientos10 = ["91","92","93","94","95","96","97","98","99","100"]
platinium = 120000
gold = 80000
silver = 50000
cont_platinium = 0
cont_gold = 0
cont_silver = 0
ganancias_totales = 0
ruts = []
asistentes = {}
total_cont = 0

while opc != 5:
    print("+------------MENU------------+")
    print("1) Comprar entradas")
    print("2) Ubicaciones disponibles")
    print("3) Ver listado de asistentes")
    print("4) Mostrar ganancias totales")
    print("5) Salir")
    print("+----------------------------+")
    print("Ingrese una opcion")
    opc = int(input(">> "))

    if opc == 1:
        print("+--------COMPRAR ENTRADAS--------+")
        print("¿Cuantas entradas comprara?")
        entradas = int(input(">> "))
        while True:
            if entradas >= 1 and entradas <= 3:
                print("+---------------ASIENTOS DISPONIBLES---------------+")
                print(asientos1)
                print(asientos2)
                print(asientos3)
                print(asientos4)
                print(asientos5)
                print(asientos6)
                print(asientos7)
                print(asientos8)
                print(asientos9)
                print(asientos10)
                print("+--------------------------------------------------+")
                for i in range(entradas):
                    print("Ingrese su rut sin guion y sin numero verificador")
                    rut = input(">> ")
                    print("¿Que asiento desea?")
                    asiento = int(input(">> "))
                    ruts.append(rut)
                    asistentes ={"-" : ruts }
                    i = i + 1
                    if asiento >= 1 and asiento <= 20:
                        print("ASIENTO PLATINIUM-----PRECIO: $",platinium)
                        print("La operacion se realizo correctamente")
                        ganancias_totales = ganancias_totales + platinium
                        cont_platinium = cont_platinium + 1
                    elif asiento >= 21 and asiento <= 50:
                        print("ASIENTO GOLD-----PRECIO: $",gold)
                        print("La operacion se realizo correctamente")
                        ganancias_totales = ganancias_totales + gold 
                        cont_gold = cont_gold + 1
                    elif asiento >= 51 and asiento <= 100:
                        print("ASIENTO SILVER-----PRECIO: $",silver)
                        print("La operacion se realizo correctamente")
                        ganancias_totales = ganancias_totales + silver
                        cont_silver = cont_silver + 1
                break
            else:
                print("Ingrese una cantidad valida") 
                break

    elif opc == 2:
        print("+--------UBICACIONES DISPONIBLES--------+")
        print(asientos1)
        print(asientos2)
        print(asientos3)
        print(asientos4)
        print(asientos5)
        print(asientos6)
        print(asientos7)
        print(asientos8)
        print(asientos9)
        print(asientos10)
        print("+---------------------------------------+")

    elif opc == 3:
        print("+--------LISTADO ASISTENTES--------+")
        print(ruts)
        print("+----------------------------------+")

    elif opc == 4:
        total_cont = cont_gold + cont_platinium + cont_silver
        print("+------------GANANCIAS TOTALES------------+")
        print("TIPO ENTRADA           CANTIDAD       TOTAL")
        print(F"PLATINIUM $120.000     {cont_platinium}              {cont_platinium*platinium}")
        print(F"GOLD $80.000           {cont_gold}              {cont_gold*gold}")
        print(F"SILVER $50.000         {cont_silver}              {cont_silver*silver}")
        print(F"TOTAL                  {total_cont}              {ganancias_totales}")
        print("+-----------------------------------------+")
    
    elif opc == 5:
        print("Adios, muchas gracias")

    else:
        print("Opcion no valida, intente nuevamente")





