<div alight='center'>
  
  ![logo](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/63f3ccb8-e71c-4135-8b67-358bb3a72c49)

</div>

# BASIC

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1500&repeat=false&width=800&height=30&lines=This+program+is+designed+to+monitor++the+change+of+two+currencies.)](https://git.io/typing-svg) 

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1500&repeat=false&width=800&height=30&lines=Python+%3D%3E+3.7)](https://git.io/typing-svg)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1500&repeat=false&width=800&height=30&lines=Package+manager%3A+poetry)](https://git.io/typing-svg)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1500&repeat=false&width=800&height=30&lines=API%3A+freecurrencyapi.com)](https://git.io/typing-svg)

# Main currencies

```
USD
EUR
RUB
```

<details>
 <summary>Other currencies</summary>
  
  ```
  AED
  AMD
  AUD
  AZN
  BGN
  BRL
  BYN
  CAD
  CHF
  CNY
  CZK
  DKK
  EGP
  EUR
  GBP
  GEL
  HKD
  HUF
  IDR
  INR
  JPY
  KGS
  KRW
  KZT
  MDL
  NOK
  NZD
  PLN
  QAR
  RON
  RSD
  RUB
  SEK
  SGD
  THB
  TJS
  TMT
  TRY
  UAH
  USD
  UZS
  VND
  XDR
  ZAR
  ```
</details>

<br>

# Installation

1. Clone repo:
```bash
git clone https://github.com/IvanIsak2000/CURRENCYTRACK.git
```

2. Change folder:
 ```bash
 cd src
```

3. Activate `poetry` environment:
```bash
poetry shell
```

4. Install dependencies:
```bash
poetry install  
```

5. Get `API key`:
  - Open <a href='https://freecurrencyapi.com/'>freecurrencyapi</a>
  - Log in 
  -  Copy your `API key`s
     
6. Open `config.py`:
   
   Paste your `API key` in `API_KEY`
 
8. Launch program:
```bash
python3 main.py
```



# FUNCTIONS

  1. Set the scan interval
  2. Select the ratio of the two currencies
  3. Writing price history to a file
  4. The script keeps a log of operations (logging)


# How use

Let's say you want to track the exchange rate of different currencies, for this follow the launch steps

  1.CHOOSE YOUR MAIN CURRENCY
  >![main_currency](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/97934fe6-6fc8-40b2-99fe-375f03b55e27)
  
  2.CHOOSE A SECOND CURRENCY
  >![second_currency](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/9e775757-fb0f-43a1-9b2d-9abc1cde8cda)
  
  
  3.CHOOSE THE VERIFICATION INTERVAL
  >![time](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/ac8711cd-b3eb-4a20-9f1e-1e09fc9cb9f4)
  
  
  4.WE LOOK
  >![set as](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/e552af1c-fa53-4cca-b179-1289e716572a)
  
  
  >![result](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/35880516-a77c-4ce7-9b1b-24f5237d0ec9)
  
  5.LOGGING
  >Please note that each request is logged to a file, and there is also a request history file!
  >
  >![files](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/65a6f296-1289-46c1-8e82-bb35cef8c620)
  
  >First file contain history:
  >
  >![history](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/593b45e5-7f3a-41b5-9226-3992e5a285cb)
  
  >Second file contain all log data:
  >
  >![log file](https://github.com/IvanIsak2000/CURRENCYTRACK/assets/79650307/632787ac-87b1-4963-95fd-55ef0c694241)



# API

This program used <a href='https://freecurrencyapi.com/'>this API</a>
- Requests limit: `5000/month`



# ERROR PROCESSING 

`The program is logging`

Let's say an API check – if the site responds that the key was wrong - the site will return a 401 error, which will be displayed to the user.
To fix the error you need to restart the program.