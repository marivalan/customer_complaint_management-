import tkinter as tk
import boto3
import requests

cog = boto3.client('cognito-idp', region_name='ap-south-1')

root = tk.Tk()
root.title("customer_compliant_management")
root.geometry("430x400")

#creating entries, labels and functions for window_1

l1_username = tk.Label(text="User Name")
l1_username.grid(column=0, row=4, padx=(50,0), pady=(20, 0))
l1_password = tk.Label(text="Password")
l1_password.grid(column=0, row=5, padx=(50,0))
l1_notice = tk.Label(text="Select user type")
l1_notice.grid(column=0, row=0, columnspan=2)

e1_username = tk.Entry(width=35)
e1_username.grid(column=1, row=4, padx=(50, 40), pady=(20, 0))
e1_password = tk.Entry(width=35)
e1_password.grid(column=1, row=5,padx=(50, 40))

employee_pool_Client_ID = '16aojtq6q5beh7ptto9rlhiir0'
customer_pool_Client_ID = '5kv7v304h4ao62rf7h1euo71bv'

post_url_c = 'https://d0el873e53.execute-api.ap-south-1.amazonaws.com/CCM/'
put_url_c = 'https://d0el873e53.execute-api.ap-south-1.amazonaws.com/CCM/update'
get_url_c = 'https://d0el873e53.execute-api.ap-south-1.amazonaws.com/CCM/'

post_url_e = 'https://zbn890lj60.execute-api.ap-south-1.amazonaws.com/CCM-E/CCM-E'
put_url_e = 'https://zbn890lj60.execute-api.ap-south-1.amazonaws.com/CCM-E/CCM-E/update'
get_url_e = 'https://zbn890lj60.execute-api.ap-south-1.amazonaws.com/CCM-E/CCM-E/'


def signup():
    var1 = Checkbutton1_a.get()
    var2 = Checkbutton1_b.get()

    if var1 == 1 and var2 == 0:  #employee signup
        # creating a new window and entries, lables
        reg = tk.Tk()
        reg.title("Register")
        reg.geometry("380x380")

        l2_username = tk.Label(reg, text="User Name")
        l2_username.grid(column=0, row=1)
        l2_mailid = tk.Label(reg, text="Mail id")
        l2_mailid.grid(column=0, row=2)
        l2_password = tk.Label(reg, text="Password")
        l2_password.grid(column=0, row=4)
        l2_info = tk.Label(reg, text="Password must contain at least one capital letter and one number")
        l2_info.grid(column=0, row=5, columnspan=2)
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

    elif var1 == 0 and var2 == 1:  #customer signup
        # creating a new window and entries, lables
        reg = tk.Tk()
        reg.title("Register")
        reg.geometry("380x380")

        l2_username = tk.Label(reg, text="User Name")
        l2_username.grid(column=0, row=1)
        l2_mailid = tk.Label(reg, text="Mail id")
        l2_mailid.grid(column=0, row=2)
        l2_password = tk.Label(reg, text="Password")
        l2_password.grid(column=0, row=4)
        l2_info = tk.Label(reg, text="Password must contain at least one capital letter and one number")
        l2_info.grid(column=0, row=5, columnspan=2)
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
                print(response)
            except Exception:
                l_confirmation = tk.Label(reg, text='Confirmation failed')
                l_confirmation.grid(column=1, row=11)
                return None
            else:
                l_confirmation = tk.Label(reg, text='Confirmed')
                l_confirmation.grid(column=1, row=11)
            finally:
                def sigin():
                    clientid_c = customer_pool_Client_ID
                    authparameters_c = {
                        'USERNAME': e2_username.get(),
                        'PASSWORD': e2_password.get()
                    }
                    global cred
                    cred = cog.initiate_auth(  # calling sign_in method
                        AuthFlow="USER_PASSWORD_AUTH",
                        AuthParameters=authparameters_c,
                        ClientId=clientid_c
                    )
                    return cred

                def store_user_data():
                    text = {"userid": e2_username.get(),
                            "mailid": e2_mailid.get()
                            }
                    id_token = str(Token['AuthenticationResult']['IdToken'])
                    body = requests.post(post_url_c, json=text,
                                         headers={'Authorization': f'Bearer {id_token}',
                                                  'Content-Type': 'application/json'})
                    return body

                def signout():
                    accesstoken = str(Token['AuthenticationResult']['AccessToken'])
                    out = cog.global_sign_out(
                        AccessToken=accesstoken
                    )
                    return out

                sigin()
                Token = cred
                store_user_data()
                signout()

        b2_register = tk.Button(reg, text="Save to register", command=save_to_register)
        b2_register.grid(column=0, row=7, columnspan=2)
        b2_confirm = tk.Button(reg, text="Confirm user", command=confirm)
        b2_confirm.grid(column=0, row=9, columnspan=2)

        reg.mainloop()
    else:
        warning_label = tk.Label(root, text="Select one of the above category")
        warning_label.grid(column=0, row=2, columnspan=2)


