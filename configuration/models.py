from django.db import models
from django import forms

class Module(models.Model):
    is_enable=models.BooleanField(default=False, null=False)
    is_online=models.BooleanField(default=False, null=False)
    addh=models.CharField(max_length=2, default="FF", blank=False, null=False)
    addl=models.CharField(max_length=2, default="FF", blank=False, null=False)
    channel=models.CharField(max_length=2,default="64", blank=False, null=False)
    uart_parity=models.CharField(max_length=1, default='0', blank=False, null=False)
    uart_baud_rate=models.CharField(max_length=1, default='3', blank=False, null=False)
    air_data_rate=models.CharField(max_length=1, default='2', blank=False, null=False)
    transmission_power=models.CharField(max_length=1, default='0', blank=False, null=False)
    wor_period=models.CharField(max_length=1, default=3, blank=False, null=False)
    enable_RSSI_ambient_noise=models.BooleanField(default=False, blank=False, null=False)
    enable_lbt=models.BooleanField(default=False, blank=False, null=False)
    enable_rssi=models.BooleanField(default=True, blank=False, null=False)
    enable_fixed_transmission=models.BooleanField(default=True, blank=False, null=False)
    power_down_lose_config=models.BooleanField(default=False, blank=False, null=False)
    timeout_sensors_read_packet = models.IntegerField(default=60, blank=False, null=False)
    timeout_config_packet = models.IntegerField(default=60, blank=False, null=False)
    timeout_handshake = models.IntegerField(default=60, blank=False, null=False)
    timeout_SYN = models.IntegerField(default=20, blank=False, null=False)
    timeout_SYNACK = models.IntegerField(default=20, blank=False, null=False)
    timeout_ACK = models.IntegerField(default=20, blank=False, null=False)
    
class ControlModule(Module):
    read_command_period= models.IntegerField(default=3, blank=False, null=False)
    check_sensors_period= models.IntegerField(default=30, blank=False, null=False)

class SensorModule(Module):
    name=models.CharField(max_length=255, blank=False, null=False, unique=True)
    crypt_key=models.BinaryField(max_length=8, blank=False)
    
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields='__all__'

    UART_PARITY_CHOICES = [
        ('0', '8N1'),
        ('1', '8O1'),
        ('2', '8E1'),
    ]
    
    UART_BAUD_RATE_CHOICES = [
        ('0', '1200'),
        ('1', '2400'),
        ('2', '4800'),
        ('3', '9600'),
        ('4', '19200'),
        ('5', '38400'),
        ('6', '57600'),
        ('7', '115200'),
    ]
    
    AIR_DATA_RATE_CHOICES = [
        ('0', '2.4k'),
        ('1', '4.8k'),
        ('2', '9.6k'),
        ('3', '19.2k'),
        ('4', '38.4k'),
        ('5', '62.5k'),
    ]
    
    TRANSMISSION_POWER_CHOICES = [
        ('0', '22'),
        ('1', '17'),
        ('2', '13'),
        ('3', '10'),
    ]

    WOR_PERIOD_CHOICES = [
        ('0','500'),
        ('1','1000'),
        ('2','500'),
        ('3','2000'),
        ('4','2500'),
        ('5','3000'),
        ('6','3500'),
        ('7','4000'),
    ]
    
    uart_parity = forms.ChoiceField(choices=UART_PARITY_CHOICES)
    uart_baud_rate = forms.ChoiceField(choices=UART_BAUD_RATE_CHOICES)
    air_data_rate = forms.ChoiceField(choices=AIR_DATA_RATE_CHOICES)
    transmission_power = forms.ChoiceField(choices=TRANSMISSION_POWER_CHOICES)
    wor_period = forms.ChoiceField(choices=WOR_PERIOD_CHOICES)


class SensorModuleForm(forms.ModelForm):
    class Meta:
        model = SensorModule
        exclude='is_online', 'is_enable', 'crypt_key' 


class ControlModuleForm(forms.ModelForm):
    class Meta:
        model = ControlModule
        exclude='is_online', 'is_enable'
