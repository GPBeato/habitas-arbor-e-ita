#!/bin/bash
# Quick Start Script for Habitas Development
# Use this for a simplified startup

cd "$(dirname "$0")/habitas"

echo "🌳 Starting Habitas Framework..."
echo ""
echo "Terminal 1: TailwindCSS (this terminal)"
echo "Terminal 2: Django Server (open another terminal and run: ./start_django.sh)"
echo ""

export PATH="$HOME/anaconda3/envs/habitasVenv/bin:$PATH"
cd jstoolchain
npx tailwindcss -i ../input.css -o ../static/css/output.css --watch
