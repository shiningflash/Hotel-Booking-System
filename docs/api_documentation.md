# Hotel Reservation System

-------------------------

## API Documentation (Swagger)

```
{{base_url}}/swagger/

# for local docker
http://localhost:8010/swagger/
```

[![API Documentation Swagger](https://img.shields.io/badge/Docs-API%20Documentation%20Swagger-blue?style=for-the-badge)](https://github.com/shiningflash/django-reservation-system/blob/master/docs/api_documentation.md) [![API Documentation Insomnia](https://img.shields.io/badge/Docs-API%20Documentation%20Insomnia-blue?style=for-the-badge)](https://github.com/shiningflash/django-reservation-system/blob/master/docs/api_documentation_insomnia.json)

----------------------

## Run in Docker

```
$ docker-compose up --build

# for migrations and others
$ docker exec -it hotelbookingsystem_app_1 bash
:/app# python3 manage.py makemigrations
:/app# python3 manage.py migrate
:/app# python3 manage.py createsuperuser

# extra: to avoid proxy bind
$ sudo netstat -pna | grep 5434
$ sudo kill <PID>

# run in docker everytime
$ docker-compose up
```

# Admin

## Register New Admin - API

Note: A previous super-user admin can only register for new admin.

```
POST {{host}}/api/account/register
```

**Request**
```
curl --request POST \
  --url http://localhost:8010/api/account/register \
  --header 'Content-Type: application/json' \
  --data '{
	"email": "yourname@gmail.com",
	"first_name": "Your_First_Name",
	"last_name": "Your_Last_Name",
	"password": "hbfdy776GFy",
	"password2": "hbfdy776GFy"
}'
```

**Response**
```
{
  "response": "Successfully registered a new admin.",
  "email": "yourname@gmail.com",
  "first_name": "Your_First_Name",
  "last_name": "Your_Last_Name",
  "token": "9031c07dad0f8a869c5551256a110cb7f3675228"
}
```

## Login User API

```
POST {{host}}/api/account/login
```

**Request**
```
curl --request POST \
  --url http://localhost:8010/api/account/login \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "yourname@gmail.com",
	"password": "YOURPASSWORD"
}'
```

**Response**
```
{
  "token": "d94ffca2c287885ca575555f9b019d6d01c25f31"
}
```

## Change Password API

```
PUT {{host}}/api/account/change-password
```

**Request**
```
curl --request PUT \
  --url http://localhost:8010/api/account/change-password \
  --header 'Authorization: Token d94ffca2c287885ca57c7265552019d6d01c25f31' \
  --header 'Content-Type: application/json' \
  --data '{
    "old_password": "dhfj766#@FGfsa",
    "new_password": "FRY5^^%75@@hgs"
}'
```
**Response**
```
"Password updated successfully"
```

## Reset Password Request API

```
POST {{host}}/api/password_reset/
```

A secret token will sent to your mail.

**Request**
```
curl --request POST \
  --url http://localhost:8010/api/password_reset/ \
  --header 'Content-Type: application/json' \
  --data '{
	"email": "yourname@gmail.com"
}'
```
**Response**
```
{
  "status": "OK"
}
```

## Reset Password Confirm API

```
POST {{host}}/api/password_reset/confirm/
```

Use the `secret token` that sent to your mail.

**Request**
```
curl --request POST \
  --url http://localhost:8010/api/password_reset/confirm/ \
  --header 'Authorization: Token d94ffca2c287885ca555526f9b019d6d01c25f31' \
  --header 'Content-Type: application/json' \
  --data '{
    "email": "amirul@gmail.com",
    "token": "4fae77cc94a4c76cf87541165555de57575fe15eeba5d4b",
    "password":"HG565%@@#fsgQW"
}'
```

**Response**
1. for wrong token
```
{ "status": "notfound" }
```
2. for same or similar password as previous
```
{
  "password": [
    "The password is too similar to the last name."
  ]
}
```
3. correct token and new valid password
```
{ "status": "OK" }
```

# Customer

## Customer List API


```
GET {{host}}/api/customer/
```

**Request**
```
curl --request GET \
  --url http://localhost:8010/api/customer/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```

**Response**
```
{
  "meta_data": {
    "count": 2,
    "page_size": 12,
    "next": null,
    "previous": null
  },
  "data": [
    {
      "id": 3,
      "phone_no": "01521300304",
      "first_name": "Nabil",
      "last_name": "Ahsan",
      "email": null,
      "gender": "male",
      "occupation": null,
      "country": null
    },
    {
      "id": 2,
      "phone_no": "01521300303",
      "first_name": "Labib",
      "last_name": "Ahsan",
      "email": null,
      "gender": "male",
      "occupation": null,
      "country": null
    }
  ]
}
```

## Customer Onboarding API

```
POST {{host}}/api/customer/
```

**Request**
```
curl --request POST \
  --url http://localhost:8010/api/customer/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1 \
  --data '{
	"phone_no": "01521300304",
	"first_name": "Nabil",
	"last_name": "Ahsan"
}'
```

**Response**
```
{
  "id": 3,
  "created_at": "2021-09-06T10:42:25.733801Z",
  "updated_at": "2021-09-06T10:42:25.733835Z",
  "created_by": "amirul@gmail.com",
  "updated_by": "",
  "phone_no": "01521300304",
  "first_name": "Nabil",
  "last_name": "Ahsan",
  "email": null,
  "gender": "male",
  "occupation": null,
  "country": null,
  "address": null,
  "details": null
}
```

## Customer Details API

```
GET {{host}}/api/customer/2/
```

**Request**
```
curl --request GET \
  --url http://localhost:8010/api/customer/2/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```
**Response**
```
{
  "id": 2,
  "created_at": "2021-09-06T10:41:44.556618Z",
  "updated_at": "2021-09-06T10:41:44.556645Z",
  "created_by": "",
  "updated_by": "",
  "phone_no": "01521300303",
  "first_name": "Labib",
  "last_name": "Ahsan",
  "email": null,
  "gender": "male",
  "occupation": null,
  "country": null,
  "address": null,
  "details": null
}
```

## Customer Update API

```
PATCH {{host}}/api/customer/<int:pk>/
```

**Request**
```
curl --request PATCH \
  --url http://localhost:8010/api/customer/1/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1 \
  --data '{
	"country": "Japan"
}'
```
**Response**
```
"Updated successfully"
```

# Room

## Room List API


```
GET {{host}}/api/room/
```

**Request**
```
curl --request GET \
  --url http://localhost:8010/api/room/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```

**Response**
```
{
  "meta_data": {
    "count": 2,
    "page_size": 12,
    "next": null,
    "previous": null
  },
  "data": [
    {
      "id": 2,
      "created_at": "2021-09-06T11:14:19.930253Z",
      "updated_at": "2021-09-06T11:14:19.930289Z",
      "created_by": "amirul@gmail.com",
      "updated_by": "",
      "room_no": "B1",
      "floor_no": 2,
      "capacity": 3,
      "price": 1200.0,
      "details": "Nice room"
    },
    {
      "id": 1,
      "created_at": "2021-09-06T05:58:06.220697Z",
      "updated_at": "2021-09-06T05:58:06.220730Z",
      "created_by": "",
      "updated_by": "",
      "room_no": "A1",
      "floor_no": 1,
      "capacity": 2,
      "price": 1200.0,
      "details": null
    }
  ]
}
```

## Room Create API

```
POST {{host}}/api/room/
```

**Request**
```
curl --request POST \
  --url http://localhost:8010/api/room/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1 \
  --data '{
	"room_no": "B1",
	"floor_no": 2,
	"capacity": 3,
	"price": 1200.0,
	"details": "Nice room"
}'
```

**Response**
```
{
  "id": 2,
  "created_at": "2021-09-06T11:14:19.930253Z",
  "updated_at": "2021-09-06T11:14:19.930289Z",
  "created_by": "amirul@gmail.com",
  "updated_by": "",
  "room_no": "B1",
  "floor_no": 2,
  "capacity": 3,
  "price": 1200.0,
  "details": "Nice room"
}
```

## Room Details API

```
GET {{host}}/api/room/2/
```

**Request**
```
curl --request GET \
  --url http://localhost:8010/api/room/2/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```
**Response**
```
{
  "id": 2,
  "created_at": "2021-09-06T11:14:19.930253Z",
  "updated_at": "2021-09-06T11:14:19.930289Z",
  "created_by": "amirul@gmail.com",
  "updated_by": "",
  "room_no": "B1",
  "floor_no": 2,
  "capacity": 3,
  "price": 1200.0,
  "details": "Nice room"
}
```

## Room Update API

```
PATCH {{host}}/api/room/2/
```

**Request**
```
curl --request PATCH \
  --url http://localhost:8010/api/room/2/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1 \
  --data '{
	"capacity": 1
}'
```
**Response**
```
"Updated successfully"
```

# Booking

## Booking List API


```
GET {{host}}/api/booking/
```

**Request**
```
curl --request GET \
  --url http://localhost:8010/api/booking/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```

**Response**
```
{
  "meta_data": {
    "count": 2,
    "page_size": 12,
    "next": null,
    "previous": null
  },
  "data": [
    {
      "id": 2,
      "customer_phone_no": "01521300303",
      "price": 900.0,
      "discounted_price": 900.0,
      "booking_time": "2021-09-06T17:46:30.410920Z",
      "booking_start_time": "2021-09-06T17:46:30.410920Z",
      "booking_end_time": "2021-11-06T17:46:30.410920Z",
      "last_checkin_time": null,
      "last_checkout_time": null,
      "room": 2
    },
    {
      "id": 1,
      "customer_phone_no": "01521300303",
      "price": 400.0,
      "discounted_price": 400.0,
      "booking_time": "2021-09-06T17:46:30.410920Z",
      "booking_start_time": "2021-09-06T17:46:30.410920Z",
      "booking_end_time": "2021-11-06T17:46:30.410920Z",
      "last_checkin_time": null,
      "last_checkout_time": null,
      "room": 1
    }
  ]
}
```

## Booking Create API

```
POST {{host}}/api/booking/
```

**Request**
```
curl --request POST \
  --url http://localhost:8010/api/booking/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1 \
  --data '{
	"customer_phone_no": "01521300303",
	"booking_time": "2021-09-06T17:46:30.410920",
	"booking_start_time": "2021-09-06T17:46:30.410920",
	"booking_end_time": "2021-11-06T17:46:30.410920",
	"room": 5,
	"discounted_price": 1200,
	"price": 1500
}'
```

**Response**
```
{
  "id": 3,
  "created_at": "2021-09-06T13:06:37.004743Z",
  "updated_at": "2021-09-06T13:06:37.004763Z",
  "created_by": "amirul@gmail.com",
  "updated_by": "",
  "customer_phone_no": "01521300303",
  "price": 1500.0,
  "discounted_price": 1200.0,
  "booking_time": "2021-09-06T17:46:30.410920Z",
  "booking_start_time": "2021-09-06T17:46:30.410920Z",
  "booking_end_time": "2021-11-06T17:46:30.410920Z",
  "last_checkin_time": null,
  "last_checkout_time": null,
  "room": 5
}
```

## Booking Details API

```
GET {{host}}/api/booking/<int:pk>/
```

**Request**
```
curl --request GET \
  --url http://localhost:8010/api/booking/3/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```
**Response**
```
{
  "id": 3,
  "created_at": "2021-09-06T13:06:37.004743Z",
  "updated_at": "2021-09-06T13:06:37.004763Z",
  "created_by": "amirul@gmail.com",
  "updated_by": "",
  "customer_phone_no": "01521300303",
  "price": 1500.0,
  "discounted_price": 1200.0,
  "booking_time": "2021-09-06T17:46:30.410920Z",
  "booking_start_time": "2021-09-06T17:46:30.410920Z",
  "booking_end_time": "2021-11-06T17:46:30.410920Z",
  "last_checkin_time": null,
  "last_checkout_time": null,
  "room": 5
}
```

# Payment

## Payment List API


```
GET {{host}}/api/payment/
```

**Request**
```
curl --request GET \
  --url http://localhost:8010/api/payment/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```

**Response**
```
{
  "meta_data": {
    "count": 1,
    "page_size": 12,
    "next": null,
    "previous": null
  },
  "data": [
    {
      "id": 1,
      "created_at": "2021-09-06T13:09:35.400355Z",
      "updated_at": "2021-09-06T13:09:35.400384Z",
      "created_by": "amirul@gmail.com",
      "updated_by": "",
      "amount": 90.0,
      "payment_method": "bkash",
      "booking": 3
    }
  ]
}
```

## Payment Create API

```
POST {{host}}/api/payment/
```

**Request**
```
curl --request POST \
  --url http://localhost:8010/api/payment/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1 \
  --data '{
	"booking": 3,
	"amount": 90.00,
	"payment_method": "bkash"
}'
```

**Response**
```
{
  "id": 1,
  "created_at": "2021-09-06T13:09:35.400355Z",
  "updated_at": "2021-09-06T13:09:35.400384Z",
  "created_by": "amirul@gmail.com",
  "updated_by": "",
  "amount": 90.0,
  "payment_method": "bkash",
  "booking": 3
}
```

## Payment Details API

```
GET {{host}}/api/payment/<int:pk>/
```

**Request**
```
curl --request GET \
  --url http://localhost:8010/api/payment/1/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```
**Response**
```
{
  "id": 1,
  "created_at": "2021-09-06T13:09:35.400355Z",
  "updated_at": "2021-09-06T13:09:35.400384Z",
  "created_by": "amirul@gmail.com",
  "updated_by": "",
  "amount": 90.0,
  "payment_method": "bkash",
  "booking": 3
}
```

# Check in/out

## Check in

```
GET {{host}}/api/booking/<int:pk>/checkin/
```

**Request**
```
curl --request PATCH \
  --url http://localhost:8010/api/booking/3/checkin/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```

**Response**
```
{
  "success": "true",
  "message": "Customer successfully checked in."
}
```

## Check out


```
GET {{host}}/api/booking/<int:pk>/checkout/
```

**Request**
```
curl --request PATCH \
  --url http://localhost:8010/api/booking/3/checkout/ \
  --header 'Authorization: Token d2670842182f579117bd7d930921902977b41996' \
  --header 'Content-Type: application/json' \
  --header 'Cookie: csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1' \
  --cookie csrftoken=BQcE6zURfENim1zFBoPulDdiCPsuAiL1krbyK9YEpkPxRTdTpnzXC3Qt1LQKLtQ1
```

**Response**
```
{
  "success": "true",
  "message": "Customer successfully checked out."
}
```

----------------------------

For more details: [amirulislamalmamun@gmail.com](amirulislamalmamun@gmail.com)
