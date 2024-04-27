import tkinter as tk
import boto3
import requests

cog = boto3.client('cognito-idp', region_name='ap-south-1')

root = tk.Tk()
root.title("customer_compliant_management")
root.geometry("450x435")

#creating entries, labels and functions for window_1

l1_username = tk.Label(text="User Name")
l1_username.grid(column=0, row=4)
l1_password = tk.Label(text="Password")
l1_password.grid(column=0, row=5)
l1_notice = tk.Label(text="Select user type")
l1_notice.grid(column=0, row=0, columnspan=2)

e1_username = tk.Entry(width=35)
e1_username.grid(column=1, row=4)
e1_password = tk.Entry(width=35)
e1_password.grid(column=1, row=5)

employee_pool_Client_ID = '16aojtq6q5beh7ptto9rlhiir0'
customer_pool_Client_ID = '5kv7v304h4ao62rf7h1euo71bv'

post_url_e = 'https://d0el873e53.execute-api.ap-south-1.amazonaws.com/CCM/'
put_url_e = 'https://d0el873e53.execute-api.ap-south-1.amazonaws.com/CCM/update'
get_url_e= 'https://d0el873e53.execute-api.ap-south-1.amazonaws.com/CCM/'
def signup():
    var1 = Checkbutton1_a.get()
    var2 = Checkbutton1_b.get()

    if var1 == 1 and var2 == 0:
        # creating a new window and entries, lables
        reg = tk.Tk()
        reg.title("Register")
        reg.geometry("450x435")

        l2_username = tk.Label(reg, text="User Name")
        l2_username.grid(column=0, row=1)
        l2_mailid = tk.Label(reg, text="Mail id")
        l2_mailid.grid(column=0, row=2)
        l2_password = tk.Label(reg, text="Password")
        l2_password.grid(column=0, row=4)
        l2_otp = tk.Label(reg, text="OTP")
        l2_otp.grid(column=0, row=8)
        #entries
        e2_username = tk.Entry(reg, width=35)
        e2_username.grid(column=1, row=1)
        e2_mailid = tk.Entry(reg, width=35)
        e2_mailid.grid(column=1, row=2)
        e2_password = tk.Entry(reg, width=35)
        e2_password.grid(column=1, row=4)
        e2_otp = tk.Entry(reg, width=35)
        e2_otp.grid(column=1, row=8)

        def save_to_register():
            try:
                employee_response = cog.sign_up(
                    ClientId=employee_pool_Client_ID,
                    Username=e2_username.get(),
                    Password=e2_password.get(),
                    UserAttributes=[
                        {
                            'Name': 'email',
                            'Value': e2_mailid.get()
                        }
                    ]
                )
                print(employee_response)

            except Exception:
                l_confirmation = tk.Label(reg, text='Signup failed')
                l_confirmation.grid(column=1, row=10)
                return None
            else:
                l_confirmation = tk.Label(reg, text='Awaiting confirmation')
                l_confirmation.grid(column=1, row=10)
            finally:
                pass

        def confirm():
            try:
                response = cog.confirm_sign_up(
                    ClientId=employee_pool_Client_ID,
                    Username=e2_username.get(),
                    ConfirmationCode=e2_otp.get(),
                )
                print(response)
            except Exception:
                l_confirmation = tk.Label(reg, text='Confirmation failed')
                l_confirmation.grid(column=1, row=11)
                return None
            else:
                l_confirmation = tk.Label(reg, text='Confirmed')
                l_confirmation.grid(column=1, row=11)
            finally:
                pass
        b2_register = tk.Button(reg, text="Save to register", command=save_to_register)
        b2_register.grid(column=0, row=7, columnspan=2)
        b2_confirm = tk.Button(reg, text="Confirm user", command=confirm)
        b2_confirm.grid(column=0, row=9, columnspan=2)

        reg.mainloop()

    elif var1 == 0 and var2 == 1:
        # creating a new window and entries, lables
        reg = tk.Tk()
        reg.title("Register")
        reg.geometry("450x435")

        l2_username = tk.Label(reg, text="User Name")
        l2_username.grid(column=0, row=1)
        l2_mailid = tk.Label(reg, text="Mail id")
        l2_mailid.grid(column=0, row=2)
        l2_password = tk.Label(reg, text="Password")
        l2_password.grid(column=0, row=4)
        l2_otp = tk.Label(reg, text="OTP")
        l2_otp.grid(column=0, row=8)

        e2_username = tk.Entry(reg, width=35)
        e2_username.grid(column=1, row=1)
        e2_mailid = tk.Entry(reg, width=35)
        e2_mailid.grid(column=1, row=2)
        e2_password = tk.Entry(reg, width=35)
        e2_password.grid(column=1, row=4)
        e2_otp = tk.Entry(reg, width=35)
        e2_otp.grid(column=1, row=8)

        def save_to_register():
            try:
                customer_response = cog.sign_up(
                    ClientId=customer_pool_Client_ID,
                    Username=e2_username.get(),
                    Password=e2_password.get(),
                    UserAttributes=[
                        {
                            'Name': 'email',
                            'Value': e2_mailid.get()
                        }
                    ]
                )
                print(customer_response)
            except Exception:
                l_confirmation = tk.Label(reg, text='Signup failed')
                l_confirmation.grid(column=1, row=10)
                return None
            else:
                l_confirmation = tk.Label(reg, text='Awaiting confirmation')
                l_confirmation.grid(column=1, row=10)
            finally:
                pass

        def confirm():
            try:
                response = cog.confirm_sign_up(
                    ClientId=customer_pool_Client_ID,
                    Username=e2_username.get(),
                    ConfirmationCode=e2_otp.get(),
                )
                return response
            except Exception:
                l_confirmation = tk.Label(reg, text='Confirmation failed')
                l_confirmation.grid(column=1, row=11)
                return None
            else:
                l_confirmation = tk.Label(reg, text='Confirmed')
                l_confirmation.grid(column=1, row=11)
            finally:
                pass

        b2_register = tk.Button(reg, text="Save to register", command=save_to_register)
        b2_register.grid(column=0, row=7, columnspan=2)
        b2_confirm = tk.Button(reg, text="Confirm user", command=confirm)
        b2_confirm.grid(column=0, row=9, columnspan=2)

        reg.mainloop()
    else:
        warning_label = tk.Label(root, text="Select one of the above category")
        warning_label.grid(column=0, row=7, columnspan=2)
