#!/usr/bin/python3
#

try: 
    import streamlit as st # pip3 install streamlit
    from st_circular_progress import CircularProgress # pip3 install st-circular-progress
    import psutil as ps # pip3 install psutil
    import db_conn as db
    import pandas as pd # pip3 install pandas

except ImportError as i_err:
    print(i_err)

d1 = [100, 50, 101]
d2 = [20, 35, 22]

def psql_db():
    dbase = db.dbase()

def main():
    '''Data visualization for server monitoring'''

    st.title("Simple Dashboard")

    # To css file.
    with open("assets/style.css") as styles:
        st.markdown(f'<style rel="stylesheet" href={styles}>', 
                    unsafe_allow_html=True)
    

    cpu = ps.cpu_percent()
    memory = ps.virtual_memory()
    print(cpu)

    # Show system resources

    dashboard = st.columns(5)
    server_progress = CircularProgress(
        label="Test",
        value=int(cpu),
        key="server_progress")
    
    server_progress.st_circular_progress()



if __name__ == "__main__":
    main()