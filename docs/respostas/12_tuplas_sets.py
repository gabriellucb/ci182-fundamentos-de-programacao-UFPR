"""Resposta — Aula 12: Tuplas e Sets
Exercício: valores únicos, operações de conjunto e desempacotamento de tuplas.
"""

numeros = [4, 7, 2, 7, 1, 4, 9, 2, 6, 4]

unicos = set(numeros)
print(f"Lista original:   {numeros}")
print(f"Valores únicos:   {sorted(unicos)}")
print(f"Quantidade única: {len(unicos)}")

matematica = {"Ana", "Beto", "Carla", "Diego", "Eva"}
fisica     = {"Beto", "Eva", "Fabio", "Carla", "Gabi"}

em_ambas      = matematica & fisica
so_uma        = matematica ^ fisica
pelo_menos_uma = matematica | fisica

print(f"\nMatemática:           {sorted(matematica)}")
print(f"Física:               {sorted(fisica)}")
print(f"Cursaram as duas:     {sorted(em_ambas)}")
print(f"Só uma delas:         {sorted(so_uma)}")
print(f"Pelo menos uma:       {sorted(pelo_menos_uma)}")

pontos = [
    (-25.4284, -49.2733),
    (-22.9068, -43.1729),
    (-3.7172,  -38.5434),
]

print("\nCoordenadas:")
for lat, lon in pontos:
    print(f"  Lat {lat:.4f}  Lon {lon:.4f}")
