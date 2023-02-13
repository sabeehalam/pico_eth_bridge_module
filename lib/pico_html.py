def getHTML():
    html = '''
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<head meta="" name="viewport" content="width=device-width,height=device-height,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no">
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width,height=device-height,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
  <script>
         function showDiv(id) {  
           const protocol = document.getElementById("protocol");
           const select_option = document.getElementById("SELECT-OPTION");
           const udp_client = document.getElementById("UDP-CLIENT");
           const udp_server = document.getElementById("UDP-SERVER");
           const tcp_client = document.getElementById("TCP-CLIENT");
           const tcp_server = document.getElementById("TCP-SERVER");
           const mqtt = document.getElementById("MQTT");
           
               udp_client.style.display = "none";
               udp_server.style.display = "none";
               tcp_client.style.display = "none";
               tcp_server.style.display = "none";
               mqtt.style.display = "none";
               select_option.style.display = "none";
               document.getElementById(id).style.display = "block";
           }
           
           function extractFormVars () {
              // (B1) FORM DATA OBJECT
                var data = new FormData();
                
                data.append("Timeout", document.getElementById("Timeout").value);
                data.append("MqPublishQos", document.getElementById("MqPublishQos").value);
                data.append("MqClientID", document.getElementById("MqClientID").value);
                data.append("MqPublishTopic", document.getElementById("MqPublishTopic").value);
                data.append("Baudrate", document.getElementById("Baudrate").value);
                data.append("LocalPort", document.getElementById("LocalPort").value);
                data.append("BufSize", document.getElementById("BufSize").value);
                data.append("KeepAlive", document.getElementById("KeepAlive").value);
                data.append("ServerPort", document.getElementById("ServerPort").value);
                data.append("Databits", document.getElementById("Databits").value);
                data.append("MqSubscribeTopic", document.getElementById("MqSubscribeTopic").value);
                data.append("MqPasswd", document.getElementById("MqPasswd").value);
                data.append("MqSubscribeQos", document.getElementById("MqSubscribeQos").value);
                data.append("Name", document.getElementById("Name").value);
                data.append("MqUSER", document.getElementById("MqUSER").value);
                data.append("PingTime", document.getElementById("PingTime").value);
                data.append("ConnectMode", document.getElementById("ConnectMode").value);
                data.append("Protocol", document.getElementById("Protocol").value);
                data.append("RegistMode", document.getElementById("RegistMode").value);
                data.append("Server", document.getElementById("Server").value);
                
                params = JSON.stringify(data)
                
                return params;
            }
 
  </script>
  
  <style>
         body,
         html {
         height: 100%;
         background-color: #f5f6f6;
         }
         html {
         -ms-text-size-adjust: 100%;
         -webkit-text-size-adjust: 100%;
         -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
         }
         body {
         background: #f4f4f4;
         font-family: "Open Sans", "Microsoft YaHei", "微软雅黑", MicrosoftJhengHei,
         "华文细黑", "Open Sans", "Helvetica Neue", Helvetica, STHeiti, MingLiu,
         Arial, sans-serif;
         font-size: 13px;
         font-weight: 400;
         margin: 50px;
         align: left
         padding: 0;
         color: #555;
         line-height: 1.4;
         }
         .form-control {
         display: block;
         width: 30%;
         max-width: 150px;
         height: 34px;
         padding: 3px 6px;
         font-size: 14px;
         line-height: 1.428571429;
         color: #555;
         background-color: #fff;
         background-image: none;
         border: 1px solid #ccc;
         border-radius: 4px;
         -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
         box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
         -webkit-transition: border-color ease-in-out 0.15s,
         box-shadow ease-in-out 0.15s;
         transition: border-color ease-in-out 0.15s, box-shadow ease-in-out 0.15s;
         }
         .form-control:focus {
         border-color: #66afe9;
         outline: 0;
         -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075),
         0 0 8px rgba(102, 175, 233, 0.6);
         box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075),
         0 0 8px rgba(102, 175, 233, 0.6);
         }
         .form-control:-moz-placeholder {
         color: #999;
         }
         .form-control::-moz-placeholder {
         color: #999;
         opacity: 1;
         }
         .form-control:-ms-input-placeholder {
         color: #999;
         }
         .form-control::-webkit-input-placeholder {
         color: #999;
         }
         .form-control[disabled],
         .form-control[readonly] {
         cursor: not-allowed;
         background-color: #eee;
         }
         .form-group {
         margin-bottom: 10px;
         }
         .form-group:last-of-type {
         margin-bottom: 0;
         }
         .form-horizontal .form-group:after,
         .form-horizontal .form-group:before {
         content: " ";
         display: table;
         }
         .form-horizontal .form-group:after {
         clear: both;
         }
         .form-horizontal .checkbox,
         .form-horizontal .checkbox-inline,
         .form-horizontal .control-label,
         .form-horizontal .radio,
         .form-horizontal .radio-inline {
         margin-top: 0;
         margin-bottom: 0;
         padding-top: 7px;
         }
         .form-horizontal .checkbox-inline {
         padding-bottom: 7px;
         }
         .form-horizontal .checkbox,
         .form-horizontal .radio {
         min-height: 27px;
         }
         .form-horizontal .form-group:after,
         .form-horizontal .form-group:before {
         content: " ";
         display: table;
         }
         .form-horizontal .form-group:after {
         clear: both;
         }
         .form-horizontal .control-label {
         text-align: center;
         }
         .container .jumbotron {
         border-radius: 5px;
         padding: 10px;
         }
         }
         .form-horizontal .control-label {
         text-align: left;
         }
         .submit button {
         margin: 20px 10px;
  </style>
  <title>Extensity Bridge</title>
</head>
<div class="container">
  <form method="get" id="bridge_module_form" onsubmit="return extractFormVars()"> 
    <div class="box-body">
      <div class="jumbotron">
        <div class="form-horizontal">
          <div class="box-title">
            <h4 iotlabel="serial_settings">Serial Settings</h4>
          </div>
          <div class="form-group">
            <label iotlabel="baud_rate">Baud Rate</label> <select class="col-sm-7 form-control" id="baud_rate" name="Baudrate" iotinput="int" placeholder="Baud Rate">
              <option value="600">
                600
              </option>
              <option value="1200">
                1200
              </option>
              <option value="2400">
                2400
              </option>
              <option value="4800">
                4800
              </option>
              <option value="9600">
                9600
              </option>
              <option value="19200">
                19200
              </option>
              <option value="38400">
                38400
              </option>
              <option value="57600">
                57600
              </option>
              <option value="115200">
                115200
              </option>
              <option value="230400">
                230400
              </option>
              <option value="460800">
                460800
              </option>
            </select>
          </div>
          <div class="form-group">
            <label class="col-sm-4 control-label" iotlabel="data_bit">Data Bit</label> <select class="col-sm-7 form-control" id="data_bit" name="Databits" iotinput="int" placeholder="Data Bit">
              <option value="5">
                5
              </option>
              <option value="6">
                6
              </option>
              <option value="7">
                7
              </option>
              <option value="8">
                8
              </option>
            </select>
          </div>
        </div>
      </div>
    </div>
    <div class="box border green" protocol="base" style="">
      <div class="box-title">
        <h4 iotlabel="basic_settings">Basic Settings</h4>
      </div>
      <div class="box-body">
        <div class="jumbotron">
          <div class="form-horizontal">
            <div class="form-group">
              <label iotlabel="name" class="col-sm-4 control-label">Name</label><input class="col-sm-7 form-control" id="name" iotinput="" name="Name" maxlength="19" placeholder="Name">
            </div>
            <div class="form-group">
              <label class="col-sm-4 control-label" iotlabel="protocol">Protocol</label> <select class="col-sm-7 form-control" id="protocol" name="Protocol" iotinput="" placeholder="Protocol" onchange="showDiv(this.value)">
                <option value="none" selected disabled hidden="">
                  Select an Option
                </option>
                <option value="TCP-SERVER">
                  Tcp Server
                </option>
                <option value="TCP-CLIENT">
                  Tcp Client
                </option>
                <option value="UDP-SERVER">
                  Udp Server
                </option>
                <option value="UDP-CLIENT">
                  Udp Client
                </option>
                <option value="MQTT">
                  MQTT
                </option>
              </select>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div id="SELECT-OPTION"></div>
    
    <div id="UDP-CLIENT">
        <div class="box border green" protocol="base" style="">
          <div class="box-title">
            <h4 iotlabel="socket_params_settings">Socket Settings UDP Client</h4>
          </div>
          <div class="box-body">
            <div class="jumbotron">
              <div class="form-horizontal">
                <div class="form-group">
                  <label iotlabel="server" class="col-sm-4 control-label">Server</label><input class="col-sm-7 form-control" id="server" iotinput="" name="Server" maxlength="99" placeholder="Server">
                </div>
                <div class="form-group">
                  <label iotlabel="server_port" class="col-sm-4 control-label">Server Port</label><input type="number" class="col-sm-7 form-control" id="server_port" iotinput="int" name="ServerPort" maxlength="6" min="1" max="65535" placeholder="Server Port" value="80">
                </div>
                <div class="form-group">
                  <label iotlabel="local_port" class="col-sm-4 control-label">Local Port</label><input type="number" class="col-sm-7 form-control" id="local_port" iotinput="int" name="LocalPort" maxlength="5" min="0" max="65535" placeholder="Local Port" value="1880">
                </div>
                <div class="form-group" iot-remote-not-supported="">
                  <label iotlabel="buffer_size" class="col-sm-4 control-label">Buffer Size</label><input type="number" class="col-sm-7 form-control" id="buffer_size" iotinput="int" name="BufSize" maxlength="4" min="32" placeholder="Buffer Size" max="8192">
                </div>
                <div class="form-group" iot-remote-not-supported="">
                  <label iotlabel="keep_alive">Keep Alive</label>(s) <input type="number" class="col-sm-7 form-control" id="keep_alive" iotinput="int" name="KeepAlive" min="0" max="2147483647" placeholder="Keep Alive">
                </div>
                <div class="form-group">
                  <label iotlabel="timeout">Timeout</label>(s) <input type="number" class="col-sm-7 form-control" id="timeout" iotinput="int" name="Timeout" min="0" max="600" placeholder="Timeout">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div id="UDP-SERVER">
        <div class="box border green" protocol="base" style="">
          <div class="box-title">
            <h4 iotlabel="socket_params_settings">Socket Settings UDP Server</h4>
          </div>
          <div class="box-body">
            <div class="jumbotron">
              <div class="form-horizontal">
                <div class="form-group">
                  <label iotlabel="local_port" class="col-sm-4 control-label">Local Port</label><input type="number" class="col-sm-7 form-control" id="local_port" iotinput="int" name="LocalPort" maxlength="5" min="0" max="65535" placeholder="Local Port" value="1880">
                </div>
                <div class="form-group" iot-remote-not-supported="">
                  <label iotlabel="buffer_size" class="col-sm-4 control-label">Buffer Size</label><input type="number" class="col-sm-7 form-control" id="buffer_size" iotinput="int" name="BufSize" maxlength="4" min="32" placeholder="Buffer Size" max="8192">
                </div>
                <div class="form-group" iot-remote-not-supported="">
                  <label iotlabel="keep_alive">Keep Alive</label>(s) <input type="number" class="col-sm-7 form-control" id="keep_alive" iotinput="int" name="KeepAlive" min="0" max="2147483647" placeholder="Keep Alive">
                </div>
                <div class="form-group">
                  <label iotlabel="timeout">Timeout</label>(s) <input type="number" class="col-sm-7 form-control" id="timeout" iotinput="int" name="Timeout" min="0" max="600" placeholder="Timeout">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div id="MQTT">
        <div class="box border green" protocol="base" style="">
          <div class="box-title">
            <h4 iotlabel="socket_params_settings">Socket Settings MQTT Client</h4>
          </div>
          <div class="box-body">
            <div class="jumbotron">
              <div class="form-horizontal">
                <div class="form-group">
                  <label iotlabel="server" class="col-sm-4 control-label">Server</label><input class="col-sm-7 form-control" id="server" iotinput="" name="Server" maxlength="99" placeholder="Server" value="192.168.0.102">
                </div>
                <div class="form-group">
                  <label iotlabel="server_port" class="col-sm-4 control-label">Server Port</label><input type="number" class="col-sm-7 form-control" id="server_port" iotinput="int" name="ServerPort" maxlength="6" min="1" max="65535" placeholder="Server Port" value="80">
                </div>
                <div class="form-group">
                  <label iotlabel="local_port" class="col-sm-4 control-label">Local Port</label><input type="number" class="col-sm-7 form-control" id="local_port" iotinput="int" name="LocalPort" maxlength="5" min="0" max="65535" placeholder="Local Port" value="1880">
                </div>
                <div class="form-group" iot-remote-not-supported="">
                  <label iotlabel="buffer_size" class="col-sm-4 control-label">Buffer Size</label><input type="number" class="col-sm-7 form-control" id="buffer_size" iotinput="int" name="BufSize" maxlength="4" min="32" placeholder="Buffer Size" max="8192">
                </div>
                <div class="form-group" iot-remote-not-supported="">
                  <label iotlabel="keep_alive">Keep Alive</label>(s) <input type="number" class="col-sm-7 form-control" id="keep_alive" iotinput="int" name="KeepAlive" min="0" max="2147483647" placeholder="Keep Alive">
                </div>
                <div class="form-group">
                  <label iotlabel="timeout">Timeout</label>(s) <input type="number" class="col-sm-7 form-control" id="timeout" iotinput="int" name="Timeout" min="0" max="600" placeholder="Timeout">
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="box border green" protocol="base" style="">
          <div class="box-title">
            <h4 iotlabel="protocol_settings">Protocol Settings MQTT Client</h4>
          </div>
          <div class="box-body">
            <div class="jumbotron">
              <div class="form-horizontal">
                <div class="form-group">
                  <label iotlabel="mqtt_client_id" class="col-sm-4 control-label">MQTT Client ID</label><input type="text" class="col-sm-7 form-control" id="mqtt_client_id" iotinput="" name="MqClientID" maxlength="128" placeholder="MQTT Client ID">
                </div>
                <div class="form-group">
                  <label iotlabel="mqtt_user" class="col-sm-4 control-label">MQTT Account</label><input type="text" class="col-sm-7 form-control" id="mqtt_user" iotinput="" name="MqUSER" maxlength="128" placeholder="MQTT Account">
                </div>
                <div class="form-group">
                  <label iotlabel="mqtt_password" class="col-sm-4 control-label">MQTT Password</label><input type="password" class="col-sm-7 form-control" id="mqtt_password" iotinput="" name="MqPasswd" maxlength="128" placeholder="MQTT Password"> <input type="checkbox" id="show_mqtt_password" for="MqPasswd" iotshowpassword="">
                </div>
                <div class="form-group">
                  <label iotlabel="mqtt_subscribe_topic" class="col-sm-4 control-label">Subscribe Topic</label><input type="text" class="col-sm-7 form-control" id="mqtt_subscribe_topic" iotinput="" name="MqSubscribeTopic" maxlength="128" placeholder="Subscribe Topic">
                </div>
                <div class="form-group">
                  <label class="col-sm-4 control-label" iotlabel="mqtt_subscribe_qos">Subscribe QoS</label> <select class="col-sm-7 form-control" id="mqtt_subscribe_qos" name="MqSubscribeQos" iotinput="int" placeholder="Subscribe QoS">
                    <option value="0">
                      0
                    </option>
                    <option value="1">
                      1
                    </option>
                    <option value="2">
                      2
                    </option>
                  </select>
                </div>
                <div class="form-group">
                  <label iotlabel="mqtt_publish_topic" class="col-sm-4 control-label">Publish Topic</label><input type="text" class="col-sm-7 form-control" id="mqtt_publish_topic" iotinput="" name="MqPublishTopic" maxlength="128" placeholder="Publish Topic">
                </div>
                <div class="form-group">
                  <label class="col-sm-4 control-label" iotlabel="mqtt_publish_qos">Publish QoS</label> <select class="col-sm-7 form-control" id="mqtt_publish_qos" name="MqPublishQos" iotinput="int" placeholder="Publish QoS">
                    <option value="0">
                      0
                    </option>
                    <option value="1">
                      1
                    </option>
                    <option value="2">
                      2
                    </option>
                  </select>
                </div>
                <div class="form-group">
                  <label iotlabel="ping_time">Ping Period</label>(s) <input type="number" class="col-sm-7 form-control" id="ping_time" iotinput="int" name="PingTime" min="0" max="2147483647" placeholder="Ping Period">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div id="TCP-CLIENT">
        <div class="box border green" protocol="base" style="">
          <div class="box-title">
            <h4 iotlabel="socket_params_settings">Socket Settings TCP Client</h4>
          </div>
          <div class="box-body">
            <div class="jumbotron">
              <div class="form-horizontal">
                <div class="form-group">
                  <label iotlabel="server" class="col-sm-4 control-label">Server</label><input class="col-sm-7 form-control" id="server" iotinput="" name="Server" maxlength="99" placeholder="Server" value="192.168.0.110">
                </div>
                <div class="form-group">
                  <label iotlabel="server_port" class="col-sm-4 control-label">Server Port</label><input type="number" class="col-sm-7 form-control" id="server_port" iotinput="int" name="ServerPort" maxlength="6" min="1" max="65535" placeholder="Server Port" value="80">
                </div>
                <div class="form-group">
                  <label iotlabel="local_port" class="col-sm-4 control-label">Local Port</label><input type="number" class="col-sm-7 form-control" id="local_port" iotinput="int" name="LocalPort" maxlength="5" min="0" max="65535" placeholder="Local Port" value="1880">
                </div>
                <div class="form-group" iot-remote-not-supported="">
                  <label iotlabel="buffer_size" class="col-sm-4 control-label">Buffer Size</label><input type="number" class="col-sm-7 form-control" id="buffer_size" iotinput="int" name="BufSize" maxlength="4" min="32" placeholder="Buffer Size" max="8192">
                </div>
                <div class="form-group" iot-remote-not-supported="">
                  <label iotlabel="keep_alive">Keep Alive</label>(s)
                  <input type="number" class="col-sm-7 form-control" id="keep_alive" iotinput="int" name="KeepAlive" min="0" max="2147483647" placeholder="Keep Alive">
              </div>
              <div class="form-group">
                <label iotlabel="timeout">Timeout</label>(s) <input type="number" class="col-sm-7 form-control" id="timeout" iotinput="int" name="Timeout" min="0" max="600" placeholder="Timeout">
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="box border green" protocol="base" style="">
        <div class="box-title">
          <h4 iotlabel="protocol_settings">Protocol Settings TCP Client</h4>
        </div>
        <div class="box-body">
          <div class="jumbotron">
            <div class="form-horizontal">
              <div class="form-group" style="">
                <label class="col-sm-4 control-label" iotlabel="connect_mode">Connect Mode</label> <select class="col-sm-7 form-control" id="connect_mode" name="ConnectMode" iotinput="" placeholder="Connect Mode">
                  <option value="Always">
                    Always
                  </option>
                  <option value="Burst">
                    Burst
                  </option>
                </select>
              </div>
              <div class="form-group" style="">
                <label class="col-sm-4 control-label" iotlabel="register_mode">Register Mode</label> <select class="col-sm-7 form-control" id="register_mode" name="RegistMode" iotinput="" placeholder="Register Mode">
                  <option value="Disable">
                    Disable
                  </option>
                  <option value="Link">
                    Link&lt;/&gt;
                  </option>
                  <option value="Data">
                    Data
                  </option>
                  <option value="Both">
                    Both
                  </option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div id="TCP-SERVER">
  <div class="box border green" protocol="base" style="">
    <div class="box-title">
      <h4 iotlabel="socket_params_settings">Socket Settings TCP Server</h4>
    </div>
    <div class="box-body">
      <div class="jumbotron">
        <div class="form-horizontal">
          <div class="form-group">
            <label iotlabel="local_port" class="col-sm-4 control-label">Local Port</label><input type="number" class="col-sm-7 form-control" id="local_port" iotinput="int" name="LocalPort" maxlength="5" min="0" max="65535" placeholder="Local Port" value="1880">
          </div>
          <div class="form-group" iot-remote-not-supported="">
            <label iotlabel="buffer_size" class="col-sm-4 control-label">Buffer Size</label><input type="number" class="col-sm-7 form-control" id="buffer_size" iotinput="int" name="BufSize" maxlength="4" min="32" placeholder="Buffer Size" max="8192">
          </div>
          <div class="form-group" iot-remote-not-supported="">
            <label iotlabel="keep_alive">Keep Alive</label>(s) <input type="number" class="col-sm-7 form-control" id="keep_alive" iotinput="int" name="KeepAlive" min="0" max="2147483647" placeholder="Keep Alive">
          </div>
          <div class="form-group">
            <label iotlabel="timeout">Timeout</label>(s) <input type="number" class="col-sm-7 form-control" id="timeout" iotinput="int" name="Timeout" min="0" max="600" placeholder="Timeout">
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="box border green" protocol="base" style="">
    <div class="box-title">
      <h4 iotlabel="protocol_settings">Protocol Settings TCP Server</h4>
    </div>
    <div class="box-body">
      <div class="jumbotron">
        <div class="form-horizontal">
          <div class="form-group" style="">
            <label class="col-sm-4 control-label" iotlabel="max_accept">Max Accept</label><input type="number" class="col-sm-7 form-control" id="max_accept" iotinput="int" name="maxAccept" min="1" max="20" maxlength="2" placeholder="Max Accept">
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="submit">
  <input iotlabel="submit" type="submit" value="Submit" >
</div>
  </form>
</div>
'''
    return html