import torch
import torch.nn as nn

class CongestionLSTM(nn.Module):
    """
    Time-Series LSTM model predicting switch port queue occupancy 50-100ms in advance
    based on incoming packet arrival rate, byte throughput, and TCP window trends.
    """
    def __init__(self, input_dim: int = 5, hidden_dim: int = 64, num_layers: int = 2):
        super(CongestionLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=input_dim, hidden_size=hidden_dim, num_layers=num_layers, batch_first=True)
        self.regressor = nn.Sequential(
            nn.Linear(hidden_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid() # Normalized predicted buffer occupancy (0.0 to 1.0)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x shape: (batch_size, seq_len, input_dim)
        out, _ = self.lstm(x)
        pred_buffer = self.regressor(out[:, -1, :])
        return pred_buffer
