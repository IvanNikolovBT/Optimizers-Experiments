import pandas as pd

def summarize_results(file_path):

    df = pd.read_csv(file_path)

    total_duration = df['Duration'].sum()

    max_crossval_algo = df.loc[df['Cross-validated R²'].idxmax(), 'Algo']
    max_test_r2_algo = df.loc[df['Test R²'].idxmax(), 'Algo']
    max_test_rmse_algo = df.loc[df['Test RMSE'].idxmin(), 'Algo']

    return {
        'total_duration': total_duration,
        'max_crossval_algo': max_crossval_algo,
        'max_test_r2_algo': max_test_r2_algo,
        'max_test_rmse_algo': max_test_rmse_algo
    }

path="/home/ivan/Desktop/BIP_lokalno/net_7_results.csv"
print(summarize_results(path))