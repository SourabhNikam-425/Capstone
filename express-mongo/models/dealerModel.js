const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const ReviewSchema = new Schema({
  name: String,
  review: String,
  rating: Number,
  sentiment: String,
  purchase_date: Date,
  car_make: String,
  car_model: String
});

const DealerSchema = new Schema({
  dealer_id: Number,
  name: String,
  address: String,
  city: String,
  state: String,
  zip: String,
  lat: Number,
  long: Number,
  reviews: [ReviewSchema]
});

module.exports = mongoose.model('Dealer', DealerSchema);
