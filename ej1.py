#dependiendo que tipo de jugador es, su valor de contrato y goles tira si debe estar contratado o no 

#def jugadores(goles: int, cat: str, costo: int):
#
#    mensaje = "No se puede determinar"
#
#    if cat == "B":
#
#        if goles == 20:
#
#            if costo <= 1000:
#                mensaje = "Sera contratado"
#
#            elif costo > 1000:
#                mensaje = "No sera contratado"
#
#        elif goles == 0:
#
#            if costo <= 1000:
#                mensaje = "Sera contratado"
#
#            elif costo > 1000:
#                mensaje = "No sera contratado"
#
#    elif cat == "A":
#
#        if goles == 20:
#
#            if 50000 < costo < 100000:
#                mensaje = "Preguntar al manager"
#
#        elif goles == 90:
#            mensaje = "Es Messi"
#
#    return mensaje
#
#
goles = int(input("Cual es su cantidad de goles 0, 20, 90? "))

cat = input("Para que categoria juega A o B? ")

costo = int(input("Cuanto cuesta el jugador? "))

print(jugadores(goles, cat, costo))

############################

costo_contrato = float(input("costo de contrato del jugador: "))
categoria =(input("que categoria es :"))
cant_goles = float(input("diga cuantos goles tiene: "))
contratar = (True,False)
manager = "consultar"
comision = "preguntar"

if 0<=  costo_contrato <1000 and categoria == "B" or categoria == "b" and cant_goles ==0:
    print("contratar",contratar)
    
if 100000 <= costo_contrato < 10000 and categoria == "B" or categoria == "b" and cant_goles >= 10:
   print("contratar",contratar)

elif 100000 <= costo_contrato <500000 and categoria == "A" or categoria == "a" and cant_goles == 0:
  print("contratar",contratar)

elif 100000 <= costo_contrato <= 5000000  and categoria == "A" or categoria == "a" and cant_goles == 0:
   print("contratar",contratar)

elif 100000 <= costo_contrato < 1000 and categoria == "B" or categoria == "b" and cant_goles <= (20):

    print("contratar",contratar)


elif 100000 <= costo_contrato < 150000 and categoria == "B" or categoria == "b" and cant_goles <= (20):
    print("contratar",contratar)


elif costo_contrato >=1000 and categoria == "A" or categoria == "a" and cant_goles <= (20):
    print("contratar",contratar)


if costo_contrato >10000000000 and categoria == "A" or categoria == "a" and cant_goles <= (90):
    print("es messi,CONTRATAR")

    
