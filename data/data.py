class Data:

    @classmethod
    def user_create_payload(cls):
        payload = {
            "id": 5555624421,
            "username": "alican",
            "firstName": "Alican",
            "lastName": "Ozsoy",
            "email": "alicanozsoy11@hotmail.com",
            "password": "231312",
            "phone": "565465",
            "userStatus": 0
        }
        return payload

    @classmethod
    def headers_payload(cls):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        return headers

    @classmethod
    def params_payload(cls):
        params = {
            "username": "alican",
            "password": "231312"
        }
        return params

    @classmethod
    def create_user_with_list(cls):
        payload = [
            {
                "id": 1,
                "username": "alicantest1",
                "firstName": "alicantest1",
                "lastName": "alicantest1",
                "email": "alicantest1",
                "password": "alicantest1",
                "phone": "111111",
                "userStatus": 0
            },
            {
                "id": 2,
                "username": "alicantest2",
                "firstName": "alicantest2",
                "lastName": "alicantest2",
                "email": "alicantest2",
                "password": "alicantest2",
                "phone": "222222",
                "userStatus": 0
            }, {
                "id": 3,
                "username": "alicantest3",
                "firstName": "alicantest3",
                "lastName": "alicantest3",
                "email": "alicantest3",
                "password": "alicantest3",
                "phone": "33333",
                "userStatus": 0
            },
            {
                "id": 4,
                "username": "alicantest4",
                "firstName": "alicantest4",
                "lastName": "alicantest4",
                "email": "alicantest4",
                "password": "alicantest4",
                "phone": "444444",
                "userStatus": 0
            },
            {
                "id": 5,
                "username": "alicantest5",
                "firstName": "alicantest5",
                "lastName": "alicantest5",
                "email": "alicantest5",
                "password": "alicantest5",
                "phone": "555555",
                "userStatus": 0
            }
        ]
        return payload

    @classmethod
    def create_user_with_array(cls):
        payload = [
            {
                "id": 111111111,
                "username": "alicantest1",
                "firstName": "alicantest1",
                "lastName": "alicantest1",
                "email": "alicantest1",
                "password": "alicantest1",
                "phone": "111111",
                "userStatus": 0
            },
            {
                "id": 111111112,
                "username": "alicantest2",
                "firstName": "alicantest2",
                "lastName": "alicantest2",
                "email": "alicantest2",
                "password": "alicantest2",
                "phone": "222222",
                "userStatus": 0
            }, {
                "id": 111111113,
                "username": "alicantest3",
                "firstName": "alicantest3",
                "lastName": "alicantest3",
                "email": "alicantest3",
                "password": "alicantest3",
                "phone": "33333",
                "userStatus": 0
            },
            {
                "id": 111111114,
                "username": "alicantest4",
                "firstName": "alicantest4",
                "lastName": "alicantest4",
                "email": "alicantest4",
                "password": "alicantest4",
                "phone": "444444",
                "userStatus": 0
            },
            {
                "id": 111111115,
                "username": "alicantest5",
                "firstName": "alicantest5",
                "lastName": "alicantest5",
                "email": "alicantest5",
                "password": "alicantest5",
                "phone": "555555",
                "userStatus": 0
            },
            {
                "id": 111111116,
                "username": "alicantest6",
                "firstName": "alicantest6",
                "lastName": "alicantest6",
                "email": "alicantest6",
                "password": "alicantest6",
                "phone": "666666",
                "userStatus": 0
            },
            {
                "id": 111111117,
                "username": "alicantest7",
                "firstName": "alicantest7",
                "lastName": "alicantest7",
                "email": "alicantest7",
                "password": "alicantest7",
                "phone": "777777777",
                "userStatus": 0
            },
            {
                "id": 111111118,
                "username": "alicantest8",
                "firstName": "alicantest8",
                "lastName": "alicantest8",
                "email": "alicantest8",
                "password": "alicantest8",
                "phone": "88888888",
                "userStatus": 0
            },
            {
                "id": 111111119,
                "username": "alicantest9",
                "firstName": "alicantest9",
                "lastName": "alicantest9",
                "email": "alicantest9",
                "password": "alicantest9",
                "phone": "99999999",
                "userStatus": 0
            }
        ]
        return payload
