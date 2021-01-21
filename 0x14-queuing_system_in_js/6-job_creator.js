import kue from "kue"
const queue = kue.createQueue();
const obj = {
    phoneNumber: "123456789",
    message: "Ready",
  }

const Newjob = queue.create('push_notification_code', obj);
Newjob.save();

Newjob.on('enqueue', (id, type) => {
  console.log(`Notification job created: ${Newjob.id}`)
});

Newjob.on('complete', (result) => {
  console.log('Notification job completed');
});
  
Newjob.on('failed', (err) => {
  console.log('Notification job failed');
});
