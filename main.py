import os
import pandas as pd
from fastapi import FastAPI, File, UploadFile, HTTPException
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.post("/import-csv/")
async def import_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="O arquivo deve ser CSV.")
    try:
        df = pd.read_csv(file.file, sep=';', encoding='utf-8')
        df.columns = [c.lower().replace(' ', '_').replace('ã', 'a').replace('ç', 'c').replace('é', 'e').replace('í', 'i').replace('ô', 'o').replace('ú', 'u') for c in df.columns]
        df = df.rename(columns={
            'exercicio': 'exercicio',
            'nivel_1': 'nivel1',
            'nivel_2': 'nivel2',
            'nivel_3': 'nivel3',
            'nivel_4': 'nivel4',
            'classe_do_custo': 'classe_custo',
            'descricao_despesa': 'descricao_despesa',
            'divisao': 'divisao',
            'empresa_do_rateio': 'empresa_rateio',
            'descricao_da_empresa_do_rateio': 'descricao_empresa_rateio',
            'centro_custo': 'centro_custo',
            'texto_descritivo': 'texto_descritivo',
            'prev._janeiro': 'prev_janeiro',
            'prev._fevereiro': 'prev_fevereiro',
            'prev._marco': 'prev_marco',
            'prev._abril': 'prev_abril',
            'prev._maio': 'prev_maio',
            'prev._junho': 'prev_junho',
            'prev._julho': 'prev_julho',
            'prev._agosto': 'prev_agosto',
            'prev._setembro': 'prev_setembro',
            'prev._outubro': 'prev_outubro',
            'prev._novembro': 'prev_novembro',
            'prev._dezembro': 'prev_dezembro'
        })
        df.to_sql('orcamento', con=engine, if_exists='append', index=False)
        return {"message": "Importação realizada com sucesso!", "rows": len(df)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 