def signin():
    def initiate_signin(authflow, clientid, authparameters):  #sign_in method
        response = cog.initiate_auth(
            AuthFlow=authflow,
            AuthParameters=authparameters,
            ClientId=clientid
        )
        global Tokens
        Tokens = response
        print(Tokens)
        global id_token
        id_token = str(Tokens['AuthenticationResult']['IdToken'])
        return response

    var1 = Checkbutton1_a.get()
    var2 = Checkbutton1_b.get()

    if var1 == 1 and var2 == 0:  #employee signin authflow
        try:
            authflow_e = 'USER_PASSWORD_AUTH'
            clientid_e = employee_pool_Client_ID
            authparameters_e = {
                'USERNAME': e1_username.get(),
                'PASSWORD': e1_password.get()
            }
            initiate_signin(authflow_e, clientid_e, authparameters_e)  # calling initiate_sign in fn
        except Exception:
            l_feedback = tk.Label(root, text="Incorrect username or Password")
            l_feedback.grid(column=0, row=6, columnspan=2)
        else:
            # creating an employee signin page
            sign = tk.Tk()
            sign.title("Sign In")
            sign.geometry("430x480")

            l_sign_customer = tk.Label(sign, text="Customer Name")
            l_sign_customer.grid(column=0, row=1, padx=(40,0), pady=(20, 0))
            l_sign_mailid = tk.Label(sign, text="Mail id")
            l_sign_mailid.grid(column=0, row=3, padx=(40,0))
            l_sign_product = tk.Label(sign, text="Product")
            l_sign_product.grid(column=0, row=4, padx=(40,0))
            l_sign_complaint = tk.Label(sign, text="Complaint")
            l_sign_complaint.grid(column=0, row=5, padx=(40,0))
            l_sign_response = tk.Label(sign, text="Response")
            l_sign_response.grid(column=0, row=6, padx=(40,0))

            e_sign_customer = tk.Entry(sign, width=35)
            e_sign_customer.grid(column=1, row=1, padx=(30,0), pady=(20, 0))
            e_sign_mailid = tk.Entry(sign, width=35)
            e_sign_mailid.grid(column=1, row=3, padx=(30,0))
            e_sign_product = tk.Entry(sign, width=35)
            e_sign_product.grid(column=1, row=4, padx=(30,0))

            t_sign_complaint = tk.Text(sign, height=10, width=26)
            t_sign_complaint.grid(column=1, row=5, padx=(30,0))
            t_sign_response = tk.Text(sign, height=5, width=26)
            t_sign_response.grid(column=1, row=6, padx=(30,0))

            def signout():  # defining functions for buttons in signin page
                accesstoken = str(Tokens['AuthenticationResult']['AccessToken'])
                response = cog.global_sign_out(
                    AccessToken=accesstoken
                )
                print(response)
                return response

            def send():  # defining functions for buttons in signin page
                try:
                    this = t_sign_response.get("1.0", "end-1c")
                    if this == "Response sent" or not this or this == "Could not fetch data" or this == "Could not send response":
                        return
                    else:
                        text = {"userid": e_sign_customer.get(),
                                "reply": this
                                }
                        body = requests.put(put_url_e, json=text,
                                            headers={'Authorization': f'Bearer {id_token}',
                                                     'Content-Type': 'application/json'})
                        print(body)
                        t_sign_response.delete('1.0', tk.END)
                        t_sign_response.insert('1.0', 'Response sent')
                except Exception:
                    t_sign_response.delete('1.0', tk.END)
                    t_sign_response.insert('1.0', 'Could not send response')
                return

            def show():  # defining response retrieval for employee
                try:
                    t_sign_complaint.delete('1.0', tk.END)
                    t_sign_response.delete('1.0', tk.END)
                    e_sign_product.delete(0, tk.END)
                    e_sign_mailid.delete(0, tk.END)

                    params = {"userid": e_sign_customer.get()}
                    id_token = str(Tokens['AuthenticationResult']['IdToken'])
                    url = get_url_e + "single"
                    body = requests.get(url, params=params,
                                        headers={'Authorization': f'Bearer {id_token}',
                                                 'Content-Type': 'application/json'})
                    print(body)
                    print(body.json())
                    content = body.json()['Item']['complaint']
                    pro = body.json()['Item']['product']
                    mail = body.json()['Item']['mailid']
                    e_sign_product.insert("0", pro)
                    e_sign_mailid.insert("0", mail)
                    if content is None:
                        t_sign_complaint.insert('1.0', 'No complaint')
                    else:
                        t_sign_complaint.insert('1.0', content)
                        pass
                except Exception:
                    t_sign_response.insert('1.0', "Could not fetch data")
                return

            def list():
                allcustomers = tk.Tk()
                allcustomers.title("Customers data")
                allcustomers.geometry("430x480")

                id_token = str(Tokens['AuthenticationResult']['IdToken'])
                url = get_url_e + "all"
                body = requests.get(url,
                                    headers={'Authorization': f'Bearer {id_token}',
                                             'Content-Type': 'application/json'})
                print(body)
                data = body.json()['Items']
                print(data)

                def label(username, complaint, product, x):
                    l2_username = tk.Label(allcustomers, text=username)
                    l2_username.grid(column=1, row=x)
                    l2_username = tk.Label(allcustomers, text=complaint)
                    l2_username.grid(column=2, row=x)
                    l2_username = tk.Label(allcustomers, text=product)
                    l2_username.grid(column=3, row=x)
                    return

                x = int(0)
                for i in data:
                    x += 1
                    u_name = i['userid']
                    comp = i['complaint']
                    pro = i['product']
                    label(u_name, comp, pro, x)
                l2_username = tk.Label(allcustomers, text="Customer Name")
                l2_username.grid(column=1, row=0)
                l2_username = tk.Label(allcustomers, text="Complaint")
                l2_username.grid(column=2, row=0)
                l2_username = tk.Label(allcustomers, text="Product")
                l2_username.grid(column=3, row=0)

                allcustomers.mainloop()
                return

            b_sign_show = tk.Button(sign, text="Show", command=show)
            b_sign_show.grid(column=1, row=2)
            b_sign_send = tk.Button(sign, text="Send", command=send)
            b_sign_send.grid(column=1, row=7)
            b_sign_signout = tk.Button(sign, text="Sign out", command=signout)
            b_sign_signout.grid(column=0, row=8, padx=(80,0), pady=(30, 20))
            b_sign_list = tk.Button(sign, text="Customers' list", command=list)
            b_sign_list.grid(column=1, row=8, padx=(40,0), pady=(30, 20))

            sign.mainloop()

    elif var1 == 0 and var2 == 1:  #customer signin authflow
        try:
            authflow_c = 'USER_PASSWORD_AUTH'
            clientid_c = customer_pool_Client_ID
            authparameters_c = {
                'USERNAME': e1_username.get(),
                'PASSWORD': e1_password.get()
            }
            initiate_signin(authflow_c, clientid_c, authparameters_c)  # calling initiate_sign in fn
        except Exception:
            l_feedback = tk.Label(root, text="Incorrect username or Password")
            l_feedback.grid(column=0, row=6, columnspan=2)
        else:
            # creating a customer signin page
            sign = tk.Tk()
            sign.title("Sign In")
            sign.geometry("350x435")

            l_sign_product = tk.Label(sign, text="Product")
            l_sign_product.grid(column=0, row=2, padx=(30,0))
            l_sign_complaint = tk.Label(sign, text="Complaint")
            l_sign_complaint.grid(column=0, row=3, padx=(30,0))
            l_sign_response = tk.Label(sign, text="Response")
            l_sign_response.grid(column=0, row=5, padx=(30,0))

            e_sign_product = tk.Entry(sign, width=35)
            e_sign_product.grid(column=1, row=2)
            t_sign_complaint = tk.Text(sign, height=10, width=26)
            t_sign_complaint.grid(column=1, row=3)
            t_sign_response = tk.Text(sign, height=5, width=26)
            t_sign_response.grid(column=1, row=5)

            def signout():  # defining functions for buttons in signin page
                accesstoken = str(Tokens['AuthenticationResult']['AccessToken'])
                response = cog.global_sign_out(
                    AccessToken=accesstoken
                )
                return response

            def send():  # defining functions for buttons in signin page
                try:
                    thing = e_sign_product.get()
                    this = t_sign_complaint.get("1.0", "end-1c")
                    if this == "Complaint sent" or not thing or not this:
                        return
                    else:
                        text = {"userid": e1_username.get(),
                                "product": thing,
                                "complaint": this
                                }
                        id_token = str(Tokens['AuthenticationResult']['IdToken'])
                        body = requests.put(put_url_c, json=text,
                                            headers={'Authorization': f'Bearer {id_token}',
                                                     'Content-Type': 'application/json'})

                        print(body)
                        t_sign_complaint.delete('1.0', tk.END)
                        t_sign_complaint.insert('1.0', 'Complaint sent')
                except Exception:
                    t_sign_complaint.delete('1.0', tk.END)
                    t_sign_complaint.insert('1.0', 'Could not send the complaint')
                return

            def retrieve():  #defining response retrieval for customer
                e_sign_product.delete(0, tk.END)
                t_sign_complaint.delete('1.0', tk.END)

                params = {"userid": e1_username.get()}
                id_token = str(Tokens['AuthenticationResult']['IdToken'])
                url = get_url_c + "single"
                body = requests.get(url, params=params,
                                    headers={'Authorization': f'Bearer {id_token}', 'Content-Type': 'application/json'})
                print(body)
                pro = body.json()['Item']['product']
                comp = body.json()['Item']['complaint']
                e_sign_product.insert('0', pro)
                t_sign_complaint.insert('1.0', comp)
                try:
                    content = body.json()['Item']['reply']
                    t_sign_response.delete('1.0', tk.END)
                    t_sign_response.insert('1.0', content)
                except Exception:
                    t_sign_response.delete('1.0', tk.END)
                    t_sign_response.insert('1.0', 'No response yet')

            b_sign_send = tk.Button(sign, text="Send", command=send)
            b_sign_send.grid(column=1, row=4)
            b_sign_retrieve = tk.Button(sign, text="Retrieve my data", command=retrieve)
            b_sign_retrieve.grid(column=1, row=1)
            b_sign_signout = tk.Button(sign, text="Sign out", command=signout)
            b_sign_signout.grid(column=1, row=7, pady=(40,0))

            sign.mainloop()

    else:
        warning_label = tk.Label(root, text="Select one of the above category")
        warning_label.grid(column=0, row=2, columnspan=2)
    return


#creating buttons on window_1
Checkbutton1_a = tk.IntVar()
b1_employee = tk.Checkbutton(text="Employee", variable=Checkbutton1_a)
b1_employee.grid(column=0, row=1, padx=(50,0), pady=(10, 0))

Checkbutton1_b = tk.IntVar()
b1_Customer = tk.Checkbutton(text="Customer", variable=Checkbutton1_b)
b1_Customer.grid(column=1, row=1, padx=(30,0), pady=(10, 0))

b1_register = tk.Button(text="Sign up", command=signup)
b1_register.grid(column=1, row=8, padx=(30,0), pady=(30, 50))
b1_signin = tk.Button(text="Sign in", command=signin)
b1_signin.grid(column=0, row=8, padx=(50,0), pady=(30, 50))

root.mainloop()
