import glob
import pandas as pd
import os

def main():
    filenames = collect_csv_files()
    cat_data(filenames)
    write_data(filenames)


def collect_csv_files():
    file_names = []
    for x in glob.glob('*.csv'):
        if x != 'everyone.csv' and x != 'mlp6.csv':
            file_names.append(x)
    return file_names

def cat_data(filenames):
    with open('everyone.csv','w') as csvfile:
        count = 0
        for file in filenames:
            df = pd.read_csv(file, delimiter=',')
            team_name = df.iloc[:,4].name
            check_no_spaces(team_name)
            count = check_camel_case(team_name,count)
            df.to_csv(csvfile)
        print('CamelCase Count: ',count)

def check_no_spaces(team_name):
    if team_name[0].isspace():
        team_name = team_name[1:]
    if ' ' in team_name:
        print('Error: space within team name')
        print('Team name: ')
        print(team_name)

def check_camel_case(team_name,count):
    if team_name[0].islower() is False:
        count += 1
    return count


def write_data(filenames):
    # CSV or JSON
    for file in filenames:
        orig_name = os.path.splitext(file)[0]
        new_name = orig_name + '.json'
        df = pd.read_csv(file, delimiter=',')
        df.to_json(new_name)
    dfmp = pd.read_csv('mlp6.csv', delimiter=',')
    dfmp.to_json('mlp6.json')

if __name__ == "__main__":
    main()