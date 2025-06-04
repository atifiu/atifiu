"""Streamlit entry point for visualizing logs and Trino queries."""

import pandas as pd
import streamlit as st

from .trino_client import TrinoClient
from .log_parser import parse_log_file


def main():
    st.title("Data Engineering Dashboard")

    if st.sidebar.button("Load Trino Tables"):
        client = TrinoClient(host="localhost")
        results = client.query("SHOW TABLES")
        st.write(pd.DataFrame(results))

    log_file = st.sidebar.text_input("Spark log file path")
    if log_file:
        records = parse_log_file(log_file)
        st.write(pd.DataFrame(records))


if __name__ == "__main__":
    main()
