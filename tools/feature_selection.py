#! pip install woe

import woe.feature_process as fp
import woe.eval as eval

def cal_iv(df, cate_vars, cont_vars, target):
  #%% woe分箱, iv and transform
  df_woe = df 
  civ_list = []
  n_positive = sum(df[target])
  n_negtive = len(df) - n_positive
  for var in cate_vars:
      civ = fp.proc_woe_discrete(df, var, n_positive, n_negtive, 0.05*len(df), alpha=0.05)
      civ_list.append(civ)
      df_woe[var] = fp.woe_trans(df[var], civ)
  
  for var in cont_vars:
      civ = fp.proc_woe_continuous(df, var, n_positive, n_negtive, 0.05*len(df), alpha=0.05)
      civ_list.append(civ)
      df_woe[var] = fp.woe_trans(df[var], civ)
    
  civ_df = eval.eval_feature_detail(civ_list,'output_feature_detail_0927.csv')
  df_iv = civ_df[['var_name','iv']].drop_duplicates()
  return df_iv.sort_values('iv',ascending=False)