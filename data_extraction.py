import pandas as pd
import json
import os



#This is to direct the path to get the data as states

path="C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\aggregated\\transaction\\country\\india\\state\\"
Agg_state_list=os.listdir(path)
#Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe - aggregate_transaction
def ex_data_agg_transaction():
    clm={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
    for i in Agg_state_list:
        p_i=path+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                for z in D['data']['transactionData']:
                    Name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm['Transaction_type'].append(Name)
                    clm['Transaction_count'].append(count)
                    clm['Transaction_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
                    #Succesfully created a dataframe
    Agg_Trans=pd.DataFrame(clm)
    print(Agg_Trans)
    return pd.DataFrame(Agg_Trans)


#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
def ex_data_agg_insurance():
    path="C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\aggregated\\insurance\\country\\india\\state\\"
    Agg_state_list=os.listdir(path)
    #Agg_state_list
    #This is to extract the data's to create a dataframe - aggregate_insurance
    clm={'State':[], 'Year':[],'Quarter':[],'insurance_type':[], 'insurance_count':[], 'insurance_amount':[]}

    for i in Agg_state_list:
        p_i=path+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                for z in D['data']['transactionData']:
                    Name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm['insurance_type'].append(Name)
                    clm['insurance_count'].append(count)
                    clm['insurance_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
                    #Succesfully created a dataframe
    Agg_insur=pd.DataFrame(clm)
                    #print(Agg_insur)
    return pd.DataFrame(Agg_insur)

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
def ex_data_agg_user():
    path="C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\aggregated\\user\\country\\india\\state\\"

    Agg_state_list=os.listdir(path)

#This is to extract the data's to create a dataframe - aggregate_users


    #path="C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\aggregated\\user\\country\\india\\state\\"
    clm = { 
        'State': [], 
        'Year': [],
        'Quarter': [],
        'user_brand': [],
        'user_count': [],
        'user_percentage': []
          }
    for i in Agg_state_list:
        p_i = path + i + "/"
        Agg_yr = os.listdir(p_i)
        for j in Agg_yr:
            p_j = p_i + j + "/"
            Agg_yr_list = os.listdir(p_j)
            for k in Agg_yr_list:
                p_k = p_j + k
                with open(p_k, 'r') as Data:
                    D = json.load(Data)

                         # skip files where usersByDevice is missing or null
                    if ("usersByDevice" not in D["data"]) or (D["data"]["usersByDevice"] is None):
                        continue
                    for z in D["data"]["usersByDevice"]:
                        clm['user_brand'].append(z["brand"])
                        clm['user_count'].append(z["count"])
                        clm['user_percentage'].append(z["percentage"])
                        clm['State'].append(i)
                        clm['Year'].append(j)
                        clm['Quarter'].append(int(k.strip('.json')))
    Agg_users = pd.DataFrame(clm)
    print("___________________")#
    print(Agg_users) 
    return pd.DataFrame(Agg_users)   






#This is to extract the data's to create a dataframe - map_transaction
def ex_map_trans():
    path = "C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\map\\transaction\\hover\\country\\india\\state\\"
    state_list = os.listdir(path)

    clm = {
    'State': [], 'Year': [], 'Quarter': [],
    'District': [], 'Transaction_count': [], 'Transaction_amount': []
          }
    for state in state_list:
        p_state = path + state + "/"
        year_list = os.listdir(p_state)
        for year in year_list:
            p_year = p_state + year + "/"
            file_list = os.listdir(p_year)
            for file in file_list:
                p_file = p_year + file
                with open(p_file, "r") as f:
                    data = json.load(f)
                    for item in data["data"]["hoverDataList"]:
                        district = item["name"]
                        count = item["metric"][0]["count"]
                        amount = item["metric"][0]["amount"]
                        clm["State"].append(state)
                        clm["Year"].append(year)
                        clm["Quarter"].append(int(file.strip(".json")))
                        clm["District"].append(district)
                        clm["Transaction_count"].append(count)
                        clm["Transaction_amount"].append(amount)
    Map_Trans = pd.DataFrame(clm)
                        #print("MAP TRANSACTION")
                        #print(Map_Trans)
    return pd.DataFrame(Map_Trans)

#This is to extract the data's to create a dataframe - map_insurance
def ex_map_insurance():
    path = "C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\map\\insurance\\country\\india\\state\\"

    state_list = os.listdir(path)

    clm = {
     'State': [], 'Year': [], 'Quarter': [],
     'District': [], 'Insurance_metric': []
         }

    for state in state_list:
        p_state = path + state + "/"
        years = os.listdir(p_state)
        for year in years:
            p_year = p_state + year + "/"
            files = os.listdir(p_year)

            for file in files:
                with open(p_year + file, "r") as f:
                    D = json.load(f)

                for row in D["data"]["data"]:
                    district = row[3]
                    metric = row[2]

                    clm["State"].append(state)
                    clm["Year"].append(year)
                    clm["Quarter"].append(int(file.strip(".json")))
                    clm["District"].append(district)
                    clm["Insurance_metric"].append(metric)
                    #print("MAP insurance")
    Map_Insur = pd.DataFrame(clm)
                    #print(Map_Insur)
    return(Map_Insur)


#This is to extract the data's to create a dataframe - map_users
def ex_map_user():
    path = "C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\map\\user\\hover\\country\\india\\state\\"
    state_list = os.listdir(path)

    clm = {
     'State': [], 'Year': [], 'Quarter': [],
     'District': [], 'RegisteredUsers': [], 'AppOpens': []
          }
    for state in state_list:
        p_state = path + state + "/"
        years = os.listdir(p_state)
        for year in years:
            p_year = p_state + year + "/"
            files = os.listdir(p_year)

            for file in files:
                with open(p_year + file, "r") as f:
                    D = json.load(f)

                    for district, info in D["data"]["hoverData"].items():
                        reg = info["registeredUsers"]
                        app = info["appOpens"]
                        clm["State"].append(state)
                        clm["Year"].append(year)
                        clm["Quarter"].append(int(file.strip(".json")))
                        clm["District"].append(district)
                        clm["RegisteredUsers"].append(reg)
                        clm["AppOpens"].append(app)
                         #print("MAP user")
    Map_Users = pd.DataFrame(clm)
#print(Map_Users)
    return(Map_Users)
#TOP_TRANSACTION
def ex_top_transaction():

    path = "C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\top\\transaction\\country\\india\\state\\"

    clm = {
      'State': [], 'Year': [], 'Quarter': [],
       'District': [], 'Transaction_count': [], 'Transaction_amount': []
    
          }

    state_list = os.listdir(path)

    for state in state_list:
        p_state = path + state + "/"
        years = os.listdir(p_state)

        for year in years:
            p_year = p_state + year + "/"
            files = os.listdir(p_year)

            for file in files:
                with open(p_year + file, 'r') as f:
                    D = json.load(f)

            # ---- DISTRICTS ----
                    for item in D["data"]["districts"]:
                        district = item["entityName"]
                        count = item["metric"]["count"]
                        amount = item["metric"]["amount"]

                        clm["State"].append(state)
                        clm["Year"].append(year)
                        clm["Quarter"].append(int(file.strip(".json")))
                        clm["District"].append(district)
                        clm["Transaction_count"].append(count)
                        clm["Transaction_amount"].append(amount)
    Top_Trans = pd.DataFrame(clm)
                    
#print(Top_Trans)
    return(Top_Trans)




#TOP_INSURANCE
def ex_top_insurance():
    path = "C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\top\\insurance\\country\\india\\state\\"

    clm = {
      'State': [], 'Year': [], 'Quarter': [],
       'District': [], 'Insurance_count': [], 'Insurance_amount': []
         }

    state_list = os.listdir(path)

    for state in state_list:
        p_state = path + state + "/"
        years = os.listdir(p_state)
        for year in years:
            p_year = p_state + year + "/"
            files = os.listdir(p_year)

            for file in files:
                with open(p_year + file, 'r') as f:
                    D = json.load(f)

            # ---- DISTRICTS ----
                    for item in D["data"]["districts"]:
                        district = item["entityName"]
                        count = item["metric"]["count"]
                        amount = item["metric"]["amount"]

                        clm["State"].append(state)
                        clm["Year"].append(year)
                        clm["Quarter"].append(int(file.strip(".json")))
                        clm["District"].append(district)
                        clm["Insurance_count"].append(count)
                        clm["Insurance_amount"].append(amount)
    Top_Insur = pd.DataFrame(clm)
    return(Top_Insur)
#print(Top_Insur)
#TOP_USERS
              

   


def ex_top_user():
    path = "C:\\Users\\hp\\OneDrive\\Documents\\Project_Guvi\\data\\data\\top\\user\\country\\india\\state\\"
    clm = {
      'State': [], 'Year': [], 'Quarter': [],
       'District': [], 'RegisteredUsers': []   
          }

    state_list = os.listdir(path)

    for state in state_list:
        p_state = path + state + "/"
        years = os.listdir(p_state)

        for year in years:
            p_year = p_state + year + "/"
            files = os.listdir(p_year)

            for file in files:
                with open(p_year + file, 'r') as f:
                    D = json.load(f)

            # ---- DISTRICTS ----
                    for item in D["data"]["districts"]:
                        district = item["name"]
                        users = item["registeredUsers"]

                        clm["State"].append(state)
                        clm["Year"].append(year)
                        clm["Quarter"].append(int(file.strip(".json")))
                        clm["District"].append(district)
                        clm["RegisteredUsers"].append(users)
              

    Top_User = pd.DataFrame(clm)
    return(Top_User)
#print(Top_User)





