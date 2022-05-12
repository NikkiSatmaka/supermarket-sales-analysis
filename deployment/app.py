#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image

from multipage import MultiPage
from pages import introduction, data_visualization, hypothesis_testing, about

app = MultiPage()

st.set_page_config(
    page_title='Supermarket Sales Analysis',
    page_icon='🛒',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/NikkiSatmaka',
        'Report a bug': 'https://github.com/NikkiSatmaka',
        'About': '# Supermarket Sales Anaylsis'
    }
)

# Title of the main page
logo = Image.open('assets/20063.jpg')
col1, col2 = st.columns(2)
col1.image(logo, width=200)
col2.title('Supermarket Sales Analysis')

# Add all of the applications
app.add_page('Introduction', introduction.app)
app.add_page('Data Visualization', data_visualization.app)
app.add_page('Hypothesis Testing', hypothesis_testing.app)
app.add_page('About', about.app)

app.run()