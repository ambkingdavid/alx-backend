import { promisify } from "util";

const redis = require('redis');

const client = redis.createClient();

client.on('connect', (err, reply) => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    const data = await getAsync(schoolName);
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
