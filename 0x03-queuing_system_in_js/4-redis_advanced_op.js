const redis = require('redis')

const client = redis.createClient();

const key = 'HolbertonSchools';

const data = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

for (const field in data) {
  client.hset(key, field, data[field], redis.print);
}

client.hgetall(key, (err, hashData) => {
  if (err) {
    console.error(err);
  } else {
    console.log(hashData);
  }
});
