import pytholog as pl
kb = pl.KnowledgeBase("Mahasiswa")

kb([
    "berprestasi(andi)",
    "disiplin(andi)",
    "rajin(andi)",
    "aktif_belajar(andi)",

    "rajin(budi)",
    "dekat(andi,budi)",

    "lulus_cepat(X) :- berprestasi(X)",
    "lulus_cepat(X) :- disiplin(X), aktif_belajar(X)",
    "tugas_cepat_selesai(X) :- disiplin(X), rajin(X)",
    "pengaruh_positif(X) :- lulus_cepat(X), tugas_cepat_selesai(X)",
    "terdampak_positif(Y) :- dekat(X,Y), pengaruh_positif(X)",
    "termotivasi(Y) :- terdampak_positif(Y)",
    "tugas_cepat_selesai(Y) :- termotivasi(Y), rajin(Y) "
])

def cek(query, deskripsi):
    hasil = kb.query(pl.Expr(query))
    print(f"{deskripsi}: {hasil}")

cek("lulus_cepat(andi)", "Apakah Andi lulus cepat")
cek("tugas_cepat_selesai(andi)", "Apakah tugas Andi cepat selesai")
cek("pengaruh_positif(andi)", "Apakah Andi memberi pengaruh positif")
cek("terdampak_positif(budi)", "Apakah Budi terdampak positif")
cek("tugas_cepat_selesai(budi)", "Apakah tugas Budi cepat selesai karena pengaruh Andi")



