EN
==

1.BASIC
--
This is a script for tracking the most famous currencies!

```
BCH
BTC
BTG
BYN
CAD
CHF
CNY
ETH
EUR
GBP
GEL
IDR
JPY
LKR
MDL
MMK
RSD
RUB
THB
USD
XRP
ZEC
```


2.FUNCTIONS
--
1. Set the scan interval
2. Select the ratio of the two currencies
3. Writing price history to a file
4. The script keeps a log of operations (logging)


3.USAGE HOWTO
--

Let's say you have nothing to do and you decide to monitor the exchange rate.
To do this, run the script and enter the time interval after which the currency will be checked

1.CHOOSE THE VERIFICATION INTERVAL
>
>![image](https://user-images.githubusercontent.com/79650307/225620215-a9d817e1-80f7-4f41-8bf1-a0102aa48144.png)
>
>In my case time = 10 seconds

2.CHOOSE YOUR MAIN CURRENCY
>![image](https://user-images.githubusercontent.com/79650307/225622031-8e2a6cf0-462f-4d6d-9cbd-d8fcc72ea491.png)
>
>Here is a dollar 

3.CHOOSE A SECOND CURRENCY
>
>![image](https://user-images.githubusercontent.com/79650307/225622370-35e30619-cd99-4bb7-998f-5357c3744ee0.png)
>
>We chose the second currency as Bitcoin.
>We press enter and we see that one dollar is equal to the number of bitcoins there.
>Work has begun!

4.WE LOOK
>
>![image](https://user-images.githubusercontent.com/79650307/225623299-3cdf69e3-45dd-4f4e-800c-9ed156eb9746.png)
>
>Here you can see that one dollar is worth that many bitcoins first and then after 10 seconds (almost). The red mark means everything is fine. Below, under the red >mark, the difference is marked: that is, the currency has not changed in 10 seconds.
>


5.LOGGING
>Please note that each request is logged to a file, and there is also a request history file!
>
>![image](https://user-images.githubusercontent.com/79650307/225626728-36df2a4c-9a6c-4e91-af57-963f63d26ebe.png)
>
>![image](https://user-images.githubusercontent.com/79650307/225627412-fc48c61c-9fce-4c1c-ac3d-362b186482ef.png)




4.API
--
Site used for the script: <a href ='https://currate.ru'>https://currate.ru<a>

5.ERROR PROCESSING 
--

``The script keeps a log of successful and unsuccessful operations.``

If the request to the site is successful, it will be displayed in the log and the program will continue to work.

Otherwise, an error message will be written, and will be displayed until the request is successful again.

if you  enter wrong API_KEY from config.py
>
>![image](https://user-images.githubusercontent.com/79650307/225626245-595df655-ad6f-4381-8d42-b6d08f5a6cf1.png)

>
