#prim
import heapq  # Mengimpor modul heapq untuk fungsi antrian prioritas

def make_graph():
    return {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],  # Node A terhubung ke D, C, B dengan biaya masing-masing
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],  # Node B terhubung ke A, C, E
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (6, 'F', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],  # Koneksi node C
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],  # Koneksi node D
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],  # Koneksi node E
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (6, 'C', 'F'), (7, 'D', 'F')],  # Koneksi node F
        'G': [(9, 'F', 'G')],  # Koneksi node G
    }

def prims(G, start='A'):
    unvisited = list(G.keys())  # Membuat daftar semua node dalam graf
    visited = []  # Menginisialisasi daftar kosong untuk node yang sudah dikunjungi
    total_cost = 0  # Menginisialisasi total biaya MST menjadi nol
    MST = []  # Menginisialisasi daftar kosong untuk menyimpan tepi-tepi dari MST

    unvisited.remove(start)  # Menghapus node awal dari daftar unvisited
    visited.append(start)  # Menambahkan node awal ke daftar visited

    heap = G[start]  # Menginisialisasi heap dengan tepi-tepi dari node awal
    heapq.heapify(heap)  # Mengubah daftar menjadi heap secara in-place

    while unvisited:  # Melanjutkan hingga semua node dikunjungi
        (cost, n2, n1) = heapq.heappop(heap)  # Mengambil tepi dengan biaya terkecil dari heap
        new_node = None  # Menginisialisasi new_node sebagai None

        if n1 in unvisited and n2 in visited:  # Memeriksa apakah n1 belum dikunjungi dan n2 sudah dikunjungi
            new_node = n1  # Menetapkan new_node ke n1 jika valid
            MST.append((n2, n1, cost))  # Menambahkan tepi ke MST

        elif n1 in visited and n2 in unvisited:  # Memeriksa apakah n1 sudah dikunjungi dan n2 belum dikunjungi
            new_node = n2  # Menetapkan new_node ke n2 jika valid
            MST.append((n1, n2, cost))  # Menambahkan tepi ke MST

        if new_node is not None:  # Jika ditemukan node baru
            unvisited.remove(new_node)  # Menghapusnya dari daftar unvisited
            visited.append(new_node)  # Menambahkannya ke daftar visited
            total_cost += cost  # Menambahkan biaya tepi ke total biaya

            for node in G[new_node]:  # Iterasi melalui tepi-tepi yang terhubung ke node baru
                heapq.heappush(heap, node)  # Menambahkan setiap tepi ke heap untuk dipertimbangkan

    return MST, total_cost  # Mengembalikan MST yang dibangun dan total biayanya

def main():
    G = make_graph()  # Membuat graf menggunakan fungsi make_graph
    MST, total_cost = prims(G, 'A')  # Menjalankan algoritma Prim mulai dari node A

    print(f'Minimum spanning tree: {MST}')  # Mencetak tepi-tepi dari MST
    print(f'Total cost: {total_cost}')  # Mencetak total biaya dari MST

main()  # Memanggil fungsi main untuk mengeksekusi program