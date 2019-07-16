# Todo_App_with_Flask-
Create a TODO App using Flask
# From : https://stackabuse.com/building-a-todo-app-with-flask-in-python/


#####  URL and curl example.
    POST DATA 
    URL : http://127.0.0.1:5000/item/new
    
    ```
curl -X POST  http://127.0.0.1:5000/item/new -d '{"item": "Adding no
tes", "status":"In Progress"}' -H  'Content-Type: application/json'
   ```
    REMOVE DATA
    URL : http://127.0.0.1:5000/item/remove
    ```
    curl -X DELETE  http://127.0.0.1:5000/item/remove -d '{"item": "Adding notes"}' -H  'Content-Type: application/json'
    ```

    UPDATE DATA
    URL : http://127.0.0.1:5000/item/update
    ```
    curl -X PUT http://127.0.0.1:5000/item/update -d '{"item": "Setting up Flask", "status": "Completed"}' -H 'Content-Type: application/json'
    ```


    GET ALL TODO's
    URL : http://127.0.0.1:5000/items/all
    ```
    curl -X GET http://127.0.0.1:5000/items/all
    ```
    CHECK TODO's Status
    URL :  ttp://127.0.0.1:5000/item/status
    ```
    curl -X GET http://127.0.0.1:5000/item/status?name=Setting+up+Flask
    ```


## TODO
    1. Refine each api
    2. Add categories to the DB
    3. Think and add more allong the way.