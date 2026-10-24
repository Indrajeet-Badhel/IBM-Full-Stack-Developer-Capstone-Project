/* Seed-backed Express API for dealership data.
 * It runs without MongoDB for local demos, while keeping the same endpoints
 * used by the Django application and deployment container.
 */
const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3030;
const loadSeed = (file, property) => JSON.parse(
  fs.readFileSync(path.join(__dirname, 'data', file), 'utf8')
)[property];

const dealerships = loadSeed('dealerships.json', 'dealerships');
const reviews = loadSeed('reviews.json', 'reviews');

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => res.send('Welcome to the Dealership API'));
app.get('/health', (req, res) => res.json({ status: 'ok' }));
app.get('/fetchReviews', (req, res) => res.json(reviews));
app.get('/fetchReviews/dealer/:id', (req, res) =>
  res.json(reviews.filter((review) => String(review.dealership) === req.params.id))
);
app.get('/fetchDealers', (req, res) => res.json(dealerships));
app.get('/fetchDealers/:state', (req, res) =>
  res.json(dealerships.filter((dealer) => dealer.state.toLowerCase() === req.params.state.toLowerCase()))
);
app.get('/fetchDealer/:id', (req, res) => {
  const dealer = dealerships.filter((item) => String(item.id) === req.params.id);
  res.json(dealer);
});
app.post('/insert_review', (req, res) => {
  const data = req.body;
  if (!data.dealership || !data.review || !data.name) {
    return res.status(400).json({ error: 'name, dealership, and review are required' });
  }
  const review = { ...data, id: Math.max(0, ...reviews.map((item) => item.id || 0)) + 1 };
  reviews.push(review);
  return res.status(201).json(review);
});

app.listen(port, () => console.log(`Dealership API listening on http://localhost:${port}`));
