from pydantic import BaseModel, constr
from typing import List

class BatikArticle(BaseModel):
    document_id: constr(strip_whitespace=True)
    name: constr(strip_whitespace=True)
    desc_batik: constr()
    teknik_pembuatan: List[str]
    link_proses_pembuatan: str
    asal: str
    image: str
    tahun: str
    arti_motif: str

    class Config:
        json_schema_extra = {
            "example": {
                "document_id": "batik_example",
                "name": "Batik Example",
                "desc_batik": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "teknik_pembuatan": ["Tulis", "Cap", "Celup", "Lukis"],
                "link_proses_pembuatan": "https://example.com",
                "asal": "AsalExample",
                "image": "https://example.com",
                "tahun": "2000",
                "arti_motif": "Example"
            }
        }

class BatikArticleList(BaseModel):
    articles: List[BatikArticle]

    class Config:
        json_schema_extra = {
            "example": {
                "articles": [
                    {
                        "document_id": "batik_example",
                        "name": "Batik Example",
                        "desc_batik": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                        "teknik_pembuatan": ["Tulis", "Cap", "Celup", "Lukis"],
                        "link_proses_pembuatan": "https://example.com",
                        "asal": "AsalExample",
                        "image": "https://example.com",
                        "tahun": "2000",
                        "arti_motif": "Example"
                    },
                    {
                        "document_id": "batik_example",
                        "name": "Batik Example",
                        "desc_batik": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                        "teknik_pembuatan": ["Tulis", "Cap", "Celup", "Lukis"],
                        "link_proses_pembuatan": "https://example.com",
                        "asal": "AsalExample",
                        "image": "https://example.com",
                        "tahun": "2000",
                        "arti_motif": "Example"
                    }
                ]
            }
        }