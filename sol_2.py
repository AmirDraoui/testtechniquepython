import pandas as pd
import json
HEADER = ["reference", "description", "unity", "quantity", "unit_price", "total_price"]
section_item_att = ['order', 'type', 'reference', 'level', 'description']
cell_item_att = ['order', 'type', 'description', 'unity', 'quantity']
INPUT_PATH="test.xlsx"
NROWS = 30 # number of rows to load
DROP_ROWS = [0, 1, 2, 3]

def load_data():
    df = pd.read_excel(INPUT_PATH, header=None, names=HEADER, nrows=NROWS,engine = 'openpyxl')
    df = df.drop(DROP_ROWS)
    df.reset_index(drop=True)
    return df

def main():
    df = load_data()
    items = []
    order_index = 0
    for i in range(len(df)):
        row = df.iloc[i]
        row['order'] = order_index
        if row['reference']==row['reference']:
            row['type'] = 'SECTION'
            row['level'] = 1
            items.append({att:row[att] for att in section_item_att})
        elif row['description'] == row['description']:
            row['type'] = "CELL"
            items.append({ att:row[att] for att in cell_item_att})
        else:
            continue
        order_index+=1
    res = {"items":items}
    # write result to a json file file
    with open('result.json', 'w', encoding='latin1') as json_file:
        json.dump(res, json_file)

    return res




if __name__ == "__main__":
    main()