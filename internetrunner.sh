#/bin/bash
echo "Cloning QJournal from GitHub..." 
git clone https://github.com/scutoidzz/QJournal &> /dev/null
echo "Sucessfully Downloaded"
cd QJournal
echo "Installing pip requirements..."
pip3 install -r requirements.txt --break-system-packages &> /dev/null
echo "Sucessfully Installed pip requirements"
echo "Running QJournal..."
python3 main.py &> /dev/null

