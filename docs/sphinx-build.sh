
sphinx-build -M html source ./wiki

open -a 'google chrome' $(pwd)/wiki/html/index.html