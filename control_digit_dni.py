n_serie='XYZ123456' # Después de IDESP, 3 letras 6 dígitos
dni='12345678' # Número DNI
fecha_nacimiento='990101' # aammdd, principio de la segunda línea, 6 dígitos
fecha_vencimiento='111231' # aammdd, después de la letra de sexo (M/F), 6 dígitos

def peso731(l):
    peso=[7,3,1]
    resultado=0
    for i in range(len(l)):
        resultado+=l[i]*peso[i%len(peso)]
        
    return resultado


nif=''.join([dni,'TRWAGMYFPDXBNJZSQVHLCKE'[int(dni)%23]]) # Cálculo letra

print("NIF: ", nif)
print("Número de serie: ", n_serie)
print("Fecha nacimiento: ", fecha_nacimiento)
print("Fecha vencimiento :", fecha_vencimiento)

# Dígito control 1: justo entre el número de serie y el número DNI

n_serie2=list(map(ord,list(n_serie)[:3]))+list(map(int,n_serie[3:]))
for i in range(3):
    n_serie2[i]=n_serie2[i]-ord('A')+10

digito_control_1=peso731(n_serie2)%10

print("Digito de control 1 (entre número de serie y DNI): ", digito_control_1)

# Dígito control 2: justo entre la fecha y la letra de sexo (M/F)

fecha_nacimiento2=list(map(int, list(fecha_nacimiento)))

digito_control_2=peso731(fecha_nacimiento2)%10

print("Dígito de control 2 (entre fecha de nacimiento y sexo): ", digito_control_2)

# Dígito control 3: justo entre la fecha de vencimiento y la nacionalidad

fecha_vencimiento2=list(map(int, list(fecha_vencimiento)))

digito_control_3=peso731(fecha_vencimiento2)%10

print("Dígito de control 3 (entre fecha de vencimiento y nacionalidad): ", digito_control_3)

# Dígito control 4: final de la segunda línea

nif2=list(map(int, list(dni)))
nif2+=[ord(nif[-1])-ord('A')+10]

concatenacion=n_serie2+[digito_control_1]+nif2+fecha_nacimiento2+[digito_control_2]+fecha_vencimiento2+[digito_control_3]

digito_control_4=peso731(concatenacion)%10

print("Dígito de control 4 (final de la segunda línea): ", digito_control_4)
