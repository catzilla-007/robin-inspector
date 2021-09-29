from fastapi import FastAPI

app = FastAPI()


@app.get('/api/v1/nft/{nft_id}/water-level')
def get_water_level(nft_id: int):
    return {
        'timestamp': '2021-03-22 10:22:11',
        'type': 'water-level',
        'nft': nft_id,
        'value': 'normal',
    }
