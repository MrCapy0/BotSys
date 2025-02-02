echo "setup python env"

python3 -m venv ./venv
source ./venv/bin/activate

echo ""
echo "installing libs"

pip install selenium
pip install python-dotenv

echo ""

echo "running..."

echo ""
echo ""
echo ""

python3 main.py