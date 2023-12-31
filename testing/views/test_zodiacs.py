from app import create_zodiac, delete_zodiacs, delete_zodiac_base
from models import Zodiacs, db


def test_zodiac_details_status_code(client):
    # delete_zodiacs()
    # delete_zodiac_base()
    create_zodiac()
    zodiac = Zodiacs(name="name", date_bth="1999-12-12", id_zodiac=3, zodiac_name="zodiac_name")
    db.session.add(zodiac)
    db.session.commit()
    zodiac_id = Zodiacs.query.first().id
    print(zodiac_id)
    response = client.get(f'/zodiacs/{zodiac_id}/')
    assert response.status_code == 200
