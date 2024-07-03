# Introduction

This charity auctions project enables users to participate in or create their own auctions. It follows best practices, including queryset optimization to avoid the n+1 problem, unit tests to ensure code functionality, caching to improve data handling speed, and containerization to ensure the app runs consistently across different machines.

# Applied Technologies

This project leverages several technologies:
- **Django REST framework** for API development.
- **PostgreSQL** for data storage.
- **Websockets** for real-time user communication.
- **Unit tests** for endpoint testing.
- **Redis** as a message broker and for caching.
- **Gunicorn and Nginx** for managing communication between the React frontend and Django backend.
- **Docker** for containerization.

# Functionality

The project includes:
- **Authentication** with JWT, password reset, and password recovery via email.
- **Auction management** with the ability to create, edit, delete, and view auctions, including descriptions and photos.
- **Bidding** functionality where users can place bids and view all bids on an auction.
- **Notifications** for auction owners when their auction receives a bid.
- **Filtering and searching** to manage auctions by various criteria.
- **User communication** via Websockets for real-time conversations.

# Usage

1. Ensure Docker is installed on your machine.
2. Clone the repository:
   ```sh
   $ git clone https://github.com/Andry925/charity_auctions2.git
   ```
3. Fill in EMAIL_HOST_PASSWORD and EMAIL_HOST_USER in the .env file to enable the email service.
4. Build and run containers
```sh
   $ docker compose up --build
   ```
5. Access the application at 127.0.0.1:80 or check the backend at 127.0.0.1:8000.