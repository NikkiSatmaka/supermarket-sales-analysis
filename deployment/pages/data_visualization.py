#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import col
import seaborn as sns
import plotly.express as px

import streamlit as st
from streamlit.elements import pyplot

from packages.columncat import categorize

sns.set_theme(style='darkgrid', palette='deep')

pd.set_option('display.precision', 2)


def app():
    st.header('Data Vizualisation')

    # Load csv data which has been processed
    df = pd.read_csv('data/supermarket_sales_processed.csv', parse_dates=['Date Time'])

    # Categorize features with object dtype
    df = categorize(df, 20, exclusion=['Day of Week'])
    day_cats = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    df['Day of Week'] = pd.Categorical(df['Day of Week'], categories=day_cats, ordered=True)

    # Graph One
    st.subheader('Branch Transactions')
    st.markdown('Shows the total number of transactions for each branch')
    # fig = plt.figure(figsize=(5, 5))
    fig = plt.figure()
    sns.countplot(x='Branch', data=df)
    st.pyplot(fig)
    st.markdown("""Branch A in Yangon have the most transactions, but the difference is marginal.
    All branches have about the same number of transactions""")

    # Graph Two
    st.subheader('Relation between Rating and Total Amount of Transaction')
    fig = px.scatter(df, x='Rating', y='Total', color='Branch')
    st.plotly_chart(fig)
    st.markdown('There is no correlation between rating and the amount of transaction')

    # Graph Three
    st.subheader('Sales for each Product Line categorized by Gender')
    fig = px.bar(df, x='Product Line', y='Total', color='Gender', barmode='group')
    st.plotly_chart(fig)
    st.markdown('Seems like there are quite a difference in Health and beauty, home and lifestyle, and food and beverages product lines')

    # Graph Four
    st.subheader('Distribution of Transaction Amount')
    fig = px.histogram(df, x='Total', nbins=50)
    st.plotly_chart(fig)
    st.markdown('People seem to spend around $100 per transaction')


    # Graph Five
    st.subheader('Make Your Own Graph')
    #### Selection
    graph_type = st.radio(
        'What kind of graph do you want to create?',
        ('bar', 'box', 'line', 'scatter')
    )
    st.write('You selected:', graph_type)

    cols = [
        'Branch',
        'City',
        'Customer Type',
        'Gender',
        'Product Line',
        'Unit Price',
        'Quantity',
        'Tax 5%',
        'Total',
        'Payment',
        'COGS',
        'Gross Margin Percentage',
        'Gross Income',
        'Rating',
        'Year',
        'Month',
        'Day',
        'Day of Week',
        'Hour',
        None
    ]

    x_axis = st.selectbox(
        'Select your x-axis:',
        cols
    )
    st.write('You selected:', x_axis)

    y_axis = st.selectbox(
        'Select your y-axis:',
        cols
    )
    st.write('You selected:', y_axis)

    cat = st.selectbox(
        'Select your category to group the data:',
        cols
    )
    st.write('You selected:', cat)

    #### Create graph
    if graph_type == 'bar':
        fig = px.bar(df, x=x_axis, y=y_axis, color=cat)

    if graph_type == 'box':
        fig = px.box(df, x=x_axis, y=y_axis, color=cat)

    if graph_type == 'line':
        fig = px.line(df, x=x_axis, y=y_axis, color=cat)

    if graph_type == 'scatter':
        fig = px.scatter(df, x=x_axis, y=y_axis, color=cat)

    st.plotly_chart(fig)

    st.markdown('Hope you had fun!')

