from varasto import Varasto

def tulosta_varastot(mehua, olutta):
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def tulosta_olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def tulosta_mehu_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def tulosta_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def tulosta_lisaa_olutta_varastossa(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def tulosta_lisaa_mehua_varastossa(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def tulosta_ota_olutta_varastosta(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def tulosta_ota_mehua_varastosta(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.ota_varastosta(1000.0)")
    saatiin = mehua.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    tulosta_varastot(mehua, olutta)
    tulosta_olut_getterit(olutta)
    tulosta_mehu_setterit(mehua)

    tulosta_virhetilanteet()

    tulosta_lisaa_olutta_varastossa(olutta)
    tulosta_lisaa_mehua_varastossa(mehua)

    tulosta_ota_olutta_varastosta(olutta)
    tulosta_ota_mehua_varastosta(mehua)

if __name__ == "__main__":
    main()
