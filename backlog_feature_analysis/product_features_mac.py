# This code is to track progress towards features in a query
# Set up 
	# 1. Create query in VSTS with features of interest. Add column option for "Story Points"
	# 2. Export query from VSTS and save as .csv to location with python code
	# 3. Edit the below section marked "EDIT BELOW"

# -->> EDIT BELOW
# Copy and paste the query from VSTS and save to the library containing this notebook 
filename = "sample_data/product_sample_data_mac.csv"
# ---------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

# --- Import and attach feature names to stories
df = pd.read_csv(filename, header = 0)
df = df.replace(np.nan, '', regex=True)

# Assign Feature label to User Story (diff for Mac)
df['Feature'] = ""
feature=df['Title'][0]
for i in range(0,len(df)):
    if df['Work Item Type'][i]!="Feature":
        df['Feature'][i]= feature;
        
    else:
        feature = df['Title'][i]
        df['Feature'][i] = feature

# --- Calculate points per feature

features = df['Feature'].unique()

total_MVP_points_per_feat = []
closed_MVP_points_per_feat = []
percent_MVP_complete = []
feat_iteration_path = []

df['Story Points'] = df[['Story Points']].convert_objects(convert_numeric=True).fillna(0)

for i in range(0,len(features)):
    num_closed_points = int(df[(df['Feature']== features[i])&(df['State']=='Closed')].sum()["Story Points"])
    closed_MVP_points_per_feat.append(num_closed_points)
    
    num_tot_points = int(df[df['Feature']== features[i]].sum()["Story Points"])
    total_MVP_points_per_feat.append(num_tot_points)
    
    if num_tot_points != 0:
        percent = int(round(num_closed_points/num_tot_points*100))
        percent_MVP_complete.append(percent)
    else:
        percent_MVP_complete.append(0)
        
    feat_iteration_path.append(df[(df['Feature']==features[i])&(df['Work Item Type']=='Feature')].iloc[0]['Iteration Path'])
        
# combine into df    
featdf = {'Feature':features, '# MVP Stories': total_MVP_points_per_feat, '# MVP Closed': closed_MVP_points_per_feat, '% MVP Complete': percent_MVP_complete, 'Iteration Path': feat_iteration_path}
featdf = pd.DataFrame (data = featdf)
featdf = featdf.dropna()


# Includes only features with MVP stories and assigned to a team
MVP_featdf = featdf[(featdf['Iteration Path']!=('\Fuse'))&(featdf['# MVP Stories']>0)]
MVP_featdf_rev = MVP_featdf[::-1]


# --- MVP Burnup
# Number of MVP points
num_mvp = MVP_featdf['# MVP Stories'].sum()
mvp_left = MVP_featdf['# MVP Stories'].sum()-MVP_featdf['# MVP Closed'].sum()
MVP_percent_complete = MVP_featdf['# MVP Closed'].sum()/MVP_featdf['# MVP Stories'].sum()*100

# --- Feature Bar Graph
ax1 = MVP_featdf_rev.plot.barh(title="MVP Feature Progress", x="Feature", y= "# MVP Stories",color='r', figsize=(14 ,10));
MVP_featdf_rev.plot.barh(x="Feature", y= "# MVP Closed", ax=ax1, color='b', width = 0.5);
ax1.set_yticklabels(MVP_featdf_rev['Feature'], rotation=0);
ax1.set_xlim(0, 60);
for i, cards in enumerate(list(MVP_featdf_rev['# MVP Stories'])):
    ax1.annotate(str(cards-MVP_featdf_rev['# MVP Closed'].iloc[i]), xy = (cards, i), va='center')

print('% Story Points Complete = ', MVP_percent_complete)
print('Total # Story Points = ', num_mvp)
print('# Remaining Story Points = ', mvp_left)

plt.tight_layout()
plt.show()