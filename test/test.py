import numpy as np
import pandas as pd
import random

chars = [chr(i) for i in range(97, 123)]
digtals = [str(i) for i in range(97, 123)]

field_list = []
# 随机生成500x10的df，随机字段名
for i in range(10):
    randoms = 'fnd' + '_' + ''.join(random.sample(chars, 3)) + "_" + "".join(random.sample(digtals, 1))
    field_list.append(randoms)
datas = np.random.random((500, 10))
df = pd.DataFrame(columns=field_list, data=datas)


# 取出两个字段对应的值 做ts_regression
def ts_regression(x_df):
    """
    此处省略
    :param x_df:
    :return:
    """

    return x_df


def t_score(fieldA, num=500):
    df[f"{fieldA}_mean"] = df[fieldA].mean()
    return df


for i in range(0, len(df.columns.to_list())):
    fieldA = field_list[i]
    df = t_score(fieldA)

means_list = [i for i in df.columns.to_list() if i.endswith("_mean")]
for i in range(0, len(means_list)):
    for j in range(i + 1, len(field_list)):
        fieldA = field_list[i]
        fieldB = field_list[j]
        df.loc[:, fieldA:fieldB].apply(ts_regression)
