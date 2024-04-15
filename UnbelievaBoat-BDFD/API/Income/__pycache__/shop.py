from fastapi import APIRouter, HTTPException
import json

router = APIRouter()

# Ruta para obtener todos los items
@router.get("api/items_shop/{guild_id}/")
async def get_items(guild_id: str):
    try:
        # Carga el archivo JSON que contiene los items
        with open(f"Economy/{guild_id}/data.json", "r") as file:
            data = json.load(file)
            items = data.get("items", [])
            return {"items": items}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="El archivo no existe")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))