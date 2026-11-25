#!/usr/bin/env sh
# Create a new 3D portfolio from adrianhajdin/project_3D_developer_portfolio.
# Usage: sh new-portfolio.sh <folder-name>
set -e
NAME="${1:-my-3d-portfolio}"
if [ -e "$NAME" ]; then echo "'$NAME' already exists" >&2; exit 1; fi
git clone --depth 1 https://github.com/adrianhajdin/project_3D_developer_portfolio.git "$NAME"
cd "$NAME"
rm -rf .git && git init -q
cat >> README.md <<'EOF'

---
Based on [project_3D_developer_portfolio](https://github.com/adrianhajdin/project_3D_developer_portfolio) by Adrian Hajdin (JavaScript Mastery).
EOF
printf 'VITE_APP_EMAILJS_SERVICE_ID=\nVITE_APP_EMAILJS_TEMPLATE_ID=\nVITE_APP_EMAILJS_PUBLIC_KEY=\n' > .env.example
grep -qx '.env' .gitignore 2>/dev/null || echo '.env' >> .gitignore
npm install
echo "Ready: cd $NAME && npm run dev"
