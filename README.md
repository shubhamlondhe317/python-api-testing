# Steps for allure :
1) Download the file from  https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/
   Download version 2.17.2
2) Extract this file in new folder like /allure_package
3) command : 
   sudo ln -s ~/Documents/allure_package/allure-2.17.2/bin/allure /usr/local/bin/allure


# Steps for generating allure reports:
1) pytest -s -v test/ --alluredir=reports
2) allure serve reports