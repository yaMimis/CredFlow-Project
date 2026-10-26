from fastapi import FastAPI, HTTPException
import random

app = FastAPI(
    tittle="CredFlow - API Open Finance",
    version="1.0.0",
    description="Endpoint que fornece o extrato de crédito do cliente conforme consentimento ativo",
)

@app.get("/open-finance/extrato/{account_id}")
def obter_extrato_open_finance(account_id: int):
    consentimento_ativo = True

    if not consentimento_ativo:
        raise HTTPException(status_code=403, detail="Consentimento revogado para esta conta.")
    return{
        "consent_id": f"urn:openid:target:consent-{account_id}",
        "status": "ATIVO",
        "cliente": {
            "account_id": account_id,
            "instituicao_origem": f"Banco concorrente {account_id}",
        },
        "fluxo_caixa_resumo": {
            "renda_media": 6500.00, #dado fictício (alterar)
            "saldo_minimo": 500.00, #dado fictício (alterar)
            "meses_saldo_negativo": 1 #dado fictício (alterar)
        }
    }
