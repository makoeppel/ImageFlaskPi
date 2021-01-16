# Setup Service

Create file with: /etc/systemd/system/int\_image.service

[Unit]
Description=Int-Run-Image
After=network.target

[Service]
WorkingDirectory=/home/pi/Int-Run-Image/
ExecStart=/usr/bin/python /home/pi/Int-Run-Image/server.py
Restart=always

[Install]
WantedBy=multi-user.target

sudo systemctl start int\_image
sudo systemctl stop int\_image
sudo systemctl status int\_image

# Get image
wget http://0.0.0.0:8080/image.jpg
