const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dealersRoute = require('./routes/dealers');

const app = express();
app.use(cors());
app.use(express.json());

const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/car_dealers';
mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected:', MONGO_URI))
  .catch(err => console.error('MongoDB connection error:', err));

app.use('/', dealersRoute);

// simple root
app.get('/', (req, res) => res.send('Express-Mongo dealers API is running.'));

// serve cars.png at root for Task 14
const path = require('path');
app.get('/cars.png', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'cars.png'));
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Express server listening on port ${PORT}`));
