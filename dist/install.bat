pushd %~dp0 
python setup.py install --record installed_files.txt 
rmdir /s /q RealTimeStoryIllustrator.egg-info 
rmdir /s /q build 
popd  
