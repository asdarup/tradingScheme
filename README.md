# Trading Sheams
1. Get the basic functions operational
2. Add relevant paramaters and fine tune the then 
3. Look into options trading 

Workflow
     
price_data = dataset containing prise data of 100 potential traids,
params_main = paramaters given by a parameter sweep using price_data
trading_main = dataset containing prise and trade data of 100 paper trades using params_main 
params_alt = paramaters given by a parameter sweep using price data from trading_data_main

if trading_data is profitable 
    while trading_data_main is profitable 
        trading_data_main = dataset containing prise and trade data of 100 traides using params_main
        trading_data_alt = dataset containing prise and trade data based on price data from trading_data_main and params_alt
    
        if trading_data_alt is more profitable then trading_data
            params_main = params_alt
    
        params_alt = paramaters given by a parameter sweep using price data from trading_data_main

