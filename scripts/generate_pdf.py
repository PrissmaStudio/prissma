#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator PDF cu suport complet Unicode pentru Prissma Studio
Folosește fpdf2 cu suport Unicode nativ
"""

import sys
from datetime import datetime
from pathlib import Path
from fpdf import FPDF

# Importează fpdf2 pentru suport Unicode optim
try:
    from fpdf import FPDF
    PDF_ENGINE = 'fpdf2'
    print("✓ fpdf2 disponibil - suport Unicode optim")
except ImportError:
    print("✗ fpdf2 nu disponibil")
    sys.exit(1)

def generate_pdf_fpdf2():
    """Generează PDF cu fpdf2 - suport Unicode complet"""
    
    pdf = FPDF(
        orientation='P',
        unit='cm',
        format='A4',
        encoding='utf-8'
    )
    
    # Setează font default cu suport Unicode
    pdf.add_font('DejaVu', '', '/Users/alex/Library/Fonts/DejaVuSans.ttf')
    pdf.add_font('DejaVu', 'B', '/Users/alex/Library/Fonts/DejaVuSans-Bold.ttf')
    
    # Fallback dacă fonturile nu sunt găsite
    try:
        pdf.set_font('DejaVu', '', 12)
    except:
        print("⚠ Fonturile DejaVu nu găsite, folosesc Arial...")
        pdf.set_font('Arial', '', 12)
    
    # Pagina 1 - Copertă
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 28)
    pdf.ln(5)
    pdf.cell(0, 1, 'PRISSMA STUDIO', ln=True, align='C')
    
    pdf.set_font('DejaVu', '', 14)
    pdf.cell(0, 0.8, 'Aplicație Web de Galerie Media', ln=True, align='C')
    
    pdf.ln(1)
    pdf.set_font('DejaVu', '', 12)
    metadata = f"""Versiune: v7.24.2b
Data: {datetime.now().strftime('%d.%m.%Y %H:%M')}
Autori: AI Assistant & Development Team
Status: COMPLET"""
    
    pdf.multi_cell(0, 0.5, metadata, align='C')
    
    # Pagina 2 - Cuprins
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 16)
    pdf.cell(0, 1, 'CUPRINS', ln=True)
    pdf.set_font('DejaVu', '', 12)
    
    toc = """1. Motivul alegerii temei
2. Descrierea softului utilizat și cerințe de sistem
3. Descrierea aplicației
4. Codul sursă - Tehnologie și Arhitectură
5. Bibliografie și Referințe"""
    
    pdf.multi_cell(0, 0.5, toc)
    
    # Pagina 3+ - Conținut
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 16)
    pdf.cell(0, 0.8, '1. MOTIVUL ALEGERII TEMEI', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    intro = """Prissma Studio reprezintă o soluție completă pentru gestionarea și prezentarea profesională a galeriilor media digitale. Alegerea acestei teme a fost determinată de necesitățile reale din domeniul fotografiei și al managementului conținutului digital, unde există o cerere crescândă pentru platforme web care să combine ușurința în utilizare cu performanță și securitate avansată."""
    
    pdf.multi_cell(0, 0.5, intro)
    pdf.ln(0.3)
    
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '1.1 Contextul și Necesitățile Identificate', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    context = """În era digitală actuală, fotografi, agenții media și creatorii de conținut se confruntă cu provocări semnificative în organizarea și prezentarea colecțiilor lor de imagini și videouri. Problemele tradiționale includ:

• Managementul volumelor mari de media: Colecții cu mii de fișiere care necesită organizare eficientă și acces rapid

• Performanță și viteză de încărcare: Imaginile de înaltă rezoluție încetinesc semnificativ site-urile web tradiționale

• Securitate și control al accesului: Necesitatea protejării conținutului sensibil sau privat

• Experiență multi-dispozitiv: Utilizatorii accesează conținutul de pe desktop, tabletă și mobil

• Internaționalizare: Suport pentru multiple limbi pentru audiențe diverse

• Feedback și interacțiune: Sistem de recenzii pentru evaluarea și comentarea conținutului"""
    
    pdf.multi_cell(0, 0.4, context)
    
    pdf.ln(0.3)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '1.2 Analiza Pieței și Soluțiilor Existente', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    market = """Platformele existente pentru galerii media (WordPress, Adobe Portfolio, Squarespace) prezintă limitări semnificative:

• Performanță scăzută: Încărcare lentă pentru galerii mari

• Securitate limitată: Protecție slabă pentru conținut privat

• Personalizare redusă: Template-uri rigide și opțiuni limitate

• Costuri ridicate: Abonamente lunare pentru funcții esențiale

• Dependente externe: Necesitatea plugin-urilor și extensiilor"""
    
    pdf.multi_cell(0, 0.4, market)
    
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '1.3 Obiectivele Proiectului', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    objectives = """Prissma Studio își propune să rezolve aceste probleme prin:

• Optimizare extremă a performanței: Caching inteligent și compresie automată

• Sistem de securitate multi-nivel: Protecție granulară a folderelor

• Arhitectură scalabilă: Suport pentru baze de date mari și trafic ridicat

