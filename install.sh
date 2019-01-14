echo "Installing dependencies that are needed for this program..."
cat requirements.txt

pip3 install -r requirements.txt

echo "Setting up pypassgen..."
pip3 install -e .
