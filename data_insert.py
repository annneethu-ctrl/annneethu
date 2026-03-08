from data_extraction import *
from db_connection import get_connection



conn = get_connection()

Agg_Trans = ex_data_agg_transaction()
Agg_Trans.to_sql("aggregate_transaction", conn, if_exists="replace", index=False)

Agg_insur=ex_data_agg_insurance()
Agg_insur.to_sql('aggregate_insurance', conn, if_exists='replace', index=False)

Agg_users=ex_data_agg_user()
Agg_users.to_sql('aggregate_users', conn, if_exists='replace', index=False)

Map_Trans=ex_map_trans()
Map_Trans.to_sql('map_transaction',conn,if_exists="replace",index=False)

Map_Insur=ex_map_insurance()
Map_Insur.to_sql('map_insurance',conn,if_exists="replace",index=False)

Map_Users=ex_map_user()
Map_Users.to_sql('map_users',conn,if_exists="replace",index=False)

Top_Trans=ex_top_transaction()
Top_Trans.to_sql('top_transaction',conn,if_exists="replace",index=False)

Top_Insur=ex_top_insurance()
Top_Insur.to_sql('top_insurance',conn,if_exists="replace",index=False)

Top_User=ex_top_user()
Top_User.to_sql('top_user',conn,if_exists="replace",index=False)


print("Data inserted successfully")