• Interfață adaptivă: Design responsiv pentru toate dispozitivele

• Automatizare completă: Procese de optimizare și management automate

• Cost-eficiență: Soluție open-source cu costuri minime de întreținere"""
    
    pdf.multi_cell(0, 0.4, objectives)
    
    pdf.ln(0.3)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '1.4 Beneficiile Educaționale', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    benefits = """Proiectul demonstrează competențe avansate în:

• Dezvoltare full-stack: Backend Python/Flask și frontend modern

• Optimizare performanță: Caching, compresie și concurență

• Securitate web: Autentificare, autorizare și protecție CSRF

• Baze de date: Design relational și migrări de date

• Internaționalizare: Suport multi-limbă și localizare

• DevOps: Deployment și management în producție"""
    
    pdf.multi_cell(0, 0.4, benefits)
    
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 16)
    pdf.cell(0, 0.8, '2. DESCRIEREA SOFTULUI ȘI CERINȚE DE SISTEM', ln=True)
    
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '2.1 Tehnologii Utilizate', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    technologies = """Prissma Studio este dezvoltat folosind un stack modern și scalabil:

• Backend: Python 3.8+ cu Flask 2.0+ framework web

• Bază de date: SQLAlchemy 3.0+ ORM cu SQLite/PostgreSQL

• Procesare media: Pillow 9.0+ pentru imagini, compresie automată

• Caching: Flask-Caching cu FileSystemCache pentru performanță

• Internaționalizare: Flask-Babel pentru suport multi-limbă

• Securitate: Werkzeug pentru hashing parole, CSRF protection

• Deployment: Gunicorn WSGI server cu gevent workers"""
    
    pdf.multi_cell(0, 0.4, technologies)
    
    pdf.ln(0.3)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '2.2 Cerințe de Sistem', ln=True)
    
    pdf.set_font('DejaVu', '', 11)
    requirements = """Minim:
• Procesor: Intel i3 / AMD Ryzen 3
• Memorie RAM: 2 GB
• Spațiu disk: 5 GB
• Sistem operare: Linux/macOS/Windows
• Python: 3.8+
• Browser: Chrome 90+ / Firefox 88+

Recomandat:
• Procesor: Intel i5 / AMD Ryzen 5
• Memorie RAM: 4 GB+
• Spațiu disk: 10 GB+
• Sistem operare: Linux/macOS/Windows 10+
• Python: 3.9+
• Browser: Chrome 100+ / Firefox 95+"""
    
    pdf.multi_cell(0, 0.4, requirements)
    
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 16)
    pdf.cell(0, 0.8, '3. DESCRIEREA APLICAȚIEI', ln=True)
    
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '3.1 Prezentare Generală și Funcționalitate', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    app_desc = """Prissma Studio este o platformă web completă destinată prezentării și gestionării profesionale a galeriilor media digitale. Aplicația permite utilizatorilor să exploreze colecții organizate de imagini și videouri într-un mod intuitiv și performant.

Site-ul funcționează ca o galerie virtuală modernă, unde conținutul este organizat în foldere tematice (ex: "Nuntă Maria & Ion", "Portret Claudia", "Evenimente Corporate"). Fiecare folder poate conține sute sau mii de imagini și videouri, toate optimizate automat pentru web."""
    
    pdf.multi_cell(0, 0.4, app_desc)
    
    pdf.ln(0.3)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '3.2 Fluxul Utilizatorului Final', ln=True)
    
    pdf.set_font('DejaVu', 'B', 11)
    pdf.cell(0, 0.5, '3.2.1 Accesarea Galeriei Principale', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    gallery_flow = """Când un utilizator accesează site-ul, este întâmpinat cu:

• Pagina de Bun Venit: Prezentare scurtă a serviciilor oferite
• Galerie Principală: Grid responsiv cu toate folderele disponibile
• Navigare Multi-Limbă: Selector pentru RO/EN/HU
• Bară de Căutare: Căutare în timp real după nume folder"""
    
    pdf.multi_cell(0, 0.4, gallery_flow)
    
    pdf.ln(0.2)
    pdf.set_font('DejaVu', 'B', 11)
    pdf.cell(0, 0.5, '3.2.2 Explorarea unui Folder', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    folder_exp = """La click pe un folder, utilizatorul:

• Vede imaginile care se încarcă progresiv (LQIP apoi full)
• Poate deschide lightbox pentru vizualizare cu zoom
• Are opțiuni de filtrare și sortare
• Poate partaja imagini sau foldere"""
    
    pdf.multi_cell(0, 0.4, folder_exp)
    
    pdf.ln(0.2)
    pdf.set_font('DejaVu', 'B', 11)
    pdf.cell(0, 0.5, '3.2.3 Sistemul de Recenzii', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    reviews = """Fiecare folder are un sistem de feedback:

• Formular cu: Nume, email, rating 1-5 stele, comentariu
• Validare automată cu rate limiting (max 5 recenzii/IP/zi)
• Afișare listă cronologică cu avatar și dată
• Moderare administrator cu ștergere recenzii neadecvate"""
    
    pdf.multi_cell(0, 0.4, reviews)
    
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '3.3 Funcționalitățile Administratorului', ln=True)
    
    pdf.set_font('DejaVu', 'B', 11)
    pdf.cell(0, 0.5, '3.3.1 Autentificarea Admin', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    admin_auth = """Accesul la panoul de control:

