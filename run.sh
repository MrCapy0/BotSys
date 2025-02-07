echo "setup python env"

python3 -m venv ./venv
source ./venv/bin/activate

echo ""
echo "installing libs"

pip install selenium
pip install python-dotenv
pip install pynput
pip install screeninfo

echo ""

echo "running..."

echo ""
echo ""
echo ""

python3 main.py