@echo off

start shell:startup

timeout /t 2 /nobreak >nul

powershell -command "[System.Windows.Forms.SendKeys]::SendWait('{DOWN}')"
powershell -command "[System.Windows.Forms.SendKeys]::SendWait('{UP}')"
powershell -command "[System.Windows.Forms.SendKeys]::SendWait('~')"

timeout /t 2 /nobreak >nul

powershell -command "[System.Windows.Forms.SendKeys]::SendWait('^(c)')"

timeout /t 2 /nobreak >nul

powershell -command "[System.Windows.Forms.SendKeys]::SendWait('%({TAB})')"

timeout /t 2 /nobreak >nul

powershell -command "[System.Windows.Forms.SendKeys]::SendWait('^(v)')"

timeout /t 2 /nobreak >nul

exit
