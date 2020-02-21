IF %PROCESSOR_ARCHITECTURE%==x86 set DIRECTORY="C:\Program Files\WordListGenerator"
ELSE set DIRECTORY="C:\Program Files(x86)\WordListGenerator"

mkdir %DIRECTORY%
copy *.* %DIRECTORY%\*.*
mkdir %DIRECTORY%\lib
copy lib\*.* %DIRECTORY%\lib\*.*