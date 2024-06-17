Introduction:
This is a customer complaint management application with backend built using AWS serverless services such as API GW, Lambda, Cognito, Dynamodb, SES, IAM.

![image](https://github.com/marivalan/customer_complaint_management-/assets/128570012/102c88bf-64be-46eb-b524-3a227476c713)
     -From the desktop application for which the code is provided in the serverless.py file we access cognito through boto3 SDK to create users and to authenticate.
     -With tokens recieved from cognito we can access api gw where cognito authorizer validates the tokens, once validated the apigw invokes lambda fuction which stores data on dynamodb.
     -Dynamodb stream invokes a lambda whenever a item is inserted or modified in dynamodb, lambda sends mail to user via SES.
     -IAM roles and policies are created to delegate permissions for cross-service access.

