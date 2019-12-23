CWD=%~dp0
cd ..
python setup.py sdist bdist_wheel
cd %CWD%