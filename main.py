#C:\Users\hp\OneDrive\Desktop\guvi\main.py#st.set_page_config(page_title="PhonePe Analysis", layout="wide")
import streamlit as st
from visuali import plot_statewise_choropleth

st.set_page_config(page_title="PhonePe Dashboard", layout="wide")

import pandas as pd
import matplotlib.pyplot as plt
from db_connection import get_connection


import sys

#st.write("Python executable path:", sys.executable)
engine = get_connection()


st.title("PhonePe Analysis")
# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.title("Navigation")
    page = st.selectbox("Select a page:",["Home","Analysis"])
if page == "Home":
    st.title("Welcome to PhonePe Dashboard")
    st.write("This is the homepage.")
    st.write("STATE WISE TRANSACTION MAP")
    query = """
        SELECT state,
        SUM(transaction_amount) AS total_amount
        FROM aggregate_transaction
        GROUP BY state; 
        """
    df_map = pd.read_sql(query, engine)
    df_map["state"] = df_map["state"].str.replace("-", " ").str.title()
    st.dataframe(df_map)
    plot_statewise_choropleth(df_map, metric_col="total_amount", title="State-wise Transaction Amount")
#_______________________________________________________

elif page == "Analysis":
    
    st.title("Analysis Page")
    st.write("This is where your analysis charts will appear.")

# ==========================================
# MAIN TITLE
# ==========================================
    #st.markdown("<h1>Business Case Study</h1>", unsafe_allow_html=True)

    st.write("### Choose a Business Case Study")
    s = st.selectbox("choose", ["Insurance Penetration and Growth Potential Analysis",
                                "Device Dominance and User Engagement Analysis",
                                "Transaction Analysis for Market Expansion"
                                ,"User Engagement and Growth Strategy"
                                ,"Decoding Transaction Dynamics on PhonePe"])
    if s=="Decoding Transaction Dynamics on PhonePe":
        
# -----------------------------------
# 1.1. Run SQL Query and Load Into DataFrame
# -----------------------------------
#1.State-wise Total Transaction Amount
        st.write("STATE WISE TRANSACTION AMOUNT")
        df1 = pd.read_sql("""
                          SELECT state, 
                          SUM(transaction_amount) AS total_amount
                          FROM aggregate_transaction
                          GROUP BY state
                          ORDER BY SUM(transaction_amount) DESC;
                          """, engine)
        plt.figure(figsize=(12,6))
        df1.plot(kind='bar', x='state', y='total_amount')
        plt.title("Total Transaction Amount by State")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())
#____________________________________________________
#2.Quarter-wise Transaction Amount Trend
        st.write("QUARTER WISE TRANSACTION AMOUNT TREND")
        query2 = """SELECT 
        year AS Year,
        quarter AS Quarter,
        SUM(transaction_amount) AS Total_Amount
        FROM aggregate_transaction
        GROUP BY year, quarter
        ORDER BY year, quarter;"""
        df2 = pd.read_sql(query2, engine)
        df2['Period'] = df2['Year'].astype(str) + "-Q" + df2['Quarter'].astype(str)
        plt.figure(figsize=(12,5))
        df2.plot(kind='line', x='Period', y='Total_Amount', marker='o')
        plt.title("Quarter-wise Transaction Amount Trend")
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())
#_____________________________________________________________
#3.Category-wise Transaction Amount
        st.write("CATEGORY WISE TRANSACTION AMOUNT")
        query3 = """SELECT
        transaction_type AS Category,
        SUM(transaction_amount) AS Total_Amount
        FROM aggregate_transaction
        GROUP BY transaction_type
        ORDER BY Total_Amount DESC;"""
        df3 = pd.read_sql(query3, engine)
        plt.figure(figsize=(8,8))
        df3 = df3.set_index("Category")      
        df3.plot(kind='pie', y='Total_Amount', autopct='%1.1f%%')   
        plt.title("Category-wise Transaction Amount Distribution")
        st.pyplot(plt.gcf())

#___________________________________________________________
#4.Year-wise Transaction Growth
        st.write("Year-wise Transaction Growth")
        query4="""SELECT year,
        SUM(transaction_amount) AS total_amount
        FROM aggregate_transaction
        GROUP BY year
        ORDER BY year;"""
        df4= pd.read_sql(query4, engine)
        plt.figure(figsize=(10,6))
        plt.barh(df4['year'], df4['total_amount'])
        plt.title("Year-wise Transaction Growth")
        plt.xlabel("Amount")
        st.pyplot(plt.gcf())
#_________________________________________________________________
#5.Average Transaction Amount by State
        st.write("Average Transaction Amount by State")
        query1 = """
          SELECT state,
          AVG(transaction_amount) AS avg_amount
          FROM aggregate_transaction
          GROUP BY state
          ORDER BY avg_amount DESC
          LIMIT 10; """
        df1 = pd.read_sql(query1, engine)
      
        plt.figure(figsize=(12,6))
        plt.bar(df1['state'], df1['avg_amount'])
        plt.xticks(rotation=90)
        plt.title("Top 10 States by Avg Transaction Amount")
        st.pyplot(plt.gcf())
    
#______________________
        
       
    if s=="Insurance Penetration and Growth Potential Analysis":

#----------------------------------------------------
#1 State-wise Insurance Amount
#----------------------------------------------------
        st.write("STATE WISE INSURANCE AMOUNT")

        df1 = pd.read_sql("""
        SELECT state,
        SUM(insurance_amount) AS total_amount
        FROM aggregate_insurance
        GROUP BY state
        ORDER BY total_amount DESC;
        """, engine)

        plt.figure(figsize=(12,6))
        df1.plot(kind='bar', x='state', y='total_amount')
        plt.title("State-wise Total Insurance Amount")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())


#----------------------------------------------------
#2.Year-wise Insurance Growth
#----------------------------------------------------
        st.write("YEAR WISE INSURANCE GROWTH")

        query2 = """
        SELECT year,
        SUM(insurance_amount) AS total_amount
        FROM aggregate_insurance
        GROUP BY year
        ORDER BY year;
        """

        df2 = pd.read_sql(query2, engine)

        plt.figure(figsize=(10,5))
        df2.plot(kind='line', x='year', y='total_amount', marker='o')
        plt.title("Year-wise Insurance Growth")
        st.pyplot(plt.gcf())


#----------------------------------------------------
#3 Quarter-wise Insurance Trend
#----------------------------------------------------
        st.write("QUARTER WISE INSURANCE TREND")

        query3 = """
        SELECT year, quarter,
        SUM(insurance_amount) AS total_amount
        FROM aggregate_insurance
        GROUP BY year, quarter
        ORDER BY year, quarter;
        """

        df3 = pd.read_sql(query3, engine)

        df3["Period"] = df3["year"].astype(str) + "-Q" + df3["quarter"].astype(str)

        plt.figure(figsize=(12,5))
        df3.plot(kind='line', x='Period', y='total_amount', marker='o')
        plt.title("Quarter-wise Insurance Amount Trend")
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())




#----------------------------------------------------
# Insurance Type Distribution (BAR CHART)
#---------------------------------------------
        st.write("INSURANCE TYPE DISTRIBUTION")
        query4 = """
        SELECT insurance_type,
        SUM(insurance_count) AS total_count
        FROM aggregate_insurance
        GROUP BY insurance_type;
        """
        df4 = pd.read_sql(query4, engine)
        plt.figure(figsize=(8,5))
        plt.bar(df4["insurance_type"], df4["total_count"])
        plt.xlabel("Insurance Type")
        plt.ylabel("Total Count")
        plt.title("Insurance Type Distribution")
        plt.xticks(rotation=45)
        st.pyplot(plt)

#----------------------------------------------------
#5.Top 10 States by Insurance Count
#----------------------------------------------------
        st.write("TOP 10 STATES BY INSURANCE COUNT")

        query5 = """
        SELECT state,
        SUM(insurance_count) AS total_count
        FROM aggregate_insurance
        GROUP BY state
        ORDER BY total_count DESC
        LIMIT 10;
        """

        df5 = pd.read_sql(query5, engine)

        plt.figure(figsize=(12,6))
        plt.bar(df5["state"], df5["total_count"])
        plt.xticks(rotation=90)
        plt.title("Top 10 States by Insurance Usage")
        st.pyplot(plt.gcf())
#---------------------------------------------------------------
    
    if s=="Device Dominance and User Engagement Analysis":

#----------------------------------------------------
#1.Device Brand-wise Total Users
#----------------------------------------------------
        st.write("Device Brand-wise Total Users")
        query1 = """
        SELECT user_brand, SUM(user_count) AS total_users
        FROM aggregate_users
        GROUP BY user_brand
        ORDER BY total_users DESC;"""
        df1 = pd.read_sql(query1, engine)
        plt.figure(figsize=(12,6))
        df1.plot(kind='bar', x='user_brand', y='total_users')
        plt.title("Device Brand-wise Total Users")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())




#----------------------------------------------------
#2. State-wise Total Users
#----------------------------------------------------
        st.write("State-wise Total Users")

        query2 = """SELECT State, SUM(user_count) AS total_users
        FROM aggregate_users
        GROUP BY State
        ORDER BY total_users DESC; """
        df2 = pd.read_sql(query2, engine)
        plt.figure(figsize=(12,6))
        df2.plot(kind='bar', x='State', y='total_users')
        plt.title("State-wise Total Users")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())

#----------------------------------------------------
#3.Year-wise User Growth
#----------------------------------------------------
        st.write("Year-wise User Growth")
        query3 = """SELECT Year, SUM(user_count) AS total_users
        FROM aggregate_users
        GROUP BY Year
        ORDER BY Year;"""
        df3 = pd.read_sql(query3, engine)
        plt.figure(figsize=(10,5))
        df3.plot(kind='line', x='Year', y='total_users', marker='o')
        plt.title("Year-wise User Growth")
        plt.ylabel("Total Users")
        st.pyplot(plt.gcf())

#----------------------------------------------------
#4.Quarter-wise User Trend
#----------------------------------------------------
        query4 = """SELECT Year, Quarter, SUM(user_count) AS total_users
        FROM aggregate_users
        GROUP BY Year, Quarter
        ORDER BY Year, Quarter;
        """
        df4 = pd.read_sql(query4, engine)
        df4['Period'] = df4['Year'].astype(str) + "-Q" + df4['Quarter'].astype(str)
        plt.figure(figsize=(12,5))
        df4.plot(kind='line', x='Period', y='total_users', marker='o')
        plt.title("Quarter-wise User Trend")
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())

#----------------------------------------------------
#5.Average Users for user brand
#----------------------------------------------------
        query5 = """SELECT user_brand, AVG(user_count) AS avg_users
        FROM aggregate_users
        GROUP BY user_brand
        ORDER BY avg_users DESC
        LIMIT 10;"""
        df5 = pd.read_sql(query5, engine)
        plt.figure(figsize=(10,6))
        df5.plot(kind='barh', x='user_brand', y='avg_users')
        plt.title("Top Device Brands by Average Users")
        st.pyplot(plt.gcf())





    if s=="Transaction Analysis for Market Expansion":

#----------------------------------------------------
#1.State-wise Total Transaction Amount
#----------------------------------------------------
        query1 = """
        SELECT State, SUM(Transaction_amount) AS total_amount
        FROM map_transaction
        GROUP BY State
        ORDER BY total_amount DESC;"""
        df1 = pd.read_sql(query1, engine)
        plt.figure(figsize=(12,6))
        df1.plot(kind='bar', x='State', y='total_amount')
        plt.title("State-wise Transaction Amount")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())


#----------------------------------------------------
#2 District-wise Transaction Amount
#----------------------------------------------------
        st.write("TOP DISTRICTS BY TRANSACTION AMOUNT")

        query2 = """SELECT District, SUM(Transaction_amount) AS total_amount
        FROM map_transaction
        GROUP BY District
        ORDER BY total_amount DESC
        LIMIT 10;
        """
        df2 = pd.read_sql(query2, engine)
        plt.figure(figsize=(12,6))
        df2.plot(kind='bar', x='District', y='total_amount')
        plt.title("Top Districts by Transaction Amount")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())


