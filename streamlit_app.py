import streamlit as st


def run():
    
    st.set_page_config(
        page_title="Market Wizard",
        page_icon="chart_with_upwards_trend",
    )

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
