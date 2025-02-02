echo "setup python env"

python3 -m venv ./venv
source ./venv/bin/activate

echo ""
echo "installing libs"

pip install selenium
pip install python-dotenv

echo ""

echo "running..."

chmod +x run.sh
./run.sh

echo ""
echo ""
echo ""