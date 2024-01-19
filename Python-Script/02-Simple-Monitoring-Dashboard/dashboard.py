#!/usr/bin/python3
#

try: 
    import streamlit as st
    import psutil as ps
    import db_conn as db

except ImportError as i_err:
    print(i_err)

def main():
    dbase = db.dbase()

    print("Connected")
main()