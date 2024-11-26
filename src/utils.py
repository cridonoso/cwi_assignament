import pandas as pd
import numpy as np

def format_table(row):
    table = []
    for x in row:
        table.append(list(x))
    t = pd.DataFrame(table[1:], columns=table[0])
    return t

def fix_duplicated_columns(row):
    is_duplicated = row.columns.duplicated() 
    if np.any(is_duplicated):
        count = 2
        new_column = []
        for k, cname in enumerate(row.columns):
            if is_duplicated[k]:
                cname = '{}_{}'.format(cname, count)
                count+=1
            else:
                count=2

            new_column.append(cname)
        # print(new_column)
        # print(list(row.columns))
        row.columns = new_column
    return row

def get_sql_tuples(table, context, db_id):
    tuples = []
    for i, roww in table.iterrows():
        columns = list(context.keys()) + list(roww.index.values)
        sqlstr = 'INSERT INTO table_{} ({}) '.format(db_id, ', '.join(columns))
        values = list(context.values()) + list(roww.values)
        sqlstr+='VALUES ({})'.format(', '.join(values))
        tuples.append(sqlstr)
    return tuples

def get_accuracy(queries, top_5):
    accuracy_vector = [] 
    for k, i in enumerate(queries['database_id']):
        if i in top_5[k]:
            accuracy_vector.append(1)
        else:
            accuracy_vector.append(0)
    return accuracy_vector