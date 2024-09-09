numero_acl = input("Ingrese nuero ACL IPv4: ")

if 1 <= int(numero_acl) <=99:
    print("ACL Estandar", numero_acl)
elif 100 <= int(numero_acl) <= 199:
    print("ACL Extendida", numero_acl)
else:
    print("No es ACL IPv4", numero_acl)    