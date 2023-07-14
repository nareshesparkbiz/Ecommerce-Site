let accessToken="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MzIwNTY5LCJpYXQiOjE2ODkzMTY5NjksImp0aSI6IjM0N2IyYjM1ZmRmMjRmMWRiZjU1OWU4NGE3MzEzMGNkIiwidXNlcl9pZCI6Mn0.w1N9GitlfyL36eRMa4otIEKaY5DipMsMibKWcCWmcm0"

 export const BaseApi:string="http://127.0.0.1:8000/"

 export const headers:{'Authorization':string,'content-type':string}={'Authorization': `Bearer ${accessToken}`,"content-type":'application/json'} 