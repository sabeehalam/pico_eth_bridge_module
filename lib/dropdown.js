

const protocol = document.getElementById("protocol");
const udp_client = document.getElementById("UDP-CLIENT");
const udp_serevr = document.getElementById("UDP-SERVER");
const tcp_client = document.getElementById("TCP-CLIENT");
const tcp_serevr = document.getElementById("TCP-SERVER");
const mqtt = document.getElementById("MQTT");


protocol.addEventListener("change", function() {
  const selectedValue = this.value;
  if (selectedValue === "UDP-CLIENT") {
    udp_client.style.display = "block";
    udp_server.style.display = "none";
    tcp_client.style.display = "none";
    tcp_server.style.display = "none";
    mqtt.style.display = "none";
  } else if (selectedValue === "UDP-SERVER") {
    udp_client.style.display = "none";
    udp_server.style.display = "block";
    tcp_client.style.display = "none";
    tcp_server.style.display = "none";
    mqtt.style.display = "none";
  } else if (selectedValue === "TCP-CLIENT") {
    udp_client.style.display = "none";
    udp_server.style.display = "none";
    tcp_client.style.display = "block";
    tcp_server.style.display = "none";
    mqtt.style.display = "none";
  }
  else if (selectedValue === "TCP-SERVER") {
    udp_client.style.display = "none";
    udp_server.style.display = "none";
    tcp_client.style.display = "none";
    tcp_server.style.display = "block";
    mqtt.style.display = "none";
    }
  else if (selectedValue === "MQTT") {
    udp_client.style.display = "none";
    udp_server.style.display = "none";
    tcp_client.style.display = "none";
    tcp_server.style.display = "none";
    mqtt.style.display = "block";
    }
});