• URL dedicat: /admin/login
• Parolă securizată ca variabilă de mediu
• Sesiune persistentă (24 ore)
• Rate limiting: Max 10 încercări pe minut"""
    
    pdf.multi_cell(0, 0.4, admin_auth)
    
    pdf.ln(0.2)
    pdf.set_font('DejaVu', 'B', 11)
    pdf.cell(0, 0.5, '3.3.2 Dashboard-ul Principal', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    dashboard = """Panoul oferă statistici în timp real:

• Mărimi foldere și număr imagini/videouri
• Statistici recenzii și rating mediu
• Performanță sistem și cache utilizat
• Activitate recentă cu ultimele recenzii"""
    
    pdf.multi_cell(0, 0.4, dashboard)
    
    pdf.ln(0.2)
    pdf.set_font('DejaVu', 'B', 11)
    pdf.cell(0, 0.5, '3.3.3 Gestionarea Conținutului', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    content_mgmt = """Administratorul poate:

• Încărca fișiere cu validare tip și dimensiune
• Organiza foldere (creare, redenumire, ștergere)
• Seta protecție cu chei de acces
• Procesa optimizare automată în background
• Efectua backup și restaurare"""
    
    pdf.multi_cell(0, 0.4, content_mgmt)
    
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 16)
    pdf.cell(0, 0.8, '4. CODUL SURSĂ - TEHNOLOGIE ȘI ARHITECTURĂ', ln=True)
    
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '4.1 Configurare Inițială', ln=True)
    
    pdf.set_font('DejaVu', '', 10)
    pdf.set_fill_color(245, 245, 245)
    init_code = """from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_caching import Cache

app = Flask(__name__)
app.secret_key = 'prissma_v2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prissma.db'
db = SQLAlchemy(app)"""
    
    pdf.multi_cell(0, 0.35, init_code, fill=True)
    
    pdf.ln(0.3)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '4.2 Modele de Date', ln=True)
    
    pdf.set_font('DejaVu', '', 10)
    models_code = """class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder_name = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime)"""
    
    pdf.multi_cell(0, 0.35, models_code, fill=True)
    
    pdf.ln(0.3)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 0.6, '4.3 Sistem de Caching', ln=True)
    
    pdf.set_font('DejaVu', '', 10)
    cache_code = """app.config['CACHE_TYPE'] = 'FileSystemCache'
app.config['CACHE_DIR'] = 'cache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 3600
cache = Cache(app)"""
    
    pdf.multi_cell(0, 0.35, cache_code, fill=True)
    
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 16)
    pdf.cell(0, 0.8, '5. BIBLIOGRAFIE ȘI REFERINȚE', ln=True)
    
    pdf.set_font('DejaVu', '', 12)
    references = """[1] Flask Documentation - https://flask.palletsprojects.com/
[2] SQLAlchemy Documentation - https://docs.sqlalchemy.org/
[3] Pillow Documentation - https://pillow.readthedocs.io/
[4] Flask-Caching - https://flask-caching.readthedocs.io/
[5] Flask-Babel - https://python-babel.github.io/flask-babel/
[6] Gunicorn Documentation - https://docs.gunicorn.org/
[7] MDN Web Docs - https://developer.mozilla.org/
[8] fpdf2 Documentation - https://py-pdf.github.io/fpdf2/"""
    
    pdf.multi_cell(0, 0.5, references)
    
    pdf.ln(0.5)
    pdf.set_font('DejaVu', '', 10)
    footer = f"Document generat {datetime.now().strftime('%d.%m.%Y %H:%M')}. © 2026 Prissma Development Team."
    pdf.multi_cell(0, 0.4, footer, align='C')
    
    # Salvează PDF
    pdf_path = Path(__file__).parent / 'PRISSMA_DOCUMENTATIE.pdf'
    pdf.output(str(pdf_path))
    
    return pdf_path

def main():
    """Generează PDF cu fpdf2 - suport Unicode complet"""
    
    print("\n" + "="*60)
    print("GENERATOR PDF - PRISSMA STUDIO DOCUMENTATIE")
    print("="*60)
    
    try:
        print("\n🎨 Utilizez fpdf2 pentru suport Unicode complet...")
        pdf_path = generate_pdf_fpdf2()
        
        file_size = pdf_path.stat().st_size / 1024
        
        print("\n" + "="*60)
        print("✓ PDF generat cu succes!")
        print(f"✓ Fisier: {pdf_path.name}")
        print(f"✓ Locatie: {pdf_path}")
        print(f"✓ Dimensiune: {file_size:.1f} KB")
        print(f"✓ Engine: {PDF_ENGINE.upper()}")
        print(f"✓ Diacritice: ✓ Suport complet Unicode!")
        print("="*60 + "\n")
        
        return pdf_path
        
    except Exception as e:
        print(f"\n✗ Eroare la generare PDF: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAnulat de utilizator.")
        sys.exit(1)
