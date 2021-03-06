#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import webbrowser

def app():
    st.header('About Me')

    st.markdown(
        """
        I'm Nikki Satmaka, a Data Scientist, Financial Market Practitioner and Analyst,
        Quantitative Finance Enthusiast. I'm a Co-Author of "Simple Trading Simple Investing"
        together with Ryan Filbert's Team.

        I can help you provide insights from data especially regarding the financial markets.
        This app is a sample portfolio of mine to display data analysis and visualization
        from a supermarket sales data.
        """
    )

    github_url = '[GitHub](https://github.com/NikkiSatmaka)'
    linkedin_url = '[LinkedIn](https://www.linkedin.com/in/nikkisatmaka/)'

    st.markdown('--------------------')
    st.markdown('Connect with me on')

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(github_url, unsafe_allow_html=True)
        # if st.button('My Github'):
            # webbrowser.open_new_tab(github_url)

    with col2:
        st.markdown(linkedin_url, unsafe_allow_html=True)
        # if st.button('My LinkedIn'):
            # webbrowser.open_new_tab(linkedin_url)