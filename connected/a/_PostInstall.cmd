@echo off
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo ---------------------------------------------------------------------------------
@echo --------------------------------DISABLE HIBERNATE--------------------------------
@echo ---------------------------------------------------------------------------------
powercfg -h off
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo ----------------------------------------------------------------------------------
@echo --------------------------------INSTALL POWER PLAN--------------------------------
@echo ----------------------------------------------------------------------------------
powercfg -import "C:\Windows\_BitsumHighestPerformance.pow" 77777777-7777-7777-7777-777777777777
powercfg -SETACTIVE "77777777-7777-7777-7777-777777777777"
powercfg -delete 381b4222-f694-41f0-9685-ff5bb260df2e
powercfg -delete 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 
powercfg -delete a1841308-3541-4fab-bc81-f71556f20b4a
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo --------------------------------------------------------------------------------------
@echo --------------------------------IMPORT NVIDIA SETTINGS--------------------------------
@echo --------------------------------------------------------------------------------------
_nvidiaProfileInspector.exe "C:\Windows\_NvidiaBaseProfile.nip"
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo ------------------------------------------------------------------------------------------------
@echo --------------------------------INSTALL TIMER RESOLUTION SERVICE--------------------------------
@echo ------------------------------------------------------------------------------------------------
_SetTimerResolutionService.exe -install
sc config STR start=auto
net start STR
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo --------------------------------------------------------------------------------------------
@echo --------------------------------REBUILD PERFORMANCE COUNTERS--------------------------------
@echo --------------------------------------------------------------------------------------------
lodctr /r
lodctr /r
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo --------------------------------------------------------------------------------------
@echo --------------------------------IMPORT REGISTRY TWEAKS--------------------------------
@echo --------------------------------------------------------------------------------------
_RegistryTweaks.reg
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo -----------------------------------------------------------------------------------
@echo --------------------------------TRANSFER USER FILES-------------------------------- 
@echo -----------------------------------------------------------------------------------
robocopy "C:\Windows\Administrator" "C:\Users\Administrator" /NFL /NDL /NJH /NJS /nc /ns /np /E /MOVE 
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo ----------------------------------------------------------------------------------------------------
@echo --------------------------------DEBLOAT SCRIPT LOADING (PLEASE WAIT)-------------------------------- 
@echo ----------------------------------------------------------------------------------------------------
powershell "& ""C:\Windows\_DebloatScript.ps1"""
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo -----------------------------------------------------------------------------
@echo --------------------------------RESTARTING PC--------------------------------
@echo -----------------------------------------------------------------------------
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
@echo .
pause
C:\Windows\System32\shutdown.exe /r /t 0