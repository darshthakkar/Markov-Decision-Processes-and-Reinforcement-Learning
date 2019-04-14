import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join


def pol_val_graphs():
    grid_name = ['Hard','Easy']

    for g in grid_name:
        df_val = pd.read_csv(str(g)+' Value.csv')
        df_val.columns = ['iter','time','reward','steps','convergence']
        df_pol = pd.read_csv(str(g)+' Policy.csv')
        df_pol.columns = ['iter','time','reward','steps','convergence']

        for col in ['time','reward','steps','convergence']:
            plt.figure()
            plt.plot(df_pol[col].values,label='Policy',color='r')
            plt.plot(df_val[col].values,label='Value',color='b')
            plt.title(str(g)+' Grid '+str(col))
            plt.legend(loc="upper right")
            plt.xlabel('Iterations')
            plt.ylabel(col)
            plt.savefig("./graphs/"+str(g)+'_Grid_'+str(col)+".png")
            #plt.show()

def pol_val_ql_graphs():
    grid_name = ['Hard','Easy']

    for g in grid_name:
        df_val = pd.read_csv(str(g)+' Value.csv')
        df_val.columns = ['iter','time','reward','steps','convergence']
        df_pol = pd.read_csv(str(g)+' Policy.csv')
        df_pol.columns = ['iter','time','reward','steps','convergence']

        files = [f for f in listdir("./") if isfile(f) and str(g)+' Q-L' in f]
        f_best = files[0]
        rew_sum = -100000
        for f in files:
            df_temp = pd.read_csv(f)
            df_temp.columns = ['iter','time','reward','steps','convergence']
            t = sum(df_temp['reward'])
            if(rew_sum < t):
                rew_sum = t
                f_best = f

        df_ql = pd.read_csv(f_best)
        df_ql.columns = ['iter','time','reward','steps','convergence']

        for col in ['time','reward','steps','convergence']:
            plt.figure()
            plt.plot(df_pol[col].values,label='Policy',color='r')
            plt.plot(df_val[col].values,label='Value',color='b')
            plt.plot(df_ql[col].values,label='Q-Learning',color='g')
            plt.title(str(g)+' Grid '+str(col))
            plt.legend(loc="upper right")
            plt.xlabel('Iterations')
            plt.ylabel(col)
            plt.savefig("./graphs/"+str(g)+'_Grid_'+str(col)+"_part3.png")
            #plt.show()

if __name__ == '__main__':
    pol_val_graphs()
    pol_val_ql_graphs()
