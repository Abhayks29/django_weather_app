#!/bin/bash

# Django Weather App - Run Script

echo "🌤️  Django Weather App"
echo "===================="
echo ""

# Check if running with -h or --help
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "Usage: ./run.sh [command]"
    echo ""
    echo "Commands:"
    echo "  (no args)     - Start the development server"
    echo "  migrate       - Run database migrations"
    echo "  createsuperuser - Create admin user"
    echo "  test          - Run tests"
    echo "  shell         - Open Django shell"
    echo "  collectstatic - Collect static files"
    echo ""
    exit 0
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Handle different commands
case "$1" in
    migrate)
        echo "🔄 Running migrations..."
        python manage.py migrate
        ;;
    createsuperuser)
        echo "👤 Creating superuser..."
        python manage.py createsuperuser
        ;;
    test)
        echo "🧪 Running tests..."
        python manage.py test
        ;;
    shell)
        echo "🐚 Opening Django shell..."
        python manage.py shell
        ;;
    collectstatic)
        echo "📦 Collecting static files..."
        python manage.py collectstatic --noinput
        ;;
    *)
        # Default: run server
        echo "✅ Dependencies installed"
        echo "🚀 Starting development server..."
        echo ""
        echo "📍 Open your browser at: http://127.0.0.1:8000"
        echo "👨‍💼 Admin panel: http://127.0.0.1:8000/admin"
        echo ""
        echo "Press Ctrl+C to stop the server"
        echo ""
        python manage.py runserver
        ;;
esac
