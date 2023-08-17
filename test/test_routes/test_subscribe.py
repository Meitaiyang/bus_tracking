import json
from flask import jsonify
from app.models.user import Users

def test_index_route(test_client):
    
    # test the success subscribe 
    response = test_client.get('/subscribe/test@gmail.com/278/%E6%8D%B7%E9%81%8B%E5%85%A7%E6%B9%96%E7%AB%99/%E6%BA%AA%E5%8F%A3%E5%9C%8B%E5%B0%8F')
    assert response.status_code == 201
    assert response.json == {"message": "User subscribed successfully"}

    # test the duplicate subscribe
    response = test_client.get('/subscribe/test@gmail.com/278/%E6%8D%B7%E9%81%8B%E5%85%A7%E6%B9%96%E7%AB%99/%E6%BA%AA%E5%8F%A3%E5%9C%8B%E5%B0%8F')
    assert response.status_code == 409
    assert response.json == {"error": "User already subscribed"}

    # test the invaild email
    response = test_client.get('/subscribe/testgmail.com/278/%E6%8D%B7%E9%81%8B%E5%85%A7%E6%B9%96%E7%AB%99/%E6%BA%AA%E5%8F%A3%E5%9C%8B%E5%B0%8F')
    assert response.status_code == 400
    assert response.json == {"error": "Invalid Email"}

    # test the invaild bus number
    response = test_client.get('/subscribe/test@gmail.com/99999/%E6%8D%B7%E9%81%8B%E5%85%A7%E6%B9%96%E7%AB%99/%E6%BA%AA%E5%8F%A3%E5%9C%8B%E5%B0%8F')
    assert response.status_code == 404
    assert response.json == {"error": "Bus not Found"}

    # test the invaild direction
    response = test_client.get('/subscribe/test@gmail.com/278/%E6%8D%B7%E9%81%8B%E6%98%86%E9%99%BD%E7%AB%99/%E6%BA%AA%E5%8F%A3%E5%9C%8B%E5%B0%8F')
    assert response.status_code == 404
    assert response.json == {"error": "Direction not Found"}


    # test the invaild station
    response = test_client.get('/subscribe/test@gmail.com/278/%E6%8D%B7%E9%81%8B%E5%85%A7%E6%B9%96%E7%AB%99/%E6%8D%B7%E9%81%8B%E5%A4%A7%E5%AE%89%E7%AB%99')
    assert response.status_code == 404
    assert response.json == {"error": "Station not Found"}


    user = Users.query.get_or_404(1)
    assert user.email == "test@gmail.com"
    assert user.bus_number == 278
    assert user.direction == "捷運內湖站"
    assert user.station == "溪口國小"