import pandas as pd
import numpy as np

def get_line_chart_data():

    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

get_line_chart_data()