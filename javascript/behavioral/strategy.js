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
  constructor ($strategy) {
    if ($strategy === 'sms') {
      this.strategy = new SmsStrategy()
    } else if ($strategy === 'email') {
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

// SMS
const dataToSms = {
  phoneNumber: 123456789,
  message: 'Message for sms'
}

const messageToSms = new Message(dataToSms)

const strategyContextSms = new StrategyContext('sms')
strategyContextSms.sendMessage(messageToSms)

// EMAIL
const dataToEmail = {
  email: 'john.doe@mail.com',
  message: 'Message for email'
}

const messageToEmail = new Message(dataToEmail)

const strategyContextEmail = new StrategyContext('email')
strategyContextEmail.sendMessage(messageToEmail)
