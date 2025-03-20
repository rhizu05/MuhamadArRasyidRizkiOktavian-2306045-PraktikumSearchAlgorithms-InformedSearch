# Algoritma Pencarian: Greedy Best-First Search dan A*

## Greedy Best-First Search
Greedy Best-First Search adalah algoritma pencarian yang memilih jalur berdasarkan nilai heuristik saja, tanpa mempertimbangkan biaya dari titik awal. Algoritma ini menggunakan fungsi evaluasi:

\[ f(n) = h(n) \]

Di mana:
- \( h(n) \) adalah perkiraan biaya dari simpul saat ini \( n \) ke tujuan.

### Kelebihan:
- Cepat dalam menemukan solusi pada beberapa kasus.
- Cocok untuk masalah dengan informasi heuristik yang akurat.

### Kekurangan:
- Tidak menjamin solusi optimal.
- Bisa terjebak dalam jalur yang tidak efisien.

---

## A* (A-Star) Search
A* Search adalah algoritma pencarian yang menggabungkan pendekatan **Greedy Best-First Search** dengan **Uniform Cost Search**. Algoritma ini menggunakan fungsi evaluasi:

\[ f(n) = g(n) + h(n) \]

Di mana:
- \( g(n) \) adalah biaya dari titik awal ke simpul saat ini.
- \( h(n) \) adalah perkiraan biaya dari simpul saat ini ke tujuan.

A* memiliki dua varian utama:

### 1. A* Graph Search
- Digunakan dalam grafik yang memiliki siklus.
- Menyimpan daftar node yang telah dikunjungi untuk menghindari eksplorasi berulang.
- Lebih efisien dalam memori dibandingkan tree search karena menghindari eksplorasi redundan.

### 2. A* Tree Search
- Digunakan dalam struktur pohon tanpa siklus.
- Tidak menyimpan daftar node yang telah dikunjungi.
- Bisa lebih cepat dalam beberapa kasus tetapi berpotensi menjelajahi kembali node yang sudah dikunjungi.

### Kelebihan A*:
- Menjamin solusi optimal jika heuristik yang digunakan **admissible** dan **consistent**.
- Efisien dibandingkan dengan algoritma pencarian uninformed.

### Kekurangan A*:
- Konsumsi memori tinggi karena harus menyimpan semua node yang dikunjungi.
- Performa sangat bergantung pada kualitas fungsi heuristik yang digunakan.

---

### Kesimpulan
- **Greedy Best-First Search** hanya mempertimbangkan heuristik \( h(n) \), sehingga bisa cepat tetapi tidak selalu optimal.
- **A* Search** mempertimbangkan biaya total \( g(n) + h(n) \), sehingga lebih optimal meskipun lebih mahal secara komputasi.
- **A* Graph Search** lebih efisien dalam eksplorasi ulang dibanding **A* Tree Search** karena menghindari kunjungan node yang sama lebih dari sekali.

Algoritma ini sering digunakan dalam pencarian jalur di AI, seperti pencarian rute navigasi dan pemecahan masalah optimasi lainnya.
