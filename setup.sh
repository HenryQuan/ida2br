# link lldb folder to the current folder
sudo ln -s $( lldb -P )/lldb lldb
# create a virtual env
virtualenv .env
# need to be updated for windows
.env/bin/pip3 install -r requirement.txt
