#!/usr/bin/env bash

# Script complet de pornire pentru aplicația Flask Prissma
# Gestionează mediul virtual, dependențele și pornirea serverului

set -e

# Permite rulare non-interactivă: ./start_gunicorn.sh 4
CLI_CHOICE="${1:-}"

# Directorul proiectului (mergi la parent directory)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

echo "🚀 Pornind aplicația Prissma..."

# Verifică și creează mediul virtual dacă nu există
# Verifică dacă mediul virtual este valid (căutând fișierul de activare)
if [ ! -f ".venv/bin/activate" ]; then
    echo "📦 Mediul virtual lipsește sau este corupt. Recreare..."
    rm -rf .venv # Elimină mediul virtual corupt/incomplet pentru o nouă încercare
    if ! python3 -m venv .venv; then
        echo "❌ Eroare: Nu s-a putut crea mediul virtual automat."
        echo "Sugestie: Încearcă manual: 'python3 -m venv --without-pip .venv', apoi 'source .venv/bin/activate' și 'python -m ensurepip --upgrade'."
        exit 1
    fi
fi 

# Activează mediul virtual
echo "🔧 Activând mediul virtual..."
source .venv/bin/activate

# Verifică și instalează gevent dacă nu există (necesar pentru performanță maximă)
if ! python3 -c "import gevent" 2>/dev/null; then
    echo "⚡ Instalând gevent pentru workeri async..."
    pip install gevent>=1.4.0
fi

# Funcție pentru selectarea performanței
select_performance() {
    CPU_CORES="$(sysctl -n hw.ncpu 2>/dev/null || getconf _NPROCESSORS_ONLN 2>/dev/null || echo 8)"
    AUTO_MAX_WORKERS_RAW=$((CPU_CORES * 2 + 1))
    STABLE_CAP=$((CPU_CORES + 2))
    if [ "$STABLE_CAP" -gt 12 ]; then STABLE_CAP=12; fi
    if [ "$STABLE_CAP" -lt 4 ]; then STABLE_CAP=4; fi
    if [ "$AUTO_MAX_WORKERS_RAW" -lt "$STABLE_CAP" ]; then
        AUTO_MAX_WORKERS=$AUTO_MAX_WORKERS_RAW
    else
        AUTO_MAX_WORKERS=$STABLE_CAP
    fi

    WORKER_CLASS="sync"
    THREADS=1

    echo ""
    echo "🚀 Selectează nivelul de performanță:"
    echo "  1) Low    - 2 workeri  (pentru dezvoltare, consum redus)"
    echo "  2) Medium - 9 workeri  (echilibru performanță/consum)"
    echo "  3) Max    - 16 workeri (performanță maximă pentru MacBook Air M4)"
    echo "  4) Max+   - max stabil ($AUTO_MAX_WORKERS workeri, gthread x4; detectat $CPU_CORES core-uri)"
    echo ""
    if [[ "$CLI_CHOICE" =~ ^[1-4]$ ]]; then
        choice="$CLI_CHOICE"
        echo "Alege opțiunea (1-4): $choice (din argument CLI)"
    else
        read -p "Alege opțiunea (1-4): " choice
    fi
    
    case $choice in
        1)
            WORKERS=2
            WORKER_CLASS="sync"
            THREADS=1
            echo "✅ Ai selectat: Low (2 workeri)"
            ;;
        2)
            WORKERS=9
            WORKER_CLASS="sync"
            THREADS=1
            echo "✅ Ai selectat: Medium (9 workeri)"
            ;;
        3)
            WORKERS=16
            WORKER_CLASS="sync"
            THREADS=1
            echo "✅ Ai selectat: Max (16 workeri)"
            ;;
        4)
            WORKERS=$AUTO_MAX_WORKERS
            WORKER_CLASS="gthread"
            THREADS=4
            echo "✅ Ai selectat: Max+ stabil ($WORKERS workeri, gthread x$THREADS / $CPU_CORES core-uri detectate)"
            ;;
        *)
            echo "❌ Opțiune invalidă. Folosind Medium (9 workeri) ca default."
            WORKERS=9
            WORKER_CLASS="sync"
            THREADS=1
            ;;
    esac
    echo ""
}

# Verifică dacă portul 5001 este liber
if lsof -i :5001 >/dev/null 2>&1; then
    echo "⚠️  Portul 5001 este ocupat. Oprim procesele existente..."
    lsof -ti:5001 | xargs kill -9 2>/dev/null || true
    sleep 2
fi

# Selectează performanța
select_performance

# Pornește serverul cu Gunicorn
echo "🌐 Pornind serverul pe portul 5001 cu $WORKERS workeri..."
echo "⚡ Optimizări activate: $WORKER_CLASS workers, preload, cache agresiv"
echo "🚀 Performanță optimizată pentru încărcări rapide"
echo "Accesează: http://localhost:5001"
echo "Pentru a opri serverul: Ctrl+C"
echo ""

GUNICORN_ARGS=(
    -w "$WORKERS"
    -b 0.0.0.0:5001
    -b [::]:5001
    --worker-class "$WORKER_CLASS"
    --max-requests 1000
    --max-requests-jitter 50
    --timeout 3600
    --keep-alive 10
    --access-logfile -
    --error-logfile -
    --log-level warning
)

if [ "$WORKER_CLASS" = "gthread" ]; then
    GUNICORN_ARGS+=(--threads "$THREADS")
fi

exec gunicorn \
    "${GUNICORN_ARGS[@]}" \
    app:app
