# Hotel Reservation System

A Dockerized Hotel Reservation System built with Django, offering REST APIs for user management, room reservations, payments, and check-ins/check-outs. This project provides seamless Swagger and Insomnia documentation support for developers.

[![API Documentation Swagger](https://img.shields.io/badge/Docs-API%20Documentation%20Swagger-blue?style=for-the-badge)](https://github.com/shiningflash/django-reservation-system/blob/master/docs/api_documentation.md) [![API Documentation Insomnia](https://img.shields.io/badge/Docs-API%20Documentation%20Insomnia-blue?style=for-the-badge)](https://github.com/shiningflash/django-reservation-system/blob/master/docs/api_documentation_insomnia.json)

---

## Features

- **User Management**: Register, login, change password, and manage user profiles.
- **Room Management**: Add, update, and view room details.
- **Customer Management**: Add, update, and view customer details.
- **Booking System**: Manage bookings with real-time check-in/check-out functionality.
- **Payment System**: Record and track payments.
- **API Documentation**: 
  - Swagger: Interactive API documentation available at `http://localhost:8010/swagger/`.
  - Insomnia: Pre-configured API workspace for testing.

---

## Prerequisites

Ensure the following are installed on your system:
- Python 3.x
- Docker and Docker Compose

---

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/shiningflash/django-reservation-system.git
    cd django-reservation-system
    ```

2. Build and run the application using Docker:

    ```bash
    docker-compose up --build
    ```

3. Access Swagger documentation:
    - [Swagger UI](http://localhost:8010/swagger/)

4. Manage migrations:

    ```bash
    docker exec -it hotelbookingsystem_app_1 bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

---

## API Endpoints 

[![API Documentation Swagger](https://img.shields.io/badge/Docs-API%20Documentation%20Swagger-blue?style=for-the-badge)](https://github.com/shiningflash/django-reservation-system/blob/master/docs/api_documentation.md)
[![API Documentation Insomnia](https://img.shields.io/badge/Docs-API%20Documentation%20Insomnia-blue?style=for-the-badge)](https://github.com/shiningflash/django-reservation-system/blob/master/docs/api_documentation_insomnia.json)

### Admin Management
- **Register Admin**: `POST /api/account/register`
- **Login**: `POST /api/account/login`
- **Change Password**: `PUT /api/account/change-password`
- **Password Reset**: 
  - Request: `POST /api/password_reset/`
  - Confirm: `POST /api/password_reset/confirm/`

### Customer Management
- **List Customers**: `GET /api/customer/`
- **Add Customer**: `POST /api/customer/`
- **Update Customer**: `PATCH /api/customer/<id>/`

### Room Management
- **List Rooms**: `GET /api/room/`
- **Add Room**: `POST /api/room/`
- **Update Room**: `PATCH /api/room/<id>/`

### Booking Management
- **List Bookings**: `GET /api/booking/`
- **Add Booking**: `POST /api/booking/`
- **Check-in**: `PATCH /api/booking/<id>/checkin/`
- **Check-out**: `PATCH /api/booking/<id>/checkout/`

### Payment Management
- **List Payments**: `GET /api/payment/`
- **Add Payment**: `POST /api/payment/`

---

## Running Tests

To run the tests, execute:

```bash
docker exec -it hotelbookingsystem_app_1 bash
python3 manage.py test
```

---

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Containerization**: Docker, Docker Compose
- **Database**: PostgreSQL
- **Documentation**: Swagger, Insomnia
- **CI/CD**: Github Actions

---

## Contributing

We welcome contributions! Please follow the steps below:

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For more details, reach out to:
- **Email**: [amirulislamalmamun@gmail.com](mailto:amirulislamalmamun@gmail.com)
