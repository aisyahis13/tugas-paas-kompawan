from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    # Menghitung Waktu WIB (UTC+7) secara manual agar tidak perlu install library tambahan
    waktu_wib = datetime.utcnow() + timedelta(hours=7)
    waktu_str = waktu_wib.strftime("%Y-%m-%d %H:%M:%S")

    # HTML dengan CSS (Desain Cantik)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tugas PaaS - Kelompok ACEL</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #333;
            }}
            .container {{
                background-color: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 15px 30px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
                width: 90%;
                transition: transform 0.3s;
            }}
            .container:hover {{
                transform: translateY(-5px);
            }}
            h1 {{
                color: #764ba2;
                margin-bottom: 5px;
                font-size: 24px;
                text-transform: uppercase;
                letter-spacing: 2px;
            }}
            .subtitle {{
                color: #888;
                font-size: 14px;
                margin-bottom: 30px;
            }}
            .group-box {{
                background-color: #f0f4ff;
                border: 2px dashed #667eea;
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 25px;
            }}
            .group-name {{
                font-weight: bold;
                color: #444;
                font-size: 16px;
                margin: 5px 0;
            }}
            .nim {{
                color: #666;
                font-size: 14px;
            }}
            .time-box {{
                margin-top: 20px;
                padding: 10px;
                background-color: #333;
                color: #0f0;
                font-family: 'Courier New', Courier, monospace;
                border-radius: 5px;
                display: inline-block;
                font-weight: bold;
            }}
            .badge {{
                background-color: #28a745;
                color: white;
                padding: 5px 10px;
                border-radius: 15px;
                font-size: 12px;
                font-weight: bold;
                vertical-align: middle;
            }}
            footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #aaa;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Tugas 12 - PaaS</h1>
            <div class="subtitle">Platform as a Service Deployment</div>
            
            <div class="group-box">
                <p class="group-name">KELOMPOK ACEL</p>
                <div class="nim">Aisyah - 1203230015</div>
                <div class="nim">Azteca Chelsy Pramestia - 1203230062</div>
            </div>

            <p>Status Aplikasi: <span class="badge">ONLINE 🟢</span></p>
            <p>Platform: <strong>Vercel (Free Tier)</strong></p>
            
            <p style="margin-top: 20px;">Waktu Server (WIB):</p>
            <div class="time-box">
                {waktu_str}
            </div>

            <footer>
                &copy; 2024 Telkom University - Komputasi Awan
            </footer>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run()
