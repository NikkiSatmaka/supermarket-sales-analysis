#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy import stats

import streamlit as st

from packages.columncat import categorize


def app():
    st.header('Hypothesis Testing')

    # Load csv data which has been processed
    df = pd.read_csv('data/supermarket_sales_processed.csv', parse_dates=['Date Time'])

    # Categorize features with object dtype
    df = categorize(df, 20, exclusion=['Day of Week'])
    day_cats = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    df['Day of Week'] = pd.Categorical(df['Day of Week'], categories=day_cats, ordered=True)

    st.subheader('Premise')

    # Graph average sales by branch and gender
    fig = px.box(
        df[df['Product Line'] == 'Health and beauty'],
        x='Branch',
        y='Total',
        color='Gender',
        title='Health and beauty product Average Sales'
    )

    expander = st.expander('Show graph')
    expander.write("This is the sales for health and beauty product for each branch, separated by gender.")
    expander.plotly_chart(fig)

    st.markdown(
        """
        There's a slight difference in the average sales for healt and beauty products between
        female and male. We want to check, whether this difference is significant.
        """
    )

    st.markdown('----------')
    st.subheader('Hypothesis:')
    st.markdown('$H_{0}: \mu_{health\ female} = \mu_{health\ male}$')
    st.markdown('$H_{1}: \mu_{health\ female} \\neq \mu_{health\ male}$')
    st.markdown('----------')


    health_female = df[(df['Product Line'] == 'Health and beauty') & (df['Gender'] == 'Female')]['Total']
    health_male = df[(df['Product Line'] == 'Health and beauty') & (df['Gender'] == 'Male')]['Total']

    st.subheader('Process:')
    st.write(f'- Average Sales of Health and beauty product for female: ${health_female.mean():.2f}')
    st.write(f'- Average Sales of Health and beauty product for male: ${health_male.mean():.2f}')
    st.markdown('- We want to see whether the difference is significant or not')

    st.markdown('- We are gonna test it out using two sample independent two tailed t-test')

    col1, col2, = st.columns(2)
    with col1:
        expander = st.expander('Show sales data for female')
        fig = plt.figure()
        sns.histplot(health_female).set_title('Distribution of Health and beauty product sales for female')
        expander.pyplot(fig)
    with col2:
        expander = st.expander('Show sales data for male')
        fig = plt.figure()
        sns.histplot(health_male).set_title('Distribution of Health and beauty product sales for male')
        expander.pyplot(fig)

    #################### t-test  ####################
    ci_health_female = stats.norm.interval(0.95, health_female.mean(), health_female.std())
    ci_health_male = stats.norm.interval(0.95, health_male.mean(), health_male.std())

    print(f'The confidence intervals from Health and beauty product sales for female is between {ci_health_female[0]:.2f} and {ci_health_female[1]:.2f}')
    print(f'The confidence intervals from Health and beauty product sales for male is between {ci_health_male[0]:.2f} and {ci_health_male[1]:.2f}')

    t_stat, p_val = stats.ttest_ind(health_female, health_male)


    health_female_pop = np.random.normal(health_female.mean(), health_female.std(), 10000)
    health_male_pop = np.random.normal(health_male.mean(), health_male.std(), 10000)

    fig = plt.figure(figsize=(16, 5))
    sns.kdeplot(health_female_pop, label='Health and beauty Product Sales for Female *Pop', color='red', shade=True)
    sns.kdeplot(health_male_pop, label='Health and beauty Product Sales for Male *Pop', color='blue', shade=True)

    plt.axvline(health_female.mean(), color='red', linewidth=2, label='Health and beauty Product Sales for Female Mean')
    plt.axvline(health_male.mean(), color='blue', linewidth=2, label='Health and beauty Product Sales for Male Mean')

    plt.axvline(ci_health_female[1], color='green', linestyle='dashed', linewidth=2, label='Confidence threshold of 95%')
    plt.axvline(ci_health_female[0], color='green', linestyle='dashed', linewidth=2)

    plt.axvline(health_female_pop.mean() + t_stat*health_female_pop.std(), color='black', linestyle='dashed', linewidth=2, label='Alternative Hypothesis')
    plt.axvline(health_female_pop.mean() - t_stat*health_female_pop.std(), color='black', linestyle='dashed', linewidth=2)

    plt.legend()


    st.subheader('Result:')
    st.write(f'- p-value: {p_val:.2f}')
    st.write(f'- t-statistics: {t_stat:.2f}')

    st.pyplot(fig)

    st.subheader('Conclusion:')
    st.markdown(
        """
        **Based on the result above, having a p value of more than `0.05`, we can conclude that we fail to reject the null hypothesis**,
        which means there are no significant difference in Health and beauty product sales between Female and Male gender
        """
    )