set puerto=com10
set firmwarePath=esp32-20180511-v1.9.4.bin
esptool --chip esp32 --port %puerto% erase_flash
esptool --chip esp32 --port %puerto% write_flash -z 0x1000 %firmwarePath%
pause