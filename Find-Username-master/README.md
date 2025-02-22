In Tools (tools dir)
    - Start the docker desktop
    - pip install --upgrade aiohttp aiohttp_socks
    - set PYTHONIOENCODING=utf-8


    ls/blackbird
        - pip3 install -r requirements.txt
    
    ls/marple
        - pip3 install -r requirements.txt
    
    ls/sherlock
        - pip3 install -r requirements.txt
        - winpty docker run -it --rm sherlock/sherlock

In ./ (Project dir)
    - npm i axios, cors, dotenv, express, http-status-codes, http, node, nodemon

Changes
    - [.env file in ./] write the port number in there
    - Change the path for tools in ./src/utils/common/paths.js