import serial
import time
import logging

class PoseidonPump:
    """
    Driver for Poseidon Open Source Syringe Pumps (Arduino/GRBL based).
    """
    def __init__(self, port, baudrate=250000, steps_per_ml=1000):
        self.port = port
        self.baudrate = baudrate
        self.steps_per_ml = steps_per_ml # CALIBRATION VALUE (Exp 7)
        self.conn = None
        self.logger = logging.getLogger("Poseidon")
        logging.basicConfig(level=logging.INFO)

    def connect(self):
        try:
            self.conn = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2) # Wait for Arduino reboot
            self.conn.write(b"\r\n\r\n") # Wake up GRBL
            time.sleep(1)
            self.conn.flushInput()
            self.logger.info(f"Connected to {self.port}")
            self.send_gcode("G91") # Relative Positioning
            self.send_gcode("M17") # Enable Motors
        except serial.SerialException as e:
            self.logger.error(f"Failed to connect: {e}")

    def send_gcode(self, command):
        if not self.conn: return
        self.conn.write(f"{command}\r\n".encode())
        self.logger.debug(f"Sent: {command}")
        return self.conn.readline().decode().strip()

    def infuse(self, volume_ml, rate_ml_min):
        steps = volume_ml * self.steps_per_ml
        feed_rate = rate_ml_min * self.steps_per_ml
        self.send_gcode(f"G1 E{steps:.2f} F{feed_rate:.2f}")

    def close(self):
        if self.conn: self.conn.close()

if __name__ == "__main__":
    print("Poseidon Driver Library. Import this class to use.")
