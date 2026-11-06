"""Calcule la grille de decision ADR-001. Notes ordinales 1 a 5 (5 = favorable), appreciations qualitatives du groupe."""
crit = ["Cout","Complexite technique","Complexite organisationnelle","Qualite et fiabilite","Evolutivite","Securite et conformite","Adaptation 14 magasins","Delai","Ressources humaines","Maintenance"]
opts = {
 "DW centralise + MDM":[4,4,3,5,3,5,5,4,4,4],
 "Data Lake":[3,2,3,2,4,2,2,3,2,2],
 "Lakehouse":[3,2,3,4,5,4,3,2,2,3],
 "Data Mesh":[2,2,1,3,5,3,1,1,1,2],
 "Hybride (DW + MDM + zone brute)":[3,3,3,5,4,5,4,3,3,3],
}
scen = {
 "A. Poids du groupe":[10,10,10,15,10,15,10,5,5,10],
 "B. Poids egaux":[10]*10,
 "C. Evolutivite privilegiee":[5,5,5,10,30,10,5,5,5,20],
 "D. Delai et cout privilegies":[20,10,5,10,5,10,10,15,10,5],
}
for s,w in scen.items():
    assert sum(w)==100,s
    print(s, w)
    res=sorted(((sum(a*b for a,b in zip(v,w))/100,k) for k,v in opts.items()),reverse=True)
    for sc,k in res: print(f"  {sc:.2f}  {k}")
