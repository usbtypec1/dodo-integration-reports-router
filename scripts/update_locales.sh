#!/bin/bash

DOMAIN="messages"
LOCALES_DIR="locales"
LANGUAGES=("ru" "en")

for lang in "${LANGUAGES[@]}"; do
    PO_DIR="$LOCALES_DIR/$lang/LC_MESSAGES"
    PO_FILE="$PO_DIR/$DOMAIN.po"

    mkdir -p "$PO_DIR"

    if [ -f "$PO_FILE" ]; then
        echo "Updating $PO_FILE..."
        msgmerge --update "$PO_FILE" "$DOMAIN.pot"
    else
        echo "Creating $PO_FILE..."
        cp "$LOCALES_DIR/$DOMAIN.pot" "$PO_FILE"
    fi
done

echo "Done updating .po files ✅"
