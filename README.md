
<div aloigh='center'>
  
![logo](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/63f3ccb8-e71c-4135-8b67-358bb3a72c49)

</div>

## BASIC

This program is designed to monitor the change of two currencies.


- Python: `=>3.7`

- Package manager: <a href='https://python-poetry.org/'>poetry</a>

- API: <a href='https://freecurrencyapi.com/'>open site<a/>



<details>
 <summary>Able currencies</summary>
  
  ```
  USD
  RUB
  EUR
  AUD
  AZN
  GBP
  AMD
  BYN
  BGN
  BRL
  HUF
  VND
  HKD
  GEL
  DKK
  AED
  EGP
  INR
  IDR
  KZT
  CAD
  QAR
  KGS
  CNY
  MDL
  NZD
  NOK
  PLN
  RON
  XDR
  SGD
  TJS
  THB
  TRY
  TMT
  UZS
  UAH
  CZK
  SEK
  CHF
  RSD
  ZAR
  KRW
  JPY
  ```
</details>


## Installation
1. Clone repo
```bash
git clone https://github.com/IvanIsak2000/CURRENCYTRACK.git
```

2. Change folder
 ```bash
 cd src
```

3. Activate `poetry` environment
```bash
poetry shell
```

4. Install dependencies
```bash
poetry install  
```

5. Get `API key`
  - Open <a href='https://freecurrencyapi.com/'>freecurrencyapi</a>
  - Log in 
  -  Copy your `API key`s
     
6. Open `config.py`
   
   Paste your `API key` in `API_KEY`
 
8. Launch program
```bash
python3 main.py
```

## FUNCTIONS

1. Set the scan interval
2. Select the ratio of the two currencies
3. Writing price history to a file
4. The script keeps a log of operations (logging)


## USAGE HOWTO

Let's say you want to track the exchange rate of different currencies, for this follow the launch steps

1.CHOOSE YOUR MAIN CURRENCY
>

2.CHOOSE A SECOND CURRENCY
>![2nd currency](https://user-images.githubusercontent.com/79650307/232417605-c1936382-1217-4fa7-8a1e-4d8be98a4781.png)
>
>We chose the second currency as Bitcoin.
>Also just click on the currency

3.CHOOSE THE VERIFICATION INTERVAL
>![time](https://user-images.githubusercontent.com/79650307/232417724-f2519c79-314f-4b75-92d7-5d51ec37f5a0.png)
>
>In my case time = 10 seconds

4.WE LOOK
>![settings](https://user-images.githubusercontent.com/79650307/232417910-c6639752-9929-4b0e-981a-4bb3347181d4.png)
>
>![result](https://user-images.githubusercontent.com/79650307/232418565-222ef4d3-ab3f-471c-88e9-e6e99caf5a73.png)
>
>Here you can see that one dollar is worth that many bitcoins first and then after 10 seconds (almost). The red mark means everything is fine. Below, under the red >mark, the difference is marked: that is, the currency has not changed in 10 seconds.

5.LOGGING
>Please note that each request is logged to a file, and there is also a request history file!
>
>![image](https://user-images.githubusercontent.com/79650307/225626728-36df2a4c-9a6c-4e91-af57-963f63d26ebe.png)
>
>![windows](https://user-images.githubusercontent.com/79650307/232423286-5943f8cf-2cc4-4aa8-a856-706cec3a98de.png)


## API
This program used <a href='https://freecurrencyapi.com/'>this API<a/>
From website:
- Requests limit: `5000/month`


## ERROR PROCESSING 


``The script keeps a log of successful and unsuccessful operations.``

If the request to the site is successful, it will be displayed in the log and the program will continue to work.

Otherwise, an error message will be written, and will be displayed until the request is successful again.

If you forgot to enter `API_KEY` or it is incorrect from `config.py`
>![if API_KEY is not set](https://user-images.githubusercontent.com/79650307/232423544-638287bf-e097-4417-a02c-ba33251d7a9c.png)

It is also possible to get a `500` error because the `currency.ru` server cannot send data about these currencies, just try to select other currencies
>![500](https://user-images.githubusercontent.com/79650307/232423959-00b172a2-389d-45ef-a22f-b3ce8b596531.png)

