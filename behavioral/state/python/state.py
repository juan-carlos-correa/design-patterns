import abc
import random

class Insurance(metaclass=abc.ABCMeta):
  def __init__(self, context_insurance):
    self.context_insurance = context_insurance

  @abc.abstractmethod
  def handle(self):
    pass

class ContextInsurance():
  def __init__(self, state_name='opened'):
    self.states = {
      'opened': InsuranceOpened(self),
      'discution': InsuranceDiscution(self),
      'negotiation': InsuranceNegotiation(self),
      'closed': InsuranceClosed(self)
    }

    self.change_state(state_name)

  def change_state(self, state_name):
    print('*** activating state: %s ***' %(state_name))

    new_state = self.states[state_name]
    self.current_state = new_state

  def handle(self):
    self.current_state.handle()

class InsuranceOpened(Insurance):
  def handle(self):
    print('insurance is open')
    self.context_insurance.change_state('discution')
    self.context_insurance.handle()

class InsuranceDiscution(Insurance):
  def handle(self):
    print('insurance is on discution')
    self.context_insurance.change_state('negotiation')
    self.context_insurance.handle()
    pass

class InsuranceNegotiation(Insurance):
  def handle(self):
    print('insurance is on negotiation')

    is_resolved = random.choice([True, False])

    if (is_resolved == True):
      self.context_insurance.change_state('closed')
    else:
      self.context_insurance.change_state('discution')

    self.context_insurance.handle()

class InsuranceClosed(Insurance):
  def handle(self):
    print('Congrats, the insurance is closed')

if __name__ == "__main__":
  context_insurance = ContextInsurance(state_name='opened')
  context_insurance.handle()