def signin():
    def initiate_signin(authflow, clientid, authparameters):           #sign_in method 
        response = cog.initiate_auth(
            AuthFlow=authflow,
            AuthParameters=authparameters,
            ClientId=clientid
        )
        global Tokens
        Tokens = response
        print(Tokens)
        return response

    var1 = Checkbutton1_a.get()
    var2 = Checkbutton1_b.get()

    if var1 == 1 and var2 == 0:                                     #employee signin authflow
        authflow_e= 'USER_PASSWORD_AUTH'
        clientid_e= employee_pool_Client_ID
        authparameters_e= {
            'USERNAME':e1_username.get(),
            'PASSWORD':e1_password.get()
        }
        initiate_signin(authflow_e, clientid_e, authparameters_e)           # calling initiate_sign in fn

        #creating an employee signin page
        sign = tk.Tk()
        sign.title("Sign In")
        sign.geometry("450x435")

        l_sign_customer = tk.Label(sign, text="Customer Name")
        l_sign_customer.grid(column=0, row=1)
        l_sign_mailid = tk.Label(sign, text="Mail id")
        l_sign_mailid.grid(column=0, row=2)
        l_sign_product = tk.Label(sign, text="Product")
        l_sign_product.grid(column=0, row=3)
        l_sign_complaint = tk.Label(sign, text="Complaint")
        l_sign_complaint.grid(column=0, row=4)
        l_sign_response = tk.Label(sign, text="Response")
        l_sign_response.grid(column=0, row=5)

        e_sign_customer = tk.Entry(sign, width=35)
        e_sign_customer.grid(column=1, row=1)
        e_sign_mailid = tk.Entry(sign, width=35)
        e_sign_mailid.grid(column=1, row=2)
        e_sign_product = tk.Entry(sign, width=35)
        e_sign_product.grid(column=1, row=3)

        t_sign_complaint = tk.Text(sign, height=10, width=26)
        t_sign_complaint.grid(column=1, row=4)

        t_sign_response = tk.Text(sign, height=5, width=26)
        t_sign_response.grid(column=1, row=5)

        def signout():              # defining functions for buttons in signin page
            accesstoken = str(Tokens['AuthenticationResult']['AccessToken'])
            response = cog.global_sign_out(
                AccessToken=accesstoken
            )
            print(response)
            return response

        def send():                 # defining functions for buttons in signin page
            return

        def show():              # defining functions for buttons in signin page

            return

        b_sign_show = tk.Button(sign, text="Show all", command=show)
        b_sign_show.grid(column=2, row=1)
        b_sign_send = tk.Button(sign, text="Send", command=send)
        b_sign_send.grid(column=2, row=5)
        b_sign_signout = tk.Button(sign, text="Sign out", command=signout)
        b_sign_signout.grid(column=1, row=7)

        sign.mainloop()

    elif var1 == 0 and var2 == 1:            #customer signin authflow
        authflow_c = 'USER_PASSWORD_AUTH'
        clientid_c = customer_pool_Client_ID
        authparameters_c = {
            'USERNAME': e1_username.get(),
            'PASSWORD': e1_password.get()
        }
        initiate_signin(authflow_c, clientid_c, authparameters_c)    # calling initiate_sign in fn

        # creating a customer signin page
        sign = tk.Tk()
        sign.title("Sign In")
        sign.geometry("450x435")

        l_sign_product = tk.Label(sign, text="Product")
        l_sign_product.grid(column=0, row=1)
        l_sign_complaint = tk.Label(sign, text="Complaint")
        l_sign_complaint.grid(column=0, row=2)
        l_sign_response = tk.Label(sign, text="Response")
        l_sign_response.grid(column=0, row=3)

        e_sign_product = tk.Entry(sign, width=35)
        e_sign_product.grid(column=1, row=1)
        t_sign_complaint = tk.Text(sign, height=10, width=26)
        t_sign_complaint.grid(column=1, row=2)
        t_sign_response = tk.Text(sign, height=5, width=26)
        t_sign_response.grid(column=1, row=3)

        def signout():          # defining functions for buttons in signin page
            accesstoken = str(Tokens['AuthenticationResult']['AccessToken'])
            response = cog.global_sign_out(
                AccessToken=accesstoken
            )
            print(response)
            return response

        def send():             # defining functions for buttons in signin page
            this = t_sign_complaint.get("1.0","end-1c")
            text = {"userid": e1_username.get(),
                    "product": e_sign_product.get(),
                    "complaint": this
                    }
            id_token = str(Tokens['AuthenticationResult']['IdToken'])
            body = requests.put(put_url_e, json=text, headers={'Authorization': f'Bearer {id_token}', 'Content-Type':'application/json'})
            return body

        b_sign_send = tk.Button(sign, text="Send", command=send)
        b_sign_send.grid(column=2, row=2)
        b_sign_signout = tk.Button(sign, text="Sign out", command=signout)
        b_sign_signout.grid(column=1, row=4)

        sign.mainloop()

    else:
        warning_label = tk.Label(root, text="Select one of the above category")
        warning_label.grid(column=0, row=6, columnspan=2)

    return


#creating buttons on window_1
Checkbutton1_a = tk.IntVar()
b1_employee = tk.Checkbutton(text="Employee", variable=Checkbutton1_a)
b1_employee.grid(column=0,  row=1)

Checkbutton1_b = tk.IntVar()
b1_Customer = tk.Checkbutton(text="Customer", variable=Checkbutton1_b)
b1_Customer.grid(column=1, row=1)

b1_register = tk.Button(text="Sign up", command=signup)
b1_register.grid(column=1, row=8, pady=40)
b1_signin = tk.Button(text="Sign in", command=signin)
b1_signin.grid(column=0, row=8)

root.mainloop()
