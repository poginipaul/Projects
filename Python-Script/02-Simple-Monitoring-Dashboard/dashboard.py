#!/usr/bin/python3
#

try: 
    import streamlit as st # pip3 install streamlit
    from st_circular_progress import CircularProgress # pip3 install st-circular-progress
    import psutil as ps # pip3 install psutil
    import pandas as pd # pip3 install pandas
    import paramiko # pip3 instal paramiko
    import subprocess as sp
    import pandas as pd
    import psycopg2

except ImportError as i_err:
    print(i_err)

st.set_page_config(page_title="Simple Dashboard",
                   initial_sidebar_state="auto")

st.header("Simple Dashboard")

def get_conn():
    icmp_ip_addr = sp.Popen('ping, ')
    pass

@st.cache_resource
def st_psql_conn():
    return psycopg2.connect(**st.secrets["postgres"])

conn = st_psql_conn()

def run_query(query):
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

def main():
    '''Network Monitoring for on-prem servers.'''

    # To css file.
    with open("assets/style.css") as styles:
        st.markdown(f'<style rel="stylesheet" type="text/css" href={styles}>', 
                    unsafe_allow_html=True)

    # System Usage of Localhost.   
    # Setting variables where to fetch data.
    cpu = ps.cpu_percent()
    memory = ps.virtual_memory()
    disk = ps.disk_usage('/')

    # Connected remote servers.
    # Localhost column
    cpu_col, ram_col, disk_col = st.columns(3)

    # CPU usage by percentage.
    with cpu_col:
        cpu_progress = CircularProgress(
            label="CPU",
            value=int(cpu),
            key="cpu_progress",
            color="#355e3b",
            size="large"
            )
        
        cpu_progress.st_circular_progress()
    
    # Memory usage by percentage.
    with ram_col:
        ram_progress = CircularProgress(
            label="Memory",
            value=int(memory[2]),
            key="ram_progress",
            color="#355e3b",
            size="large"
            )
        
        ram_progress.st_circular_progress()
    
    # Disk usage by percentage.
    with disk_col:
        disk_progress = CircularProgress(
            label="Disk",
            value=int(disk[3]),
            key="disk_progress",
            color="#355e3b",
            size="large"
            )
        
        disk_progress.st_circular_progress()



    rows = run_query("SELECT * FROM ip_add_tb")
    data = pd.DataFrame(rows, columns=['ID', 'IP_Address'])
    st.table(data)





if __name__ == "__main__":
    main()
    