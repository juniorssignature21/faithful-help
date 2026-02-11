#!/bin/bash

# Update primary button/theme color from red (#e12454) to healthcare blue (#e32f6f)
sed -i 's/#e12454/#e32f6f/g' css/style.css
sed -i 's/#E12454/#e32f6f/g' css/style.css
sed -i 's/rgb(225, 36, 84)/rgb(0, 102, 204)/g' css/style.css

# Update accent green (#8fb569) to teal (#008080) 
sed -i 's/#8fb569/#008080/g' css/style.css
sed -i 's/#8FB569/#008080/g' css/style.css
sed -i 's/rgb(143, 181, 105)/rgb(0, 128, 128)/g' css/style.css

# Update theme overlay blue to match new primary color
sed -i 's/#1696e7/#e32f6f/g' css/style.css

echo "Color scheme updated from red/green to blue/teal healthcare colors"
