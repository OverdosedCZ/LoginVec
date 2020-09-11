import os



otazka = input("Chces se prihlasit nebo registrovat?: ")
if otazka == "r":
    jmeno = input("Jak se chces jmenovat?: ")
    heslo = input("Jake chces heslo?: ")
    heslo1 = input("Zopakujte heslo: ")
    while heslo != heslo1:
      heslo1 = input("Zopakujte heslo: ")
    file = open(jmeno + ".txt", "w")   
    registrace = file.write(jmeno + "," + heslo)   
    file.close()
elif otazka == "p":
  while True:
    jmeno = input("Zadejte jmeno: ")
    heslo = input("Zadejte heslo: ")

    file = open(jmeno + ".txt", "r")
    log = file.readline()
    file.close()
    if log == jmeno + "," + heslo:
      print("Uspesne si se prihlasil")
      break
