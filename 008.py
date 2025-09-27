import streamlit as st
st.set_page_config(page_title='Trắc nghiệm tính cách', page_icon=':question', layout='wide')
st.title('Hãy chọn một con vật mà bạn thích nhất')
col1,col2,col3,col4,col5 = st.columns(5)
col6, col7 = st.columns([2,1])
personality = {'Cat':'Lazy but smart',
               'Dog':'A diciplined and hardworking person but usually is not creative as a person',
               'Lion':'''If your favorite animal is the lion,
               it often reflects a personality that’s bold, commanding, and deeply rooted in strength. Lions are symbols of courage, dominance, and pride, and people who gravitate toward them tend to embody those traits in subtle or overt ways. You might be someone who naturally takes the lead in group settings, not necessarily because you seek control, but because others trust your instincts and presence. There’s a quiet confidence in lion lovers—an ability to stay composed under pressure and to face challenges with a regal kind of resilience. You may value loyalty above all, protecting those close to you with fierce devotion, and you likely have a strong sense of identity that doesn’t waver easily. Much like the lion surveying its territory, you’re observant, strategic, and not easily rattled by chaos.'''
               ' At the same time, favoring the lion can hint at a deeper emotional complexity. Lions are not just powerful—they’re also deeply social creatures, living in tight-knit prides that rely on cooperation and connection. This suggests that you might crave meaningful relationships and thrive when surrounded by people who understand and respect you. You may have a strong moral compass, guided by a sense of justice and fairness, and you’re probably not one to back down when something feels wrong. Beneath your strength, there’s likely a layer of vulnerability that you guard carefully, revealing it only to those who’ve earned your trust. In essence, loving lions isn’t just about admiring their power—it’s about resonating with their balance of ferocity and tenderness, independence and community, dominance and dignity.',
               'Horse':'You always strive for freedom',
               'Swan':'You are beautiful as a person and seek inner peace'}
with col1:
    b1= st.button('Lion')
with col2:
    b2= st.button('Dog')
with col3:
    b3= st.button('Swan')
with col4:
    b4= st.button('Cat')
with col5:
    b5=st.button('Horse')

# st.success(personality['Lion']) st.success(personality['Dog'])st.success(personality['Dog'])st.success(personality['Cat'])st.success(personality['Horse'])

if b1:
    with st.expander('Lion'):
        st.write(personality['Lion'])
    with col6: 
        audio = open('Who can roar the loudest #lion #roar #loud - isaiah malonson.mp3','rb')
        st.audio(audio, format='audio/wav')
        st.write('Video')
        video1= 'https://www.youtube.com/watch?v=OMkEVX23BdM'
        st.video(video1, format='video/mp4')
    with col7:
        st.image('https://files.worldwildlife.org/wwfcmsprod/images/pc_honorable_mention_lion_nat_hab_photo_contest_2017/magazine_small/8kd8qhz2do_Lion_King.jpg',caption='Con sư tử')
if b2:  
    with st.expander('Dog'):
        st.write(personality['Dog'])
    with col6:
        audio = open('Ollie Pop the Siberian Husky howling - RockyMTN steeze.mp3','rb')
        st.audio(audio, format='audio/wav')
        st.write('Video')
        video1= 'https://www.youtube.com/watch?v=VDqxSg98CjM'
        st.video(video1, format='video/mp4')
    with col7:
        st.image('https://bowwowinsurance.com.au/wp-content/uploads/2024/10/shutterstock_135246929_ed-brown-siberian-husky-dog-portrait.jpg',caption='Siberian Husky')
if b3:
    with st.expander('Swan'):
        st.write(personality['Swan'])
    with col6:
        audio = open('swan.mp3','rb')
        st.audio(audio, format='audio/wav')
        st.write('Video')
        video1= 'https://www.youtube.com/watch?v=QZcJ1PdHttA'
        st.video(video1, format='video/mp4')
    with col7:
        st.image('https://www.kentwildlifetrust.org.uk/sites/default/files/styles/og_image/public/2018-01/Bird%20-%20Swan%20Mute%20Gillian%20Day%20Slimbridge%20Oct%202010.jpg?h=759fe590&itok=E-dfHZDe',caption='Swan')
if b4:
    with st.expander('Cat'):
        st.write(personality['Cat'])
    with col6: 
        audio = open('Mèo kêu meo meo - COUNTRYSIDE TV.mp3','rb')
        st.audio(audio, format='audio/wav')
        st.write('Video')
        video1= 'https://www.youtube.com/watch?v=5ZvUTDPU3Ak'
        st.video(video1, format='video/mp4')
    with col7:
        st.image('https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg',caption='Con mèo')
if b5:
    with st.expander('Horse'):
        st.write(personality['Horse'])
    with col6: 
        audio = open('Horse sounds.mp3','rb')
        st.audio(audio, format='audio/wav')
        st.write('Video')
        video1= 'https://www.youtube.com/watch?v=H9aC5AGY9YU'
        st.video(video1, format='video/mp4')
    with col7:
        st.image('https://yumove.co.uk/cdn/shop/articles/custom_resized_f30ef82c-c32b-4b5f-aab2-7ae103e9c7cf.jpg?v=1742568467',caption='Horse')

st.sidebar.image('https://i.pinimg.com/564x/f9/13/46/f9134655b53cbeaeb00664b04371b9b0.jpg',caption='Hello!')
with st.sidebar:
    st.header('Ever wondered what your favorite animal says about you? ')
    st.write('This page is all about exploring personality through the wild lens of the animal kingdom. Whether youre a bold lion, a wise owl, or a mysterious octopus, your choice reveals more than just taste—its a peek into your soul. Take the quiz, discover your spirit creature, and learn what makes you uniquely you. It’s playful, insightful, and maybe even a little surprising. Ready to find out who you really are?')
