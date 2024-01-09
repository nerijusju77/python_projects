"""
labas
"""
kasa = float(input("Bolt pajamos "))
premija = float(input("Kokia premija? "))
arbata = float(input("Kiek arbatos? "))
islaidos = float(input("Kokios islaidos? "))
komisas = kasa * 0.2
atvirkstinis = komisas * 21 / 121
pelnas = kasa + premija + arbata - islaidos - komisas - atvirkstinis
vsd = pelnas * 0.9 * 0.1252
psd = pelnas * 0.9 * 0.06980
if psd < 64.5:
    psd = 64.5
pelnas_po_sodros = pelnas - vsd - psd
gpm_kreditas = pelnas_po_sodros * 0.1
gpm = pelnas_po_sodros * 0.15 - gpm_kreditas
if gpm < 0:
    gpm = 0
    viso_valstybei = vsd + psd
else:
    viso_valstybei = vsd + psd + gpm
uzdarbis = pelnas - viso_valstybei

print(f"Bolt Komisas {round(komisas, 2)}")
print(f"Bolt atvirkstinis {round(atvirkstinis, 2)}")
print(f"VSD {round(vsd, 2)}")
print(f"PSD {round(psd, 2)}")
print(f"GPM {round(gpm, 2)}")
print(f"Viso valstybei {round(viso_valstybei, 2)}")
print(f"Uzdarbis {round(uzdarbis, 2)}")

print("dabar paskaiciuosiu tavo mokescius")

print("Vat tiek uzdirbai, ir nepamirsk sumokete mokescius!!!")
