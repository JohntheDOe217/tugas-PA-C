from flask import Flask

app = Flask(__name__)

# Route dasar atau halaman utama
@app.route('/')
def home():
    return 'Hello, Flask!'

# Menjalankan aplikasi di server lokal
if __name__ == '__main__':
    app.run(debug=True)
