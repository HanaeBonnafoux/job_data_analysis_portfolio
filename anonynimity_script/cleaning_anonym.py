import pandas as pd
import numpy as np
from faker import Faker
faker = Faker()
from pathlib import Path

#loading the data

data_filepath = "anonynimity_script\Analyste_donnee_mtp.csv"
analysts_bdx = pd.read_csv(data_filepath)

# Replace inf and -inf with NaN explicitly
analysts_bdx = analysts_bdx.replace([np.inf, -np.inf], np.nan)

#cleaning
#making up fake names for privacy
analysts_bdx['anonymisation']= analysts_bdx.apply(lambda row: faker.unique.user_name(), axis=1)
#keeping only the columns I want
analysts_bdx_clean = analysts_bdx.loc[:,['anonymisation', 'occupation','job_title', 'company_name', 'gender']]
analysts_bdx_clean.head()

filepath = Path('anon_data_analysts_mtp.csv')
analysts_bdx_clean.to_csv(filepath)  
