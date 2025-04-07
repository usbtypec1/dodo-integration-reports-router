#!/bin/bash

DOMAIN="messages"
SRC_DIR="src"

echo "Extracting translatable strings from $SRC_DIR (excluding venvs)..."

xgettext --language=Python --keyword=_ \
  --from-code=UTF-8 \
  --output="./locales/$DOMAIN.pot" \
  $(find "$SRC_DIR" -name "*.py" -not -path "*/.venv/*" -not -path "*/venv/*")

sed -i '' 's/charset=CHARSET/charset=UTF-8/' ./locales/$DOMAIN.pot

echo "Done extracting strings ✅"
