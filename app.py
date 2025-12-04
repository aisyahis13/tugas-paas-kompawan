from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <div style="text-align: center; margin-top: 50px; font-family: Arial;">
       <h1>Tugas 12 - PaaS (Vercel)</h1>
       <h3>Kelompok: Kelompok ACEL (Aisyah - 1203230015, Azteca Chelsy Pramestia - 1203230062)</h3>
       <p>Aplikasi ini berjalan di atas <strong>Vercel (PaaS)</strong></p>
        <hr>
        <p>Waktu Server: {waktu}</p>
    </div>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)

