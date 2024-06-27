

# Sentiment analysis and auto-reply functions
positive_keywords = [
    "responsif", "memuaskan", "puas", "cepat", "profesional",
    "menguntungkan", "luar biasa", "nilai tambah", "ramah", "stabil",
    "kompetitif", "praktis", "update", "konsisten", "senang",
    "lengkap", "baik", "mudah", "tepat waktu", "cepat tanggap",
    "modern", "bermanfaat", "terjangkau", "berkualitas", "canggih",
    "inovatif", "efisien", "handal", "terpercaya", "unik",
    "pintar", "menyenangkan", "fleksibel", "luas", "brilian",
    "mulus", "cepat", "hebat", "cerdas", "teknologi",
    "premium", "jujur", "terbaik", "bernilai", "fantastis",
    "mumpuni", "efektif", "unik", "santai", "tepat",
    "langsung", "ramah", "bermanfaat", "pengalaman", "nyaman",
    "populer", "istimewa", "inovasi", "terpadu", "komprehensif",
    "tangguh", "perkembangan", "keamanan", "memikat", "peningkatan",
    "terdepan", "maju", "ramah lingkungan", "akurat", "bermutu",
    "terpercaya", "dipercaya", "tepat sasaran", "unggul", "brilian",
    "mudah digunakan", "modern", "produktif", "hemat", "ramah",
    "cepat", "terjangkau", "cemerlang", "mudah", "istimewa",
    "praktis", "efisien", "hemat biaya", "revolusioner", "banyak pilihan",
    "berkelas", "memuaskan", "cepat dan mudah", "teknologi tinggi", "solusi terbaik"
]

negative_keywords = [
    "gangguan", "kurang", "mahal", "lama", "rumit", "sulit",
    "turun", "tidak sesuai", "masalah", "tidak transparan",
    "perlu ditingkatkan", "perlu diperbaiki", "tidak memuaskan", "penurunan",
    "rusak", "error", "mati", "rusak", "terganggu", "buruk",
    "gangguan", "penghambat", "patah", "bocor", "kebocoran",
    "terlambat", "kecepatan rendah", "kecil", "terisolasi", "kurang",
    "putus", "tersendat", "gagal", "kegagalan", "terputus",
    "kesalahan", "kerusakan", "padam", "bermasalah", "batal",
    "pemadaman", "penundaan", "tunda", "keras", "kerugian",
    "terganggu", "konflik", "biaya tambahan", "komplain", "berat",
    "lemot", "lemah", "terbatas", "tertunda", "terlalu mahal",
    "bergantung", "terbatas", "penghancur", "kerugian", "penurunan kualitas",
    "cacat", "lemahnya", "batas", "kurangnya", "kebingungan",
    "disfungsi", "ganggu", "kekurangan", "rendah", "berbahaya",
    "keterlambatan", "ditunda", "risiko", "mengecewakan", "kerugian",
    "masalah", "terbatas", "salah", "pembatalan", "kesalahan",
    "gagal", "terganggu", "kerusakan", "penghambat", "terlambat",
    "merugikan", "pemutusan", "penundaan", "menghambat", "terganggu",
    "kendala", "keterbatasan", "terbatas", "gagap", "rusak",
    "lemah", "penyimpangan", "kebocoran", "tak layak", "bocor",
    "permasalahan", "penurunan", "batal", "batal", "putus", "jelek"
]

def analyze_sentiment(comment):
    comment_lower = comment.lower()
    positive_count = sum(comment_lower.count(keyword) for keyword in positive_keywords)
    negative_count = sum(comment_lower.count(keyword) for keyword in negative_keywords)
    
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"  

def auto_reply(comment):
    sentiment = analyze_sentiment(comment)
    if sentiment == "negative":
        return "Maaf sedang ada gangguan, akan ditangani dalam 1x24 jam"
    else:
        return None  


def input_comment():
    comment = input("Masukkan komentar Anda: ")
    return comment

def output_reply(reply):
    if reply:
        print("Balasan untuk komentar Anda:")
        print(reply)
    else:
        print("Tidak perlu merespons komentar ini.")

# Main program loop
def main():
    while True:
        comment = input_comment()
        if comment.lower() == "exit":
            print("Program selesai.")
            break
        
        reply = auto_reply(comment)
        output_reply(reply)

if __name__ == "__main__":
    main()
