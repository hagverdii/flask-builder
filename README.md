# flask-builder

python must be installed   
```pip install flask```   
```pip install pyinstaller```   
add react generated dist folder to the same folder/directory as this script and rename the "dist" to "react"   
then run command ```pyinstaller --onefile --add-data "react/assets;react/assets" --add-data "react/index.html;react" course_flask.py```   
generated exe file will appear in newly generated dist folder   
