#!/bin/bash
# Django Server Startup Script

cd "$(dirname "$0")/habitas"

echo "🌐 Starting Django Development Server..."
echo ""
echo "Application will be available at: http://localhost:8000/"
echo "Admin panel: http://localhost:8000/admin/"
echo ""

/bin/python3 manage.py runserver
