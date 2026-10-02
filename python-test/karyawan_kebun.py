import pytholog as pl

kb = pl.KnowledgeBase("karyawan_kebun")

kb([
    # Fakta
    "karyawan_kebun(alice)",
    "karyawan_kebun(bruno)",
    "karyawan_kebun(charlie)",

    "produktif(alice)",
    "disiplin(alice)",
    "rajin(alice)",
    "aktif_bekerja(alice)",

    "rajin(charlie)",
    "dekat(alice,charlie)",

   
    "panen_cepat(X) :- produktif(X)",
    "panen_cepat(X) :- disiplin(X), aktif_bekerja(X)",
    "tugas_cepat_selesai(X) :- disiplin(X), rajin(X)",
    "pengaruh_positif(X) :- panen_cepat(X), tugas_cepat_selesai(X)",
    "terdampak_positif(Y) :- dekat(X,Y), pengaruh_positif(X)",
    "termotivasi(Y) :- terdampak_positif(Y)",
    "tugas_cepat_selesai(Y) :- termotivasi(Y), rajin(Y)"
])

def cek(query, deskripsi):
    hasil = kb.query(pl.Expr(query))
    print(f"{deskripsi}: {hasil}")

cek("karyawan_kebun(alice)", "Apakah Alice karyawan kebun")
cek("panen_cepat(alice)", "Apakah Alice panen cepat")
cek("tugas_cepat_selesai(alice)", "Apakah tugas Alice cepat selesai")
cek("pengaruh_positif(alice)", "Apakah Alice memberi pengaruh positif")
cek("terdampak_positif(charlie)", "Apakah Charlie terdampak positif")
cek("termotivasi(charlie)", "Apakah Charlie termotivasi")
cek("tugas_cepat_selesai(charlie)", "Apakah tugas Charlie cepat selesai karena pengaruh Alice")