from flask import Flask, render_template_string

app = Flask(__name__)

# --- DATA MOBIL (Ceritanya ini Database kita) ---
daftar_mobil = [
    {
        "id": 1,
        "nama": "Toyota Avanza",
        "jenis": "MPV - 7 Kursi",
        "transmisi": "Manual",
        "harga": 350000,
        "gambar": "https://images.unsplash.com/photo-1590362891991-f776e747a588?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 2,
        "nama": "Honda Brio",
        "jenis": "City Car - 5 Kursi",
        "transmisi": "Otomatis",
        "harga": 300000,
        "gambar": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 3,
        "nama": "Mitsubishi Pajero",
        "jenis": "SUV - Sport",
        "transmisi": "Otomatis",
        "harga": 1200000,
        "gambar": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 4,
        "nama": "Toyota Hiace",
        "jenis": "Minibus - 15 Kursi",
        "transmisi": "Manual",
        "harga": 1100000,
        "gambar": "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    }
]

@app.route('/')
def home():
    # CSS dan HTML digabung disini agar praktis satu file
    html_template = """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ACEL Rent Car - Sewa Mobil Terpercaya</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <style>
            :root {
                --primary: #2563eb;
                --dark: #1e293b;
                --light: #f8fafc;
            }
            body {
                font-family: 'Segoe UI', sans-serif;
                margin: 0;
                background-color: var(--light);
                color: var(--dark);
            }
            
            /* Navbar */
            .navbar {
                background: white;
                padding: 1rem 5%;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                display: flex;
                justify-content: space-between;
                align-items: center;
                position: sticky;
                top: 0;
                z-index: 100;
            }
            .logo {
                font-size: 1.5rem;
                font-weight: 800;
                color: var(--primary);
                text-decoration: none;
            }
            
            /* Hero Section */
            .hero {
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?ixlib=rb-4.0.3');
                background-size: cover;
                background-position: center;
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                color: white;
                padding: 0 20px;
            }
            .hero h1 { font-size: 2.5rem; margin-bottom: 10px; }
            .hero p { font-size: 1.1rem; opacity: 0.9; }

            /* Card Container */
            .container {
                max-width: 1200px;
                margin: 40px auto;
                padding: 0 20px;
            }
            .section-title {
                text-align: center;
                margin-bottom: 30px;
                color: var(--dark);
            }
            
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 25px;
            }

            /* Car Card */
            .card {
                background: white;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                transition: transform 0.3s;
            }
            .card:hover {
                transform: translateY(-5px);
            }
            .card-img {
                width: 100%;
                height: 200px;
                object-fit: cover;
            }
            .card-content {
                padding: 20px;
            }
            .car-name {
                font-size: 1.25rem;
                font-weight: bold;
                margin: 0 0 10px 0;
            }
            .specs {
                display: flex;
                gap: 15px;
                color: #64748b;
                font-size: 0.9rem;
                margin-bottom: 15px;
            }
            .specs i { color: var(--primary); margin-right: 5px; }
            
            .price-tag {
                font-size: 1.2rem;
                color: var(--primary);
                font-weight: bold;
                margin-bottom: 15px;
                display: block;
            }
            .btn-sewa {
                display: block;
                width: 100%;
                padding: 12px;
                background-color: #25D366; /* Warna WA */
                color: white;
                text-align: center;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                transition: background 0.3s;
            }
            .btn-sewa:hover {
                background-color: #128C7E;
            }

            /* Footer */
            footer {
                background: var(--dark);
                color: white;
                text-align: center;
                padding: 20px;
                margin-top: 50px;
            }
        </style>
    </head>
    <body>

        <nav class="navbar">
            <a href="#" class="logo">ACEL RENT CAR 🚗</a>
            <div style="font-weight: bold; color: #555;">Kelompok Acel</div>
        </nav>

        <div class="hero">
            <div>
                <h1>Solusi Perjalanan Nyaman</h1>
                <p>Sewa mobil lepas kunci atau dengan supir, harga mahasiswa!</p>
            </div>
        </div>

        <div class="container">
            <h2 class="section-title">Armada Pilihan Kami</h2>
            
            <div class="grid">
                {% for mobil in mobil_list %}
                <div class="card">
                    <img src="{{ mobil.gambar }}" alt="{{ mobil.nama }}" class="card-img">
                    <div class="card-content">
                        <h3 class="car-name">{{ mobil.nama }}</h3>
                        <div class="specs">
                            <span><i class="fas fa-car"></i> {{ mobil.jenis }}</span>
                            <span><i class="fas fa-cog"></i> {{ mobil.transmisi }}</span>
                        </div>
                        <span class="price-tag">Rp {{ '{:,}'.format(mobil.harga).replace(',', '.') }} / hari</span>
                        
                        <a href="https://wa.me/6281234567890?text=Halo%20Admin%20Acel%20Rent,%20saya%20mau%20booking%20mobil%20{{ mobil.nama }}" target="_blank" class="btn-sewa">
                            <i class="fab fa-whatsapp"></i> Booking via WA
                        </a>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>

        <footer>
            <p>&copy; 2024 Tugas PaaS - Kelompok ACEL. Deployed on Vercel.</p>
        </footer>

    </body>
    </html>
    """
    return render_template_string(html_template, mobil_list=daftar_mobil)

if __name__ == '__main__':
    app.run()
