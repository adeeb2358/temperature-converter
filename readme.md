#### Requirement
>Write an HTTP API that takes a temperature value in 
>Celsius as input and gives the equivalent temperature 
>in Fahrenheit as the output. The same API endpoint should also be able to take the 
> temperature in Fahrenheit and output the equivalent temperature in Celsius. 

#### Technical Design Thoughts

| Sl No | Suggestion                                                                                                                    | Additional Note                                                                                                             |
|-------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 1     | The API should be easy to maintain                                                                                            |                                                                                                                             |
| 2     | Avoid boiler plate code                                                                                                       | Maximize the use of already tested open source libraries                                                                    |  
| 3     | The framework/technology should be 'code-wise' scalable                                                                       | Should be easily able to change features on the go                                                                          |  
| 4     | Maintainable code with less over head                                                                                         |                                                                                                                             |  
| 5     | The existing backend implementation should not get too much affected when additional requirements comes in                    |                                                                                                                             |
| 6     | Error handling should be automatically handled through framework(for majority scenarios)                                      |                                                                                                                             |
| 7     | The technology should well support existing HTTP clients                                                                      |                                                                                                                             |
| 8     | There should be a mechanism inbuilt in the framework to give only necessary details on every particular request               |                                                                                                                             |
| 9     | Framework should support asynchronous requests                                                                                |                                                                                                                             |
| 10    | It should have support for major database vendors and different kinds of databases                                            |                                                                                                                             |
| 11    | The developing service should be 100 % federated service                                                                      | Federated service means, data and the associated application <br/>should be absolutely isolated from the rest of the system |
| 12    | The framework itself should have good support for Integration and Unit Testing                                                |                                                                                                                             |
| 13    | The framework should have support for a well known service discovery system(or for a better Backend for frontend layer-> BFF) |                                                                                                                             |
| 14    | It should be way better if we can choose same end point to serve multiple request with out touching existing service          |                                                                                                                             |
| 15    | The framework + code should have light memory foot print and less prone to vulnerabilities                                    |                                                                                                                             |
| 16    | The framework should have inbuilt support for permission hooks                                                                | Authorization and authentication can be easily controlled through these hooks                                               |

#### What are the problems with traditional rest apis interfaces?
 
| Sl No | Pain points                                                                  | Additional Note                                                   |
|-------|------------------------------------------------------------------------------|-------------------------------------------------------------------|
| 1     | Less flexibility over leveraging existing service                            | Most of the times modification to existing interface is necessary |
| 2     | Joining data from two services to the front end will be additional over head |                                                                   |
| 3     | Custom error handling should be done separately                              |                                                                   |

Points which has not been included are as follows (It is not mentioned in the requirement)


By considering the above points and below are the technical design choices made.


> By looking at the above pain points, my conclusion was to use graphql instead of traditional rest API.
> There are some disadvantage as we can either go for a POST or GET request mode in a graphql server.
> After looking at various options , My decision was to choose python as the programming language and chose strawberry
> python as the framework. Even though it is a relatively new framework , the support for appolo gateway,
> asynchronous programming and federation approach
> led me using it. By comparing the tradditional graphql framework, strawberry has data first approach .
> Were we design the data model first and then the schema and 


##### Local Build Deployment And Testing Information

| Sl No | Purpose                     | Command                                                                     |
|-------|-----------------------------|-----------------------------------------------------------------------------|
| 1     | Build Image                 | `docker compose build temperature-conversion-api`                           |
| 2     | Run Tests                   | `docker compose run temperature-conversion-api  pytest --cov=api tests/ -v` |
| 3     | Deploy application          | `docker compose up temperature-conversion-api `                             |
| 4     | API EndPoint                | http://localhost:8000/graphql                                               |
| 5     | API docs and PlayGround URL | http://localhost:8000/graphql                                               |


#### Curl Script for calling the API Locally After Deployment

##### Degree Celsius to Fahrenheit Conversion
`curl -g -X POST -H "Content-Type: application/json"  
-d '{"query":"mutation {
  convertTemperature(inputTemperature: 68569.22, unitToConvert: FAHRENHEIT) {
    unit,
    value,
    convertedAt
  }
}"}' 
http://localhost:8000/graphql `

##### Fahrenheit to Degree Celsius Conversion
`curl -g -X POST -H "Content-Type: application/json"  
-d '{"query":"mutation {
  convertTemperature(inputTemperature: 123456.6, unitToConvert: DEGREE_CELSIUS) {
    unit,
    value,
    convertedAt
  }
}"}' 
http://localhost:8000/graphql `

> **Additional Note**: **_GraphQL servers can be configured to either accept Request via POST or GET method._**
> **_This application uses POST method to handle the request_**

