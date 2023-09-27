const redis = require('redis');
const express = require('express');
import { promisify } from 'util';
import { createQueue } from 'kue';

// redis
const client = redis.createClient();
const app = express();
app.listen('1245', () => {
  console.log('server is running on port 1245');
});

const number = 50;
let reservationEnabled = true;
const asyncGet = promisify(client.get).bind(client);
const queue = createQueue()

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const available_seats = await asyncGet('available_seats');
  return available_seats;
}

reserveSeat(number)

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ 'numberOfAvailableSeats': numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ 'status': 'Reservations are blocked' })
  } else {

    const job = queue.create('reserve_seat')
    job.save((err) => {
      if (err) {
        res.json({ 'status': 'Reservation failed' });
      } else {
        res.json({ 'status': 'Reservation in process' });
      }
    });
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
  }
});

app.get('/process', async (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    reserveSeat(currentAvailableSeats - 1);
    if (currentAvailableSeats - 1 === 0) {
      reservationEnabled = false;
    }
    if (currentAvailableSeats - 1 >= 0) {
      done()
    } else {
      const err = new Error('Not enough seats available');
      job.failed().error(err);
      done(err);
    }
  })
  res.json({ 'status': 'Queue processing'});
});
