echo ""
echo "Install system deps"
echo ""

apt install python3-pip
apt install python3-venv
python3 -m ensurepip --default-pip

chmod +x run.sh
