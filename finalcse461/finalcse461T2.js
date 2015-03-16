var dgram = require('dgram');
var util = require('util');
var readline = require('readline');
var fs = require('fs');
var ip_port_array = [];
var timer = null;
var timeout = 1000;
var stop_timer = null;
var stop_timeout = 10000;
var clientSocket = dgram.createSocket('udp4');
// make ctrl-d work
process.stdin.resume();

if (process.argv.length != 5) {
  // console.log(process.argv.length);
  console.log("Usage: node file.txt port time");
  process.exit(1);
}

var fileName = process.argv[2];
var self_port = process.argv[3];
var self_time = process.argv[4];
var self_IP = "localhost";
var confirm = false;

// take in file
fs.readFileSync(fileName).toString().split('\n').forEach(function (line) { 
	var ip_port = line.split(' ');
	ip_port_array.push([ip_port[0], ip_port[1]]);
})

// on message, if time is greater then take time
// confirm = true
clientSocket.on('message', function(message,remote) {
	var message = message.toString();
	// console.log("RECIEVED: " + message);
	var message = message.toString();
	var time_temp = message;
	if (parseInt(time_temp) >= parseInt(self_time)) {
		
		// console.log("new time:" + time_temp);
		// console.log("old_time" + self_time);
		if (parseInt(time_temp) > parseInt(self_time) || confirm == false){
			clearTimeout(stop_timer);
			stop_timer = null;
			stopTimer();
		}
		confirm = true;
		self_time = time_temp;
	}
});

clientSocket.bind(self_port);

testCallBack();
function testCallBack() {
	broadCast(function() {
		helloTimer();
		stopTimer();
	});
}

function stopTimer() {
	// console.log("hererer");
	// console.log(stop_timer == null);
	if (stop_timer == null) {
		stop_timer = setTimeout(function() { 
			if (confirm) {
				console.log(self_time);
				process.exit(0);
			} else {
				// console.log(confirm);
				process.exit(0);
			}
		}, stop_timeout);
	}
}


function helloTimer() {
	if (timer == null) {
		timer = setTimeout(function() { 
			timer = null;
			broadCastNoCall();
			// console.log("broadCast cur time: " + self_time);
			helloTimer();
		}, timeout);
	}
}

// first time set timer
function broadCast(callBack) {
	for (var i = 0; i < ip_port_array.length; i++) {
		var IP_temp = ip_port_array[i][0];
		var Port_temp = ip_port_array[i][1];
		if (IP_temp != self_IP || Port_temp != self_port){
			sendTime(IP_temp, Port_temp);
		}
	}
	callBack();
}

// don't set timer
function broadCastNoCall() {
	for (var i = 0; i < ip_port_array.length; i++) {
		var IP_temp = ip_port_array[i][0];
		var Port_temp = ip_port_array[i][1];
		if (IP_temp != self_IP || Port_temp != self_port){
			sendTime(IP_temp, Port_temp);
		}
	}
}

function sendTime(IP, Port) {
	var newTime = generateHeader(self_time);
	clientSocket.send(newTime, 0, newTime.length, Port, IP, function(err, bytes) {
	    if (err) throw err;
	});
}

function generateHeader(Time) {
  var message = new Buffer(Time.length);
  var allHead = Time;
  message.write(allHead, 0, allHead.length, 'utf8');
  return message;
}

// ctrl-d 
process.stdin.on('end', function() {
	// console.log("here");
	process.exit(1);
});