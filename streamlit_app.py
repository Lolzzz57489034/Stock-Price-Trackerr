import streamlit as st

# Player Data (Name, Matches, Runs, Wickets, Image URL)
players = {
    "Virat Kohli": {
        "matches": 500, "runs": 25000, "wickets": 4, 
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/71/Virat_Kohli.jpg"
    },
    "Sachin Tendulkar": {
        "matches": 664, "runs": 34357, "wickets": 201, 
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/25/Sachin-Tendulkar.jpg"
    },
    "MS Dhoni": {
        "matches": 538, "runs": 17092, "wickets": 1, 
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d5/MS_Dhoni_2016.jpg"
    },
    "Rohit Sharma": {
        "matches": 450, "runs": 17000, "wickets": 10, 
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Rohit_Sharma.jpg"
    },
    "Kapil Dev": {
        "matches": 356, "runs": 9031, "wickets": 687, 
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/30/Kapil_Dev.jpg"
    },
}

# Streamlit UI
st.title("🏏 Indian Cricketer Stats Viewer")

selected_player = st.selectbox("Select a Player", list(players.keys()))

if selected_player:
    player = players[selected_player]
    
    # Try displaying the image
    try:
        st.image(player["image"], caption=selected_player, width=250)
    except:
        st.write("⚠️ Image could not be loaded.")

    st.write(f"**Matches:** {player['matches']}")
    st.write(f"**Runs:** {player['runs']}")
    st.write(f"**Wickets:** {player['wickets']}")
