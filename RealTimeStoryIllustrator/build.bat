pushd %~dp0
python setup.py sdist
rmdir /s /q RealTimeStoryIllustrator.egg-info
rmdir /s /q build
popd