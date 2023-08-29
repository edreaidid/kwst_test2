import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

import hydralit_components as hc
from streamlit_extras.switch_page_button import switch_page

# define what option labels and icons to display
option_data = [         
   {'icon': "bi bi-hand-thumbs-up", 'label':"recognition"},
   {'icon':"fa fa-question-circle",'label':"firstaid"},
   {'icon': "far fa-chart-bar", 'label':"intervention"},
   {'icon': "fa fa-unlock-alt", 'label':"prevention"},
   {'icon':"fas fa-robot", 'label':"others"}
]

over_theme = {'txc_inactive': 'white','menu_background':'#0b6b66','txc_active':'black','option_active':'white'}
op = hc.nav_bar(
    menu_definition=option_data,
    override_theme=over_theme,
    home_name='Home',
    login_name='Screening',
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)

if op == "recognition": 
    switch_page("recognition")
if op == "firstaid":
    switch_page("firstaid")
if op == "intervention":
    switch_page("intervention")
if op == 'prevention':
    switch_page("prevention")
if op == 'others':
    switch_page("others")
if op == 'Screening':
    switch_page("untitled0")

st.video("https://www.youtube.com/watch?v=xJfm1Ht9fgI")
