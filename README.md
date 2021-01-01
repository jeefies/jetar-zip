# jezip-tar

A package for save zip/tar file in memory buffer(not write in file)

Usage:
```
from jezt import ZipFile MyZip = ZipFile()  
# The Type of the ZipFile:  
# MyZip = ZipFile(ZipFile.BZIP) BZIP, LZMA, DELATED, STORED(default DEFLATED)  
MyZip.add('fn1', 'bytes or str') MyZip.get('fn1')  
# 'bytes or str' MyZip.addf('myfile.txt')  
MyZip.get('myfile.txt') # The content of the file  
# Save the zip file  
import io  
bf = io.BytesIO() # Also can be io.FileIO(filename, 'wb')  
MyZip.flush(bf)  
# if there's no IO given, return a BytesIO object  
bf.getvalue()  # The content of the file The TarFile is the same  
```
