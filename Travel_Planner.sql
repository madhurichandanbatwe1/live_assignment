CREATE DATABASE Travel_Planner;

USE Travel_Planner;

CREATE TABLE bookings (
    user_id INT,
    flight_id INT,
    hotel_id INT,
    activity_id INT,
    booking_date DATE
);

INSERT INTO bookings (user_id, flight_id, hotel_id, activity_id, booking_date) VALUES
(1, 101, 201, 301, '2023-07-01'),
(2, 102, 202, 302, '2023-07-02'),
(3, 103, 203, 303, '2023-07-03');
