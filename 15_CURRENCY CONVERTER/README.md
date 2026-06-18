# Project 16 — Currency Converter

## What it does

A terminal currency converter that fetches live exchange rates from the
ExchangeRate-API. Users can list all supported currencies, check the
exchange rate between two currencies, or convert a specific amount from
one currency to another. The program runs in a loop until the user quits.

## What I learned

- How to use the `requests` library to call a real-world financial API
  and work with live, constantly changing data
- How to use f-strings to build dynamic URLs that insert variables
  like the API key and currency codes directly into the request
- How to validate API responses by checking a `result` field before
  trusting the data — preventing the program from crashing on bad input
- How to use `try/except` around a type conversion (`float(amount)`)
  to catch invalid user input gracefully
- How to structure a program with separate functions for each
  responsibility — fetching data, displaying data, calculating rates,
  and converting amounts
- How to use `.upper()` to normalise currency codes so input is not
  case-sensitive

## What was hard

- Making sure invalid currency codes were caught before attempting
  to access them in the rates dictionary

## What I would add next

- Cache exchange rates locally for a few minutes to avoid hitting
  API rate limits on repeated conversions
- Add a history log of all conversions performed in a session
- Support converting multiple amounts at once
- Add error handling for network failures using a try/except around
  the requests call itself
