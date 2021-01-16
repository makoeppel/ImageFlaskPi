# Setup Service

Create file with: /etc/systemd/system/int\_image.service

```
sudo systemctl start int_image
sudo systemctl stop int_image
sudo systemctl status int_image
sudo systemctl enable int_image
```

# Get image

```
wget http://0.0.0.0:8080/image.jpg
```
