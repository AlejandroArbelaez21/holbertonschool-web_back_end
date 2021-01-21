export default function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
  jobs.forEach((job) => createJob(job.phoneNumber, job.message, queue) )
}

function createJob (phoneNumber, message, queue) {
  const obj = {
    phoneNumber: phoneNumber,
    message: message
  }

const Newjob = queue.create('push_notification_code_3', obj);

Newjob.save();

Newjob.on('enqueue', (id, type) => {
  console.log(`Notification job created: ${Newjob.id}`)
});

Newjob.on('complete', (result) => {
  console.log(`Notification job #${Newjob.id} completed`);
});

Newjob.on('failed', (errorMessage) => {
  console.log(`Notification job #${Newjob.id} failed: ${errorMessage}`);
});

Newjob.on('progress', (progress, data) => {
  console.log(`Notification job #${Newjob.id} ${progress}% complete`);
});

}
