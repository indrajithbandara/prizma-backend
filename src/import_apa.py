import pandas as pd
import sqlalchemy

import settings

df = pd.read_csv(settings.APA_WITH_CUSTOM_IDS, sep=';', engine='python')

df = df.rename(columns={
    'URL': 'url',
    'Meno': 'meno',
    'PSC': 'psc',
    'Obec': 'obec',
    'Opatrenie - Kod': 'opatrenie_kod',
    'Opatrenie': 'opatrenie',
    'Suma': 'suma',
    'Rok': 'rok',
    'custom_id': 'custom_id'
})
types_dict = {
    'URL': sqlalchemy.types.TEXT,
    'Meno': sqlalchemy.types.TEXT,
    'PSC': sqlalchemy.types.INT,
    'Obec': sqlalchemy.types.TEXT,
    'Opatrenie - Kod': sqlalchemy.types.TEXT,
    'Opatrenie': sqlalchemy.types.TEXT,
    'Suma': sqlalchemy.types.FLOAT,
    'Rok': sqlalchemy.types.INT,
    'custom_id': sqlalchemy.types.INT,
}

df['psc'] = df['psc'].apply(lambda x: str(x).replace(' ', ''))


conn = sqlalchemy.create_engine(settings.DATABASE_URL)
df.to_sql('apa_prijimatelia', con=conn, index=False, dtype=types_dict, if_exists='replace')
