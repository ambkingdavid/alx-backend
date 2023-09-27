import { createQueue } from "kue";

const queue = createQueue();

const blacklistedNumber = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumber.includes(phoneNumber)) {
    // If the phone number is blacklisted, fail the job
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(error);
    done(error)
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    job.complete();
    done()
  }
}

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});