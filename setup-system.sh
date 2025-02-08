echo ""
echo "Install system deps"
echo ""

apt update
apt install python3-pip
apt install python3-venv
apt install tk-dev

pyenv uninstall 3.10.6

apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git



chmod +x run.sh
