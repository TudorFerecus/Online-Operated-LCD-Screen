ssid = 'YOUR_SSID_HERE' # this is where you enter your WI-FI Connection's name (the ssid)
wlan_password = 'YOUR_PASSWORD_HERE' # this is where you enter your WI-FI Connection's password

I2C_SDA_PIN = 0 # This is the Pico's GPIO Pin you wirded to the I2C's SDA pin, CHANGE only if you want other pins, if you do so, you will need to change the I2C_ADDR
I2C_SCL_PIN = 1 # This is the Pico's GPIO Pin you wirded to the I2C's SCL pin, CHANGE only if you want other pins, if you do so, you will need to change the I2C_ADDR
I2C_ADDR     = 0x27 # This I2C Address, which coresponds with the pins you used for SCL and SDL, if you used other pins than in guide you should CHANGE it, as it shows in the step by step set up
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20 

# this sets up the website hosted by the pico, change only if you want th change the website's
# look, funtionality or layout, if not, this should not be changed
network_html = '''
    <!DOCTYPE html>
<html>
    <head> 
        <style>
        html, body{
    height: 100%;
    width: 100vw;
}

body{
    display: flex;
    align-items: center;
    flex-direction: column;
    
}

.title{
    display: flex;
    font-weight: 700;
    font-size: 25px;
    margin-top: 50px;
}


.input-area{
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.text{
    width: 200px;
    font-size: 17px;
}

.input{
    width: 300px;
    font-size: 17px;
}

.button{
    width: 120px;
    margin-top: 20px;

}
        </style>
        <title>Remote </title>
    </head>

    <body>
        <div class="title">LED Screen Remote Control</div>
        <div class="input-area">
            <div class="text">Enter the text you want to send to LED Screen</div>
            <input class='input' type="text" placeholder="your text (recommended max 32 chr)">
        </div>
        <button class="button">Submit</button>
    </body>
    <script>
    function changeWindowLocation()
    {
        var xhttp = new XMLHttpRequest();
        var inputValue = input.value;
        inputValue = inputValue.replace(/\s/g, '_');
        console.log(inputValue);
        xhttp.open('GET', '/led/'+ inputValue.length + '_'+ inputValue, true);
        xhttp.send();
    }


    var button = document.querySelector('.button');
    var input = document.querySelector('.input');

    button.addEventListener('click', function()  {
        console.log('merge');
        changeWindowLocation();
    })
    </script>
</html>'''