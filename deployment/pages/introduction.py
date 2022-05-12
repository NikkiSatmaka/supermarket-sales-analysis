#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st

pd.set_option('display.precision', 2)

from packages.columncat import unique_count, categorize

def app():
    st.header('Introduction')

    df = pd.read_csv('data/supermarket_sales_raw.csv', parse_dates=[['Date', 'Time']])

    # Tidy up column names to make it look pretty
    df.columns = df.columns.str.replace('_', ' ').str.title()
    df = df.rename(columns={'Invoice Id': 'Invoice ID', 'Cogs':'COGS'})
    df = categorize(df, 20)

    # st.markdown('### This is our Supermarket Sales data')

    st.markdown(
        """
        The growth of supermarkets in most populated cities are increasing
        and market competitions are also high.
        
        The dataset is one of the historical sales of supermarket company
        which has recorded in 3 different branches for 3 months data.

        Our role as a market research company is to find insights from this data.
        """
    )

    st.markdown('--------------------')
    st.markdown("Please navigate using the 'App Navigation' menu on the left sidebar")
    st.markdown('--------------------')


    if st.checkbox('Show the full Supermarket Sales data'):
        st.write(df)

    expander = st.expander('Attribute Information')
    expander.markdown(
        """
        - Date Time: Date and time of purchase (Record available from January 2019 to March 2019, 10am to 9pm)
        - Invoice ID: Computer generated sales slip invoice identification number
        - Branch: Branch of supercenter (3 branches are available identified by A, B and C).
        - City: Location of supercenters
        - Customer Type: Type of customers, recorded by Members for customers using member card and Normal for without member card.
        - Gender: Gender type of customer
        - Product Line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
        - Unit Price: Price of each product in $
        - Quantity: Number of products purchased by customer
        - Tax: 5% tax fee for customer buying
        - Total: Total price including tax
        - Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)
        - COGS: Cost of goods sold
        - Gross Margin Percentage: Gross margin percentage
        - Gross Income: Gross income
        - Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)
    """
    )

