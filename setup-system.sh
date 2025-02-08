echo ""
echo "SETUP SYSTEM"
echo ""

#PYTHON
echo ""
echo "INSTALL PYTHON AND DEPS"
echo ""

apt update
apt install python3-pip
apt install python3-venv
apt install tk-dev

pyenv uninstall 3.10.6

apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git


echo ""
echo "ADDED PERMISSION TO RUN run.sh"
echo ""
chmod +x run.sh
