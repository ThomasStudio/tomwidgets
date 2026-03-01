@REM Install the package in editable mode
@REM 
@REM Usage:
@REM build package:
@REM python -m build
@REM 
@REM # upload to TestPyPI
@REM twine upload --repository testpypi dist/*
@REM 
@REM # upload to PyPI
@REM twine upload dist/*
@REM 
@REM dev mode:
@REM    pip install -e .
@REM 
@REM install local:
@REM     pip install .
@REM 
pip install -e .