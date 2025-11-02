const express = require('express');
const router = express.Router();
const Dealer = require('../models/dealerModel');

// GET all dealers
router.get('/dealers', async (req, res) => {
  const dealers = await Dealer.find({}, '-reviews');
  res.json(dealers);
});

// GET dealer by dealer_id and include reviews
router.get('/dealer/:dealer_id', async (req, res) => {
  const dealer = await Dealer.findOne({ dealer_id: Number(req.params.dealer_id) });
  if (!dealer) return res.status(404).json({ error: 'Dealer not found' });
  res.json(dealer);
});

// GET dealers by state (state param is like KS)
router.get('/dealers/state/:state', async (req, res) => {
  const dealers = await Dealer.find({ state: req.params.state.toUpperCase() }, '-reviews');
  res.json(dealers);
});

// GET reviews for dealer (query param ?dealer_id=1)
router.get('/reviews', async (req, res) => {
  const dealer_id = Number(req.query.dealer_id);
  if (!dealer_id) return res.status(400).json({ error: 'dealer_id required' });
  const dealer = await Dealer.findOne({ dealer_id });
  if (!dealer) return res.status(404).json({ error: 'Dealer not found' });
  res.json(dealer.reviews);
});

module.exports = router;
