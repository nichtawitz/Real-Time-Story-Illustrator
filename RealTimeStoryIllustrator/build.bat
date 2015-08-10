pushd %~dp0
python setup.py sdist
type NUL > dist/install.bat
echo pushd %%~dp0 >> dist/install.bat
echo python setup.py install --record installed_files.txt >> dist/install.bat
echo rmdir ^/s ^/q RealTimeStoryIllustrator.egg-info >> dist/install.bat
echo rmdir ^/s ^/q build >> dist/install.bat
echo popd >> dist/install.bat 
pause
type NUL > dist/uninstall.bat
echo pushd %%~dp0 >> dist/uninstall.bat
echo for ^/f ^"delims=^" %%%%g in ('type installed_files.txt') DO del "%%g"  >> dist/uninstall.bat
echo del installed_files.txt  >> dist/uninstall.bat
echo python -m pip uninstall RealTimeStoryIllustrator-0.1.zip  >> dist/uninstall.bat
echo rmdir ^/s ^/q dist  >> dist/uninstall.bat
echo popd  >> dist/uninstall.bat
pause
type NUL > dist/start.bat
echo pushd %%~dp0 >> dist/start.bat
echo cd RealTimeStoryIllustrator-0.1\RealTimeStoryIllustrator-0.1\rtsi ^&^& python main.py >> dist/start.bat
echo popd >> dist/start.bat
pause
type NUL > dist/MANIFEST.in
echo recursive-include rtsi/data *.jpg *.txt *.png >> dist/MANIFEST.in
pause
type NUL > dist/setup.py
echo from setuptools import setup, find_packages, Command >> dist/setup.py
echo. >> dist/setup.py
echo setup( >> dist/setup.py
echo     name='RealTimeStoryIllustrator', >> dist/setup.py
echo     version='0.1', >> dist/setup.py
echo     packages=find_packages(), >> dist/setup.py
echo     include_package_data=True, >> dist/setup.py
echo     package_data={'rtsi.data': ['*.txt','*.png','*.jpg']}, >> dist/setup.py
echo     url='https://github.com/nichtawitz/bac', >> dist/setup.py
echo     license='', >> dist/setup.py
echo     author='hoebartNichtawitz', >> dist/setup.py
echo     author_email='', >> dist/setup.py
echo     description='Real Time Story Illustrator - Narrates german stories and displays fitting images', >> dist/setup.py
echo     install_requires=[ >> dist/setup.py
echo         'gTTs', >> dist/setup.py
echo         'PySide', >> dist/setup.py
echo         'goslate' >> dist/setup.py
echo     ], >> dist/setup.py
echo     entry_points={ >> dist/setup.py
echo         'console_scripts': [ >> dist/setup.py
echo             'start_rtsi = rtsi.main:main', >> dist/setup.py
echo         ] >> dist/setup.py
echo     } >> dist/setup.py
echo ) >> dist/setup.py
rmdir /s /q RealTimeStoryIllustrator.egg-info
rmdir /s /q build
popd