#C:\Users\hp\OneDrive\Desktop\guvi\main.py#st.set_page_config(page_title="PhonePe Analysis", layout="wide")
import streamlit as st
from visuali import plot_statewise_choropleth

st.set_page_config(page_title="PhonePe Dashboard", layout="wide")

import pandas as pd
import matplotlib.pyplot as plt
from db_connection import get_connection


import sys

st.write("Python executable path:", sys.executable)
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
#State-wise Total Transaction Amount
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
#Quarter-wise Transaction Amount Trend
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
#Category-wise Transaction Amount
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
#TOP PAYMENT CATEGORIES BY TOTAL AMOUNT
        st.write("TOP PAYMENT CATEGORIES")
        query4="""SELECT Transaction_type AS Category, SUM(Transaction_amount) AS Total_Amount
        FROM aggregate_transaction
        GROUP BY Category
        ORDER BY Total_Amount DESC;"""
        df4= pd.read_sql(query4, engine)
        plt.figure(figsize=(10,6))
        plt.barh(df4['Category'], df4['Total_Amount'])
        plt.title("Category-wise Total Transaction Amount")
        plt.xlabel("Amount")
        st.pyplot(plt.gcf())
#_________________________________________________________________
#TOP 10 STATES BY AVERAGE TRANSACTION AMOUNT
        st.write("TOP 10 STATE WISE TRANSACTION AMOUNT")
        query1 = """
          SELECT State, AVG(Transaction_amount) AS Avg_Amount
          FROM aggregate_transaction
          GROUP BY State
          ORDER BY Avg_Amount DESC
          LIMIT 10; """
        df1 = pd.read_sql(query1, engine)
      
        plt.figure(figsize=(12,6))
        plt.bar(df1['State'], df1['Avg_Amount'])
        plt.xticks(rotation=90)
        plt.title("Top 10 States by Avg Transaction Amount")
        st.pyplot(plt.gcf())
    
#______________________
        
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
#2Year-wise Insurance Growth
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
#4Insurance Type Distribution (DONUT CHART)
#----------------------------------------------------
        st.write("INSURANCE TYPE DISTRIBUTION")

        query4 = """
        SELECT insurance_type,
        SUM(insurance_count) AS total_count
        FROM aggregate_insurance
        GROUP BY insurance_type;
        """

        df4 = pd.read_sql(query4, engine)

        plt.figure(figsize=(8,8))
        plt.pie(df4["total_count"],
        labels=df4["insurance_type"],
        autopct="%1.1f%%",
        wedgeprops={'width':0.4})

        plt.title("Insurance Type Distribution")
        st.pyplot(plt.gcf())


#----------------------------------------------------
#5Top 10 States by Insurance Count
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
    
    if s=="Device Dominance and User Engagement Analysis":

#----------------------------------------------------
#1 Device-wise Registered Users
#----------------------------------------------------
        st.write("DEVICE WISE REGISTERED USERS")

        df1 = pd.read_sql("""
        SELECT user_brand,
        SUM(user_count) AS total_users
        FROM aggregate_users
        GROUP BY user_brand
        ORDER BY total_users DESC;
        """, engine)

        plt.figure(figsize=(10,6))
        plt.bar(df1["user_brand"], df1["total_users"])
        plt.xticks(rotation=45)
        plt.title("Registered Users by Device Brand")
        st.pyplot(plt.gcf())




#----------------------------------------------------
#3 Year-wise User Growth
#----------------------------------------------------
        st.write("YEAR WISE USER GROWTH")

        df3 = pd.read_sql("""
        SELECT year,
        SUM(user_count) AS total_users
        FROM aggregate_users
        GROUP BY year
        ORDER BY year;
        """, engine)

        plt.figure(figsize=(10,5))
        df3.plot(kind="line", x="year", y="total_users", marker="o")
        plt.title("Year-wise User Growth")
        st.pyplot(plt.gcf())


    if s=="Transaction Analysis for Market Expansion":

#----------------------------------------------------
#1 State-wise Transaction Amount
#----------------------------------------------------
        st.write("STATE WISE TRANSACTION AMOUNT")

        df1 = pd.read_sql("""
        SELECT state,
        SUM(transaction_amount) AS total_amount
        FROM aggregate_transaction
        GROUP BY state
        ORDER BY total_amount DESC;
        """, engine)

        plt.figure(figsize=(12,6))
        df1.head(10).plot(kind='bar', x='state', y='total_amount')
        plt.title("Top States by Transaction Amount")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())


#----------------------------------------------------
#2 District-wise Transaction Amount
#----------------------------------------------------
        st.write("TOP DISTRICTS BY TRANSACTION AMOUNT")

        df2 = pd.read_sql("""
        SELECT district,
        SUM(transaction_amount) AS total_amount
        FROM map_transaction
        GROUP BY district
        ORDER BY total_amount DESC
        LIMIT 10;
        """, engine)

        plt.figure(figsize=(12,6))
        plt.bar(df2["district"], df2["total_amount"])
        plt.xticks(rotation=90)
        plt.title("Top 10 Districts by Transaction Amount")
        st.pyplot(plt.gcf())


#----------------------------------------------------
#3 Top states by Transaction Amount
#----------------------------------------------------
        st.write("TOP states BY TRANSACTION AMOUNT")

        df3 = pd.read_sql("""
        SELECT state,
        SUM(transaction_amount) AS total_amount
        FROM top_transaction
        GROUP BY state
        ORDER BY total_amount DESC
        LIMIT 10;
        """, engine)

        plt.figure(figsize=(10,5))
        plt.bar(df3["state"], df3["total_amount"])
        plt.title("Top state by Transaction Amount")
        st.pyplot(plt.gcf())    

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

        df2 = pd.read_sql("""
        SELECT district,
        SUM(registeredusers) AS total_users
        FROM map_users
        GROUP BY district
        ORDER BY total_users DESC
        LIMIT 10;
        """, engine)

        plt.figure(figsize=(12,6))
        plt.bar(df2["district"], df2["total_users"])
        plt.xticks(rotation=90)
        plt.title("Top Districts by Registered Users")
        st.pyplot(plt.gcf())


#----------------------------------------------------
#3 State-wise User Registrations
#----------------------------------------------------
        st.write("TOP States BY USER REGISTRATIONS")

        df3 = pd.read_sql("""
        SELECT state,
        SUM(registeredusers) AS total_users
        FROM top_user
        GROUP BY state
        ORDER BY total_users DESC
        LIMIT 10;
        """, engine)

        plt.figure(figsize=(10,5))
        plt.bar(df3["state"], df3["total_users"])
        plt.title("Top state by Registered Users")
        st.pyplot(plt.gcf())


