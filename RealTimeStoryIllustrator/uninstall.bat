pushd %~dp0 
for /f "delims=" %%g in ('type installed_files.txt') DO del "%%g"
del installed_files.txt
cd..
cd..
python -m pip uninstall RealTimeStoryIllustrator-0.2.zip
rmdir /s /q dist  
popd  
