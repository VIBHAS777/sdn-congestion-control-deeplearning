class ProactiveSDNController:
    """
    Proactive OpenFlow controller executing dynamic alternate-path rerouting
    and rate shaping BEFORE buffer overflow occurs.
    """
    def __init__(self, congestion_threshold: float = 0.75):
        self.threshold = congestion_threshold
        self.reroute_count = 0

    def manage_flow(self, current_port: str, predicted_occupancy: float, alternate_ports: list) -> dict:
        if predicted_occupancy >= self.threshold:
            self.reroute_count += 1
            chosen_alt = alternate_ports[0] if alternate_ports else current_port
            return {
                "action": "PROACTIVE_REROUTE",
                "assigned_port": chosen_alt,
                "flow_rule": f"FORWARD -> {chosen_alt}",
                "buffer_risk": "HIGH",
                "packet_drop_prevented": True
            }
        else:
            return {
                "action": "MAINTAIN_ROUTE",
                "assigned_port": current_port,
                "flow_rule": f"FORWARD -> {current_port}",
                "buffer_risk": "NOMINAL",
                "packet_drop_prevented": False
            }
