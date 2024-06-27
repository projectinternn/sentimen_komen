from textblob import TextBlob

# Contoh data
positif_samples = [
    "keren", "luar biasa", "terimakasih", "Sangat memuaskan!", "Suka sekali", 
    "Sangat puas", "Terbaik", "Fantastis", "Mengagumkan", "Brilian", 
    "Hebat", "Keren", "Sempurna", "Inspiratif", "Menyenangkan", 
    "Mantap", "Spektakuler", "Mengesankan", "Super", "Istimewa", 
    "Optimal", "Dahsyat", "wow", "bagus"
]

negative_samples = [
    "jelek", "cemen", "cupu"
]

def analyze_and_respond(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    print(f"Analyzing: {text}")
    if any(word in text for word in negative_samples):
        print("Response: Maaf")
    elif any(word in text for word in positif_samples):
        print("Response: Terima kasih")

def interactive_mode():
    while True:
        user_input = input("Input: ")
        if user_input.lower() == 'exit':
            break
        analyze_and_respond(user_input)

# Memulai mode interaktif
print("Mulai mode interaktif. Ketik 'exit' untuk keluar.")
interactive_mode()
