#!/bin/bash

DOMAIN="messages"
LOCALES_DIR="locales"
LANGUAGES=("en" "ru")

for lang in "${LANGUAGES[@]}"; do
    PO_DIR="$LOCALES_DIR/$lang/LC_MESSAGES"
    PO_FILE="$PO_DIR/$DOMAIN.po"
    MO_FILE="$PO_DIR/$DOMAIN.mo"
    
    echo $lang
    echo $PO_FILE

    if [ -f "$PO_FILE" ]; then
        echo "Compiling $PO_FILE -> $MO_FILE..."
        msgfmt "$PO_FILE" -o "$MO_FILE"
    else
        echo "No .po file found for $lang. Skipping..."
    fi
done

echo "Done compiling .mo files ✅"
