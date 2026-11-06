#!/usr/bin/env bash
# Génère les exports SVG et PNG de tous les diagrammes Mermaid de docs/diagrammes.
# Prérequis : mermaid-cli (commande mmdc). Usage : bash scripts/build_diagrams.sh
set -euo pipefail
cd "$(dirname "$0")/../docs/diagrammes"

PUPPETEER_CFG="$(mktemp)"
echo '{"args":["--no-sandbox"]}' > "$PUPPETEER_CFG"

status=0
for f in 0*.mmd; do
  base="${f%.mmd}"
  for fmt in svg png; do
    extra=""
    [ "$fmt" = "png" ] && extra="-s 2 -w 1600 -b white"
    if mmdc -i "$f" -o "${base}.${fmt}" -c mermaid-config.json -p "$PUPPETEER_CFG" $extra >/dev/null 2>&1; then
      echo "OK   ${base}.${fmt}"
    else
      echo "ERREUR ${base}.${fmt}"; status=1
    fi
  done
done
rm -f "$PUPPETEER_CFG"
exit $status
