import streamlit as st
import pandas as pd
from modules.functions import Zacks_Rank
from modules.functions import get_PSratio

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def run():
    
    # Page config
    st.set_page_config(
        page_title="Market Wizard",
        page_icon="chart_with_upwards_trend",
    )
    
    # Produce a stock watchlist
    st.markdown("""### Actions:""")
    upload = st.file_uploader('Upload "IBD Data Tables.xlsx"', type="xlsx")
    if upload is not None:
        if st.button('Produce Bullish List'):    
            watchlist = pd.read_excel(upload).dropna()
            watchlist = watchlist.rename(columns=watchlist.iloc[0]).drop(watchlist.index[0])
            watchlist['Zack Rank'] = watchlist['Symbol'].apply(lambda x: Zacks_Rank(x))
            watchlist = watchlist.loc[(watchlist['Zack Rank'].isin(['Buy', 'Strong Buy']))]
            watchlist['PS'] = watchlist['Symbol'].apply(lambda x: get_PSratio(x))
            watchlist = watchlist.sort_values(by=['PS'])
            csv = convert_df(watchlist['Symbol'])
            st.download_button("Download",csv,"Bullish List.csv","text/csv",key='download-csv')

    # Useful links
    st.markdown(
        """
        ### Useful Websites:
        - [Zacks](https://www.zacks.com)
        - [TradingView](https://www.tradingview.com/chart/3JwfLY94)
        - [Tipranks](https://www.tipranks.com/dashboard)
        - [IBD](https://www.investors.com/)
    """
    )


if __name__ == "__main__":
    run()
