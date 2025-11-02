// seed.js
const mongoose = require('mongoose');
const Dealer = require('./models/dealerModel');
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/car_dealers';

mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(async () => {
    console.log('Connected to MongoDB:', MONGO_URI);
    await Dealer.deleteMany({});

    const dealers = [
      {
        dealer_id: 1,
        name: 'Kansas Auto Plaza',
        address: '123 Main St',
        city: 'Wichita',
        state: 'KS',
        zip: '67202',
        lat: 37.6872,
        long: -97.3301,
        reviews: [
          { name: 'Alice', review: 'Great service.', rating: 5, sentiment: 'positive', purchase_date: new Date('2024-09-01'), car_make: 'Toyota', car_model: 'Camry' },
          { name: 'Bob', review: 'Average experience.', rating: 3, sentiment: 'neutral', purchase_date: new Date('2024-10-05'), car_make: 'Honda', car_model: 'Civic' }
        ]
      },
      {
        dealer_id: 2,
        name: 'Omaha Motors',
        address: '789 Auto Blvd',
        city: 'Omaha',
        state: 'NE',
        zip: '68102',
        lat: 41.2565,
        long: -95.9345,
        reviews: [
          { name: 'Charlie', review: 'Not satisfied', rating: 2, sentiment: 'negative', purchase_date: new Date('2024-08-10'), car_make: 'Ford', car_model: 'F-150' }
        ]
      },
      {
        dealer_id: 3,
        name: 'Kansas City Cars',
        address: '456 Dealer Rd',
        city: 'Kansas City',
        state: 'KS',
        zip: '66101',
        lat: 39.0997,
        long: -94.5786,
        reviews: []
      }
    ];

    await Dealer.insertMany(dealers);
    console.log('Seeded dealers.');
    process.exit(0);
  })
  .catch(err => {
    console.error('MongoDB connection error:', err);
    process.exit(1);
  });
