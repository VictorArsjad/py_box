# Python Sandbox

Originally intended for testing out Python, now it contains send_message 
function which can be used to send message to WA number, using the message 
as its parameter.

## Setup
1. Duplicate `credentials.sample.py` file, and rename it as `credentials.py`.
   Leave the sample values as is for now.
2. Register to Nexmo, and setup WA API Sandbox.
3. Once sandbox is setup, you will receive the WA sandbox number. In 
   `credentials.py`, change `nexmo_number` into the sandbox number.
3. Change `wa_number` into your own number (which has the sandbox setup).
4. Utilize the cURL provided by Nexmo to retrieve `user` and `pwd`.
5. in `main.py`, change the sample text into your expected message.


###_Happy Coding!_

