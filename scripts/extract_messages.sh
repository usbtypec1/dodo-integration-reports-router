#!/bin/bash

DOMAIN="messages"
SRC_DIR="."

echo "Extracting translatable strings from $SRC_DIR..."
xgettext --language=Python --keyword=_ --output="./locales/$DOMAIN.pot" $(find "$SRC_DIR" -name "*.py")

echo "Done extracting strings ✅"
