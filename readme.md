
#### Local Build Deployment And Testing Information

| Sl No | Purpose                     | Command                                                                  |
|-------|-----------------------------|--------------------------------------------------------------------------|
| 1     | Build Image                 | `docker compose build temperature-conversion-api`                        |
| 2     | Run Tests                   | `docker compose run temperature-conversion-api  pytest --cov=api tests/` |
| 3     | Deploy application          | `docker compose up temperature-conversion-api `                          |
| 4     | Url EndPoint                | http://localhost:8000/graphql                                            |
| 5     | API docs and PlayGround URL | http://localhost:8000/graphql                                            |


#### Curl Script for calling the API Locally After Deployment

##### Degree Celsius to Fahrenheit Conversion
`curl -g -X POST -H "Content-Type: application/json"  
-d '{"query":"mutation {
  convertTemperature(inputTemperature: 68569.22, unitToConvert: FAHRENHEIT) {
    unit
    value
    convertedAt
  }
}"}' 
http://localhost:8000/graphql `

##### Fahrenheit to Degree Celsius Conversion
`curl -g -X POST -H "Content-Type: application/json"  
-d '{"query":"mutation {
  convertTemperature(inputTemperature: 123456.6, unitToConvert: DEGREE_CELSIUS) {
    unit
    value
    convertedAt
  }
}"}' 
http://localhost:8000/graphql `

> **Additional Note**: **_GraphQL servers can be configured to either accept Request via POST or GET method._**
> **_This application uses POST method to handle the request_**

