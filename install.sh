printf "Installing dependencies that are needed for pypassgen...\n\n"
printf "These dependencies are needed for the program:\n"
cat requirements.txt
printf "\n"

printf "Installing, with pip3\n"

pip3 install -r requirements.txt

echo "Setting up pypassgen..."
pip3 install -e .
