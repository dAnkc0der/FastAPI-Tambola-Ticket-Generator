# FastAPI-Tambola-Ticket-Generator

1. Clone this repository, navigate to this repository, create a virtual environment, and activate the virtual environment and finally install libraries from requirements.txt file
   
   ```git clone **Url link** ```
   
   ```cd Submission-onito```

   ```python -m venv env```

   ```source ./env/Scripts/activate```

   ```pip install -r requirements.txt```

   **Note** - Use Git bash terminal

2. Create a **.env** file and add these parameters to it with your credentials

   ```
    DB_USER=Add your value here
    DB_PASSWORD=Add your value here
    DB_HOST=Add your value here
    DB_PORT=Add your value here
    DB_NAME=Add your value here
   ```

3. Once above requirements are met then start the server -

   `uvicorn main:app --reload`

4. Upon the start of server either navigate to ```localhost:8000/docs``` to use the swagger docs directly or use postman to test the APIs.

5. To test the APIs using postman -

  - POST Request - ```localhost:8000/generate_and_save_tickets/```

    Navigate to body -> raw -> from dropdown select json  

    ```
    {
      "number_of_tickets": 4
    }
    ```

    - Response

      ```
          {
              "tickets": {
                  "1": [
                      "[0,13,0,35,0,53,63,0,81]",
                      "[0,14,0,0,48,59,0,78,86]",
                      "[5,20,27,37,0,0,0,0,0]"
                  ],
                  "2": [
                      "[0,14,22,0,41,0,0,72,81]",
                      "[9,18,0,0,47,53,0,0,0]",
                      "[0,0,25,36,49,60,0,0,82]"
                  ]
              }
        }
      ```

  - GET Request - ```localhost:8000/get_tickets?page=1&page_size=15```

    Navigate to params and add the following key and values.

    ```
    page - 1
    page_size - 10
    ```

    - Response

      ```
      {
          "tickets": {
              "1": [
                  "[0, 14, 0, 0, 41, 0, 65, 74, 83]",
                  "[3, 0, 0, 0, 45, 56, 0, 79, 86]",
                  "[5, 19, 21, 38, 0, 0, 69, 0, 0]"
              ],
              "2": [
                  "[5, 11, 0, 0, 45, 51, 63, 0, 0]",
                  "[0, 18, 22, 0, 0, 59, 66, 74, 0]",
                  "[0, 19, 25, 33, 0, 0, 70, 78, 0]"
              ],
              "3": [
                  "[3, 0, 21, 0, 49, 0, 61, 78, 0]",
                  "[0, 11, 25, 0, 0, 51, 68, 0, 0]",
                  "[0, 13, 0, 35, 0, 58, 0, 0, 84]"
              ],
              "4": [
                  "[8, 13, 0, 0, 0, 56, 0, 79, 88]",
                  "[0, 0, 23, 31, 42, 58, 0, 0, 89]",
                  "[10, 15, 29, 33, 49, 0, 0, 0, 0]"
              ],
              "5": [
                  "[3, 0, 26, 38, 0, 0, 61, 73, 0]",
                  "[5, 0, 0, 31, 49, 0, 63, 75, 0]",
                  "[0, 17, 0, 39, 50, 0, 69, 0, 88]"
              ]
          }
      }
    ```
