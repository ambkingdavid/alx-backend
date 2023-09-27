const kue = require('kue');
const chai = require('chai');
const expect = chai.expect;
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Create a Kue queue and enter test mode
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  after(() => {
    // Clear the queue and exit test mode after all tests
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should create jobs for an array of valid job data', () => {
    const jobs = [
      {
        phoneNumber: '1234567890',
        message: 'Message 1',
      },
      {
        phoneNumber: '9876543210',
        message: 'Message 2',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Get the list of jobs in the queue
    const jobList = queue.testMode.jobs;

    // Expect two jobs to be created
    expect(jobList).to.have.lengthOf(2);

    // Check if the job properties match the input data
    expect(jobList[0].type).to.equal('push_notification_code_3');
    expect(jobList[0].data).to.deep.equal(jobs[0]);

    expect(jobList[1].type).to.equal('push_notification_code_3');
    expect(jobList[1].data).to.deep.equal(jobs[1]);
  });

  it('should throw an error for non-array input', () => {
    const invalidInput = 'not an array';
    
    expect(() => createPushNotificationsJobs(invalidInput, queue)).to.throw('Jobs is not an array');
  });
});
