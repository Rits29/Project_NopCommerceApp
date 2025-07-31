#!/bin/bash


pytest -v -s -m "sanity" --html=Reports/report.html
# pytest -v -s -m "sanity or regression" --html=Reports/report.html
# pytest -v -s -m "regression" --html=Reports/report.html
# pytest -v -s -m "sanity and regression" --html=Reports/report.html


#rem the one which you want to execute leave that and comment the remaining lines by using rem. In windows use rem and in Linux use #. in windows file name is run.bat and in linux its run.sh. and by using chmod +x run.sh cmd in cmp-prompt we need to make the file executable in Linux.
