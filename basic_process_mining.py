import pandas as pd
import sys

def process_event_log(filename):
    df = pd.read_csv(filename, sep=';')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.sort_values(by=['Case', 'Timestamp'])
    
    
    num_events = len(df)
    num_cases = df['Case'].nunique()
    num_activities = df['Activity'].nunique()

    def join_activities(activities):
        return '-'.join(activities)

    case_variants = df.groupby('Case')['Activity'].apply(join_activities)
    print(case_variants.unique())
    num_variants = case_variants.nunique()
    
    print(f"# Events: {num_events}")
    print(f"# Cases: {num_cases}")
    print(f"# Activities: {num_activities}")
    print(f"# Variants: {num_variants}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python basic_process_mining.py <filename>")
    else:
        process_event_log(sys.argv[1])
