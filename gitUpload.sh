#!/bin/bash
echo "Write commit reason:"
read COMMIT
git add .
git add .
git commit -m "$COMMIT"
git push