def dense_ranking(scores, gits_scores):
    # Membuat set dari daftar skor untuk mendapatkan nilai unik yang terurut dari besar ke kecil
    unique_scores = sorted(set(scores), reverse=True)

    # Membuat kamus yang akan menyimpan peringkat untuk setiap skor
    score_rank = {}
    current_rank = 1

    for score in unique_scores:
        score_rank[score] = current_rank
        current_rank += 1

    # Menghitung peringkat GITS berdasarkan skor yang didapat
    gits_ranks = []
    for gits_score in gits_scores:
        gits_rank = 1
        for score in unique_scores:
            if gits_score >= score:
                break
            gits_rank += 1
        gits_ranks.append(gits_rank)

    return gits_ranks

# Contoh penggunaan fungsi
if _name_ == "_main_":
    num_players = int(input())
    scores = list(map(int, input().split()))
    num_games = int(input())
    gits_scores = list(map(int, input().split()))

    result = dense_ranking(scores, gits_scores)
    print(*result)