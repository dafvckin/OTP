@echo off
del /s /f /q C:\windows\temp\*.* 
rd /s /q C:\windows\temp 
md c:\windows\temp  
del /s /f /q %temp%\*.* 
rd /s /q %temp% 
md %temp%
cleanmgr /verylowdisk