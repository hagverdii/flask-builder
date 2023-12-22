# flask-builder

python must be installed   return
```pip install flask```   return
```pip install pyinstaller```   return
add react generated dist folder to the same folder/directory as this script and rename the "dist" to "react"   return
then run command ```pyinstaller --onefile --add-data "react/assets;react/assets" --add-data "react/index.html;react" course_flask.py```   return
generated exe file will appear in newly generated dist folder   return
