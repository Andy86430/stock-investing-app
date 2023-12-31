from typing import Any
import numpy as np
import streamlit as st
import pandas as pd


def animation_demo() -> None:

    stock_list = pd.read_csv('csv/Database.csv').sort_values("Buying Distance (%)")

    if st.button("Produce Bullish Watchlist"):
        watchlist = pd.read_excel('xlsx/IBD Data Tables.xlsx').dropna()
        watchlist = watchlist.rename(columns=watchlist.iloc[0]).drop(watchlist.index[0])
        # watchlist['Zack Rank'] = watchlist['Symbol'].apply(lambda x: Zacks_Rank(x))
        # watchlist = watchlist.loc[(watchlist['Zack Rank'].isin(['Buy', 'Strong Buy']))]
        # watchlist['PS'] = watchlist['Symbol'].apply(lambda x: get_PSratio(x))
        # watchlist = watchlist.sort_values(by=['PS'])
        watchlist['Symbol'].to_csv('csv/IBD.csv', index=False)
    
    table = pd.read_csv('csv/IBD.csv')
    st.table(table)

    # Interactive Streamlit elements, like these sliders, return their value.
    # This gives you an extremely simple interaction model.
    iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
    separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

    # Non-interactive elements return a placeholder to their location
    # in the app. Here we're storing progress_bar to update it later.
    progress_bar = st.sidebar.progress(0)

    # These two elements will be filled in later, so we create a placeholder
    # for them using st.empty()
    frame_text = st.sidebar.empty()
    image = st.empty()

    m, n, s = 960, 640, 400
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

    for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
        # Here were setting value for these two elements.
        progress_bar.progress(frame_num)
        frame_text.text("Frame %i/100" % (frame_num + 1))

        # Performing some fractal wizardry.
        c = separation * np.exp(1j * a)
        Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
        C = np.full((n, m), c)
        M: Any = np.full((n, m), True, dtype=bool)
        N = np.zeros((n, m))

        for i in range(iterations):
            Z[M] = Z[M] * Z[M] + C[M]
            M[np.abs(Z) > 2] = False
            N[M] = i

        # Update the image placeholder by calling the image() function on it.
        image.image(1.0 - (N / N.max()), use_column_width=True)

    # We clear elements by calling empty on them.
    progress_bar.empty()
    frame_text.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="Watchlist", page_icon="book")
st.markdown("# Watchlist")
st.sidebar.header("Animation Demo")
st.write(
    """This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters."""
)

animation_demo()
