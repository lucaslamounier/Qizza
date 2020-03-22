from server.util.table import Table


class Agent:
  def __init__(self, learn_rate, discount_factor, num_states, num_actions):
    self.learn_rate = learn_rate
    self.discount_factor = discount_factor

    self.q_table = Table(num_states, num_actions)

  def update(self, state, action, reward, max_future_reward):
    # assume state_to_update is already encoded
    old_q_val = self.q_table.get(state, action)

    new_q_val = old_q_val + self.learn_rate * (reward + self.discount_factor * max_future_reward - old_q_val)

    self.q_table.set(state, action, new_q_val)


  def get_best_action(self, state):
    max_val = max(self.q_table.arr[state])
    max_idx = self.q_table.arr[state].index(max_val)

    return max_idx
