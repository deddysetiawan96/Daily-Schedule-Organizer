# Library1
import google.generativeai as palm
import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
import threading

# Set API
palm.configure(api_key='AIzaSyDbqR25goY3VyT9WULVoUv11nXmJwmxNVE')

# Set default parameters
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

# Fungsi Main
def main():
    st.title("Daily Schedule Organizer")
    st.subheader("Your Assistant")
    st.write("Developed by AWAN")

    # Menu
    main_menu = ["Saran tentang penjadwalan", "Pengingat jadwal", "Membuat Jadwal"]
    choice = st.sidebar.selectbox('Apa yang ingin kamu lakukan?', main_menu)

    if choice == 'Saran tentang penjadwalan':
        with st.chat_message("DS"):
            st.write("Hello 👋, Apa yang bisa kubantu")
        prompt = st.chat_input("Ketikkan sesuatu kawan...")

        formatted_prompt = f"Answer the {prompt} in schedule format"
        if prompt:
            response = palm.generate_text(**defaults, prompt=formatted_prompt)

            if response != None:
                with st.chat_message(name='Assistant', avatar="🤖"):
                    st.write('Ini adalah saran penjadwalan dari saya: ')
                    st.write(response.result)


    elif choice == 'Pengingat jadwal':
        with st.chat_message("DS"):
            st.write("Hello 👋, Mau diingatkan tentang apa dan jam berapa?")
        waktu_pengingat = st.chat_input("Masukkan waktu pengingat (hh:mm)")

        if waktu_pengingat:
            # Modifikasi prompt untuk pengingat jadwal
            prompt_pengingat = f"Ingatkan saya pada jam {waktu_pengingat}"

            if st.button("Buat Pengingat"):
                response_pengingat = palm.generate_text(**defaults, prompt=prompt_pengingat)
                if response_pengingat is not None:
                    with st.chat_message(name='Assistant', avatar="🤖"):
                        st.write(f'Oke, aku akan mengingatkanmu pada jam {waktu_pengingat}')
                        st.write(response_pengingat.result)
                    # Implementasi notifikasi atau pengingat sesuai dengan kebutuhan Anda.

    elif choice == 'Membuat Jadwal':
        with st.chat_message("DS"):
            st.write("Hello 👋, Jadwal seperti apa yang ingin kamu buat?")
        deskripsi_jadwal = st.chat_input("Deskripsikan jadwalmu")

        if deskripsi_jadwal:
            # Memodifikasi prompt untuk membuat jadwal dengan kegiatan
            prompt_membuat_jadwal = f"schedule {deskripsi_jadwal}"
            response_membuat_jadwal = palm.generate_text(**defaults, prompt=prompt_membuat_jadwal)

            if response_membuat_jadwal is not None:
                with st.chat_message(name='Assistant', avatar="🤖"):
                    st.write(f'Oke, jadwal telah dibuat untuk {deskripsi_jadwal}')
                    st.write(response_membuat_jadwal.result)

                    # Implementasi penyimpanan jadwal atau tindakan lain sesuai dengan kebutuhan Anda.


if __name__ == '__main__':
    main()
