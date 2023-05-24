@echo off
@REM FOR /F "tokes=* delims=" %%x in (npm.txt) DO echo %%x\
@REM FOR /F %%i IN (npm.txt) DO @echo %%i
@REM for /?
@REM FOR /F "eol=; tokens=2,3* delims=, " %i in (npm.txt) do @echo %i %j %k
COLOR 1
ECHO DOWN BELOW LIST NPM TO INSTALL:
COLOR 7
FOR /F "eol=; tokens=* delims= " %%i IN (npm.txt) DO @echo %%i
pause
