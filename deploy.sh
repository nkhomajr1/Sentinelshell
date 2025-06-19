#!/bin/bash
echo "[+] Deploying SentinelShell to GitHub..."

git init
git remote add origin https://github.com/nkhoma1/SentinelShell.git
git add .
git commit -m "🚀 Initial release of SentinelShell"
git branch -M main
git push -u origin main

echo "[✔] SentinelShell is now live at:"
echo "https://github.com/nkhoma1/SentinelShell" 
