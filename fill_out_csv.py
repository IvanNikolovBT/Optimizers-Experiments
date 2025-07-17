import re
import csv
import pandas as pd
def parse_results_to_csv(input_path, output_csv_path):
    name_map = {
        'grid': 'Grid',
        'random': 'Random',
        'bayes': 'Bayes',
        'pso': 'Partical Swarm Optimization',
        'hill_climbing': 'Hill Climbing',
        'ga': 'Genetic Algorithms',
        'sa': 'Simulated Anealing',
        'optuna': 'Optuna',
        'abc': 'Artificial Bee Colony'
    }

    with open(input_path, 'r') as f:
        text = f.read()

    blocks = re.split(r"=+\s*\nStrategy:", text)
    rows = []
    for blk in blocks[1:]:  
        blk = "Strategy:" + blk

        m_name = re.search(r"Strategy:\s*([^\s]+)", blk)
        if not m_name:
            continue
        raw = m_name.group(1).lower()
        algo = name_map.get(raw, raw.title())


        m_cv = re.search(r"Cross-validated R²:\s*([\d.]+)", blk)
        m_test_r2 = re.search(r"Test R²:\s*([\d.]+)", blk)
        m_rmse = re.search(r"Test RMSE:\s*([\d.]+)", blk)
        m_time = re.search(r"Time needed to train\s*([\d.]+)\s*seconds", blk)

        if not (m_cv and m_test_r2 and m_rmse and m_time):
            
            continue

        duration = float(m_time.group(1))
        cv_r2    = float(m_cv.group(1))
        test_r2  = float(m_test_r2.group(1))
        rmse     = float(m_rmse.group(1))

        rows.append({
            'Algo': algo,
            'Duration': duration,
            'Cross-validated R²': cv_r2,
            'Test R²': test_r2,
            'Test RMSE': rmse
        })


    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
            'Algo','Duration','Cross-validated R²','Test R²','Test RMSE'
        ])
        writer.writeheader()
        writer.writerows(rows)

model='extratrees'
number=10
input_path1=f"/home/ivan/Desktop/BIP_lokalno/{model}_{number}_results.txt"
input_path=f"/home/ivan/Desktop/BIP_lokalno/{model}_results_{number}.txt"
input_path=f"/home/ivan/Desktop/BIP_lokalno/{model}_test_results.txt"
output_path=f'{model}_{number}_results.csv'
parse_results_to_csv(input_path, output_path)


def csv_to_latex(csv_path, caption="Summary of Results", label="tab:results"):

    df = pd.read_csv(csv_path)
    latex_table = df.to_latex(
        index=False,
        float_format="%.4f",
        caption=caption,
        label=label,
        column_format="|l|r|r|r|r|",
        header=True,
        escape=False
    )
    print(latex_table)


csv_to_latex(output_path, caption="Summary of XGBoost Tuning Results", label="tab:xgb_results")
