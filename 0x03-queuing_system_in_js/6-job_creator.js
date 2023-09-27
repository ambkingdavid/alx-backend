const kue = require('kue');

const queue = kue.createQueue();

const data = {
  phoneNumber: '0123456789',
  message: 'push notification',
};

const job = queue.create('push_notification_code', data);
job.save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.log(error);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (error) => {
  console.log('Notification job failed');
});
