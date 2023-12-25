import streamlit as st
import pandas as pd
import mysql.connector


cursor = None  #prevent cursor not defined error
global conn
# Establish a connection to database
try:
    
    conn = mysql.connector.connect(
    host=st.secrets["host"],
    user=st.secrets["user"],
    password=st.secrets["password"],
    database=st.secrets["database"])
    cursor = conn.cursor() # Create a cursor that interacts with db

except Exception as e:
    st.error(f"Sorry ," + e.__class__.__name__ + " has occurred" )
    #if conn  and conn.is_connected():
     #   conn.close()
    #if cursor  and cursor is not None:
     #   cursor.close()    

#global variable declaration
global df_HR
df_HR=pd.DataFrame()
global df_USER
df_USER=pd.DataFrame()

def match(ID):
    try:
        global df_HR , df_USER
        # Execute  query with  placeholder for  ID
        cursor.execute("SELECT * FROM HR_REQUIREMENTS WHERE ADMIN_ID=%s", (ID,)) #(ID,) creates one element tuple
        # Convert the result to a DataFrame 
        df_HR = create_df()

        st.title('HR REQ')

        # Display data 
        st.write(df_HR)

    except Exception as e:
        
        st.error(f"Error occurred: {e}")
        
    finally:
        #close the connection
        if conn:
         conn.close()
         st.success("DB connection closed") 

#function for creating dataframes
def create_df():
  #Fetch data
  result = cursor.fetchall()
  #Convert the result to a DataFrame 
  df= pd.DataFrame(result, columns=[col[0] for col in cursor.description])
  return df

match('101')         
