seg = input("Por favor, entre com o número de segundos que deseja converter:")
seg = int(seg)
dia = 86400
qd = seg / dia 
qd = int(qd)
r =  seg % dia 
hr = 3600
qh = r / hr 
qh = int(qh)
r = seg %  hr
min = 60 
qm = r / min 
qm = int(qm)
segundos = r % min 
print(qd,"dias,",qh,"horas,",qm,"min e",segundos,"segundos.")