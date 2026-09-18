import pandas as pd

def get_data():


def generate_cpk_report():
        data = {'测试项': ['流量计A', '流量计B', '流量计C'],
                '均值': [100.1, 100.2, 100.3],
                '标准差': [0.1, 0.2, 0.3],
                'CPK': [1.5, 1.2, 0.8]}

        df = pd.DataFrame(data)
        df.to_excel('d:\python\cpk_report.xlsx', index=False)
        print("CPK报告已生成，文件名为 cpk_report.xlsx")

if __name__ == '__main__':
        generate_cpk_report()