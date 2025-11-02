Run Express + Mongo backend:

1. Install dependencies:
   cd express-mongo
   npm install

2. Seed DB (ensure MongoDB running):
   MONGO_URI=mongodb://localhost:27017/car_dealers npm run seed

3. Start server:
   MONGO_URI=mongodb://localhost:27017/car_dealers npm start

Endpoints:
- GET /dealers                -> list all dealers (no reviews)
- GET /dealer/:dealer_id      -> dealer details with reviews
- GET /dealers/state/:state   -> dealers by state (e.g., /dealers/state/KS)
- GET /reviews?dealer_id=1    -> reviews for dealer_id=1
- GET /cars.png               -> returns cars.png image
