from app import app, generate_cache_for_attached_volume, get_base_dir, GDRIVE_FOLDER
import os

with app.app_context():
    base = get_base_dir()
    print(f"📂 Baza curentă detectată: {base}")
    print(f"📂 Calea configurată pentru GDrive: {GDRIVE_FOLDER}")
    
    # Verificăm dacă suntem pe Drive
    if "GoogleDrive" in base or "CloudStorage" in base or os.path.exists(GDRIVE_FOLDER):
        print("🔄 Generăm cache pentru pozele de pe Drive...")
        try:
            generate_cache_for_attached_volume()
            print("✅ Gata! Cache-ul a fost generat.")
        except Exception as e:
            print(f"❌ Eroare la generare: {e}")
    else:
        print("⚠️  Se pare că Drive-ul nu este selectat ca bază curentă.")
        print("Dacă vrei să forțezi Drive-ul, asigură-te că este conectat/montat.")