#/bin/bash
git clone https://github.com/scutoid/QJournal.git
cd QJournal
pip3 install -r requirements.txt --break-system-packages
python3 main.py