#----------------------------------------------------
#3 Top Districts by Transaction Count
#----------------------------------------------------
        st.write("Top Districts by Transaction Count")

        query3 = """
        SELECT District, SUM(Transaction_count) AS total_transactions
        FROM map_transaction
        GROUP BY District
        ORDER BY total_transactions DESC
        LIMIT 10;"""
        df3 = pd.read_sql(query3, engine)
        plt.figure(figsize=(12,6))
        df3.plot(kind='barh', x='District', y='total_transactions')
        plt.title("Top Districts by Transaction Count")
        st.pyplot(plt.gcf())

#----------------------------------------------------
#4 -Year wise Transaction Growth
#----------------------------------------------------
        query4 = """
        SELECT Year, SUM(Transaction_amount) AS total_amount
        FROM map_transaction
        GROUP BY Year
        ORDER BY Year;
        """
        df4 = pd.read_sql(query4, engine)
        plt.figure(figsize=(10,5))
        df4.plot(kind='line', x='Year', y='total_amount', marker='o')
        plt.title("Year-wise Transaction Growth")
        st.pyplot(plt.gcf())

#----------------------------------------------------
#5 -Top District Transactions
#----------------------------------------------------
        query5 = """
         SELECT District, SUM(Transaction_amount) AS total_amount
         FROM top_transaction
         GROUP BY District
         ORDER BY total_amount DESC
         LIMIT 10;"""
        df5 = pd.read_sql(query5, engine)
        plt.figure(figsize=(12,6))
        df5.plot(kind='bar', x='District', y='total_amount')
        plt.title("Top District Transactions")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())

#----------------------------------------------------
#
#----------------------------------------------------

    if s=="User Engagement and Growth Strategy":

#----------------------------------------------------
#1 State-wise Registered Users
#----------------------------------------------------
        st.write("STATE WISE REGISTERED USERS")

        df1 = pd.read_sql("""
        SELECT state,
        SUM(registeredusers) AS total_users
        FROM map_users
        GROUP BY state
        ORDER BY total_users DESC;
        """, engine)

        plt.figure(figsize=(12,6))
        df1.head(10).plot(kind='bar', x='state', y='total_users')
        plt.title("Top States by Registered Users")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())


#----------------------------------------------------
#2 District-wise User Engagement
#----------------------------------------------------
        st.write("TOP DISTRICTS BY REGISTERED USERS")

        query2 = """
       SELECT District, SUM(RegisteredUsers) AS total_users
       FROM map_users
       GROUP BY District
       ORDER BY total_users DESC
       LIMIT 10;
       """
        df2 = pd.read_sql(query2, engine)
        plt.figure(figsize=(12,6))
        df2.plot(kind='bar', x='District', y='total_users')
        plt.title("Top Districts by Registered Users")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())

        


#----------------------------------------------------
#3 Year-wise User Growth
#----------------------------------------------------
        st.write("Year-wise User Growth")

        query3 = """
        SELECT Year, SUM(RegisteredUsers) AS total_users
        FROM map_users
        GROUP BY Year
        ORDER BY Year;
        """
        df3 = pd.read_sql(query3, engine)
        plt.figure(figsize=(10,5))
        df3.plot(kind='line', x='Year', y='total_users', marker='o')
        plt.title("Year-wise User Growth")
        st.pyplot(plt.gcf())

#----------------------------------------------------
#4 App Opens by State (User Engagement)
#----------------------------------------------------
        query4 = """
        SELECT State, SUM(AppOpens) AS total_opens
        FROM map_users
        GROUP BY State
        ORDER BY total_opens DESC;"""
        df4 = pd.read_sql(query4, engine)
        plt.figure(figsize=(12,6))
        df4.plot(kind='bar', x='State', y='total_opens')
        plt.title("State-wise App Opens")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())


#----------------------------------------------------
#5 Top Districts by Registered Users 
#----------------------------------------------------
        query5 = """
        SELECT District, SUM(RegisteredUsers) AS total_users
        FROM top_user
        GROUP BY District
        ORDER BY total_users DESC
        LIMIT 10;
        """
        df5 = pd.read_sql(query5, engine)
        plt.figure(figsize=(12,6))
        df5.plot(kind='barh', x='District', y='total_users')
        plt.title("Top Districts by Registered Users")
        st.pyplot(plt.gcf())




























