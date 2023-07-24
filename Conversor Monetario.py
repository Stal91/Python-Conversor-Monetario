
while True:

    valor_Real_float = 0
    tipo_moeda = ""
     
    valor_Real_float = None

    valor_Real = input("Digite o valor em reais: ")
    tipo_moeda = input("Escolha a moeda a ser convertida (USD, EUR, PESO)").upper()

    try:
        valor_Real_float = float(valor_Real)
    except Exception :
        valor_Real_float = None

        if valor_Real_float is None:
            print("Digite um numero valido")
            continue
    
    moedas_permitidas = "USD EUR PESO"
            
    if tipo_moeda not in moedas_permitidas:
        print("Digite alguma moeda valida!!")
        continue
   
    print("Convertendo sua moeda...")

    real_usd = valor_Real_float * 5
    real_eur = valor_Real_float * 6
    real_peso = valor_Real_float * 56

    if tipo_moeda == "USD":
        print(f"Valor em Dólar (USD): {real_usd:.2f}")
    elif tipo_moeda == "EUR":
        print(f"Valor em Euro (EUR): {real_eur:.2f}")
    elif tipo_moeda == "PESO":
        print(f"Valor em Peso (PESO): {real_peso:.2f}")
    else:
        print("Controle de qualidade")          
          

    sair = input("Deseja Sair [S]im: ").lower().startswith("s")
    if sair is True:
        break