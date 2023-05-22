# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:54:01 2023

@author: Edre MA
"""

import streamlit as st
import pandas as pd
import datetime as dt
import pytz

# Layout for the form 
with st.form("myform",clear_on_submit=True):

    "### KWS Triager"
    
    kuala_lumpur=pytz.timezone('Asia/Kuala_Lumpur')
    now=dt.datetime.now()
    live_datetime=now.astimezone(kuala_lumpur)
    live_datetime
    
    # These exist within the form but won't wait for the submit button
    kategori_pesakit = st.empty()
    placeholder_for_optional_text = st.empty()
    kategori_dependent = st.empty()
    bukan_dependent_sesuai = st.empty()
    kategori_sesuai = st.empty()
    kategori_sesuai2 = st.empty()
    gejala_tidak_sesuai = st.empty()
    gejala_tidak_sesuai2 = st.empty()
    senarai_gejala = st.empty()
    senarai_gejala2 = st.empty()
    
    x =st.form_submit_button("hantar maklumat ke KWS")
    st.write(x)
 
# Screening for right category
with kategori_pesakit:
    options = ["ya","bukan","ahli keluarga staf"] + ["tidak berkaitan"]
    selection = st.selectbox("Adakah anda staf SASMEC?", options=options, index=3)

# Create text input for user entry
with placeholder_for_optional_text:
    if selection == "tidak berkaitan":
        selection3=False
        selection2=False
        selection4=False
        st.write("Terima kasih kerana menggunaan aplikasi ini")
    if selection == "bukan":
        selection3=False
        selection2=False
        selection4=False
        st.write("sila pergi ke ETD SASMEC atau fasiliti kesihatan yang lain")    

# dependent screening
with kategori_dependent:
    if selection == "ahli keluarga staf":
        options2 = ["ayah/emak/suami/isteri","anak kurang 18 tahun","pelajar kurang 21 tahun", "tiada dalam senarai"] 
        selection2 = st.selectbox("Apa hubungan anda dengan staf?", options=options2, index=3) 
        with kategori_sesuai2:
            if selection2 == "ayah/emak/suami/isteri" or selection2 == "anak kurang 18 tahun" or selection2 =="pelajar kurang 21 tahun":
                options4 = ["ya","tidak"] 
                selection4 = st.selectbox("Adakah anda ada gejala seperti dibawah?", options=options4, index=1) 
                with senarai_gejala:
                    if selection2 == "ayah/emak/suami/isteri" or selection2 == "anak kurang 18 tahun" or selection2 =="pelajar kurang 21 tahun":
                        selection3=False
                        st.write (["kesukaran bernafas", "sakit dada","pitam", "kesakitan melampau"])
                with gejala_tidak_sesuai:
                    if selection4 == "ya":
                        st.write("sila pergi ke ETD SASMEC atau fasili kesihatan berdekatan")
                
        with bukan_dependent_sesuai:
            if selection2 == "tiada dalam senarai":
                selection3=False
                selection4=False
                st.write("sila pergi ke ETD SASMEC atau fasili kesihatan berdekatan")

# staff screening

with senarai_gejala2:
    if selection == "ya": 
        st.write (["kesukaran bernafas", "sakit dada","pitam", "kesakitan melampau"])
        with kategori_sesuai:
            if selection == "ya":
                options3 = ["ya","tidak"] 
                selection3 = st.selectbox("Adakah anda ada gejala seperti dibawah?", options=options3, index=1) 
                selection2=False
                selection4=False
                with gejala_tidak_sesuai2:
                    if selection3 == "ya":
                        st.write("sila pergi ke ETD SASMEC atau fasili kesihatan berdekatan")
           
def form_callback(data1, data2, data3, data4, data5):    
    with open('kwst.csv', 'a+') as f:    #Append & read mode
        f.write(f"{data1},{data2},{data3},{data4},{data5}\n")    
    
if x:
    form_callback(selection,selection3,selection2,selection4,live_datetime)

with st.sidebar:
    st.info(" #### Admin monitoring :point_down:")
    password = st.text_input("Enter a password", value="", type="password")
    if password=="abcd":
        st.dataframe(pd.read_csv("kwst.csv",names=["staf sasmec","bergejala", "ahli staf", "ahli bergejala", "masa"]),height=300)
      





