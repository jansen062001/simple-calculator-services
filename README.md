# Simple Calculator Services
Pada arsitektur ini anda diminta untuk membuat sebuah aplikasi kalkulator sederhana yang menghitung / melakukan kalkulasi yang cukup berat. Oleh karena itu anda diminta untuk membuat sebuah aplikasi asynchronous dengan memanfaatkan teknologi celery.
## Request: Mencari bilangan prima yang ke `<index>`
![GET](https://badgen.net/badge/Method/GET/green)**/api/prime/`<int:index>`**


### Responses:
#### Bilangan prima ke `<index>`
![OK](https://badgen.net/badge/OK/200/green)
```json
{
    "result": 47
}
```
#### Bilangan prima ke `<index>` (Not found)
![Not Found](https://badgen.net/badge/Not%20Found/404/red)
```json
{
    "status": "error",
    "message": "Not found"
}
```

## Request: Mencari bilangan prima palindrome ke `<index>`
![GET](https://badgen.net/badge/Method/GET/green)**/api/prime/palindrome/`<int:index>`**


### Responses:
#### Bilangan prima palindrome ke `<index>`
![OK](https://badgen.net/badge/OK/200/green)
```json
{
    "result": 727
}
```
#### Bilangan prima palindrome ke `<index>` (Not found)
![Not Found](https://badgen.net/badge/Not%20Found/404/red)
```json
{
    "status": "error",
    "message": "Not found"
}
```