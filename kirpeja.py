pajamos = float(input("Pajamos "))
islaidos = float(input("Kokios islaidos? "))

pelnas = pajamos - islaidos
vsd = pelnas * 0.9 * 0.1252
psd = pelnas * 0.9 * 0.06980
if psd < 58.63:
    psd = 58.63
pelnas_po_sodros = pelnas - vsd - psd
gpm_kreditas = pelnas_po_sodros * 0.1
gpm = pelnas_po_sodros * 0.15 - gpm_kreditas
if gpm < 0:
    gpm = 0
    viso_valstybei = vsd + psd
else:
    viso_valstybei = vsd + psd + gpm
uzdarbis = pelnas - viso_valstybei


print(f"VSD {round(vsd, 2)}")
print(f"PSD {round(psd, 2)}")
print(f"GPM {round(gpm, 2)}")
print(f"Viso valstybei {round(viso_valstybei, 2)}")
print(f"uzdarbis{round(uzdarbis, 2)}")
print("nepamirsk sumoketi mokescius!!!")
