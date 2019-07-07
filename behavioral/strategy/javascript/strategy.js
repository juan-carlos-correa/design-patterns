class SmsStrategy {
  sendMessage (message) {
    console.log('SmsStrategy - sendMessage', message.getData())
  }
}

class EmailStrategy {
  sendMessage (message) {
    console.log('EmailStrategy - sendMessage', message.getData())
  }
}

class StrategyContext {
  constructor (strategy) {
    if (strategy === 'sms') {
      this.strategy = new SmsStrategy()
    } else if (strategy === 'email') {
      this.strategy = new EmailStrategy()
    }
  }

  sendMessage (message) {
    return this.strategy.sendMessage(message)
  }
}

class Message {
  constructor (data) {
    this.data = data
  }

  getData () {
    return this.data
  }
}

function sendSms () {
  const strategyContextSms = new StrategyContext('sms')

  strategyContextSms.sendMessage(new Message({
    phoneNumber: 123456789,
    message: 'Message for sms'
  }))
}

function sendEmail () {
  const strategyContextEmail = new StrategyContext('email')

  strategyContextEmail.sendMessage(new Message({
    email: 'john.doe@mail.com',
    message: 'Message for email'
  }))
}

sendSms()
sendEmail()
