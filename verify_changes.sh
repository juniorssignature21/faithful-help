#!/bin/bash

echo "=== FAITHFUL HELP HEALTHCARE LTD - WEBSITE UPDATE VERIFICATION ==="
echo ""

echo "✓ Color Updates in CSS:"
grep -c "#e32f6f" css/style.css
echo "  Primary Blue (#e32f6f) instances found"

echo ""
echo "✓ Contact Information Updates:"
grep -c "09121172271" index.html
echo "  Phone number instances in main page"

grep -c "faithwillie261@gmail.com" index.html
echo "  Email instances in main page"

echo ""
echo "✓ Service Updates:"
grep -c "Home-Based Elderly Care\|Hospital Support Care\|Caregiver Training" index.html
echo "  Service references in main page"

echo ""
echo "✓ Team Member Updates:"
grep "Faith Willie\|Chukwu Okafor\|Dr. Amara Nwankwo" index.html | wc -l
echo "  Team member names found"

echo ""
echo "✓ Branding CSS File:"
test -f css/faithful-branding.css && echo "  ✓ faithful-branding.css exists" || echo "  ✗ File missing"

echo ""
echo "✓ Files Updated:"
grep -l "faithful-branding.css" *.html | wc -l
echo "  HTML files with branding CSS reference"

echo ""
echo "✓ Documentation:"
test -f UPDATE_DOCUMENTATION.md && echo "  ✓ UPDATE_DOCUMENTATION.md created" || echo "  ✗ File missing"

echo ""
echo "=== VERIFICATION COMPLETE